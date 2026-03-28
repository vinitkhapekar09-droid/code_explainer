import sys
import os
from datetime import datetime
from agents import reader_agent, explainer_agent, namer_agent, summary_agent


def read_file(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"  File not found: {filepath}")
        return None


def save_report(content: str):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = f"reports/report_{timestamp}.md"
    with open(filepath, "w") as f:
        f.write(content)
    print(f"\n  Report saved → {filepath}")
    return filepath


def process_single_file(filepath):
    filename = os.path.basename(filepath)
    code = read_file(filepath)
    if not code:
        return None, None

    analysis = reader_agent(filename, code)
    result = explainer_agent(filename, code, analysis)
    new_name = namer_agent(filename, analysis)

    return analysis, {
        "filename": filename,
        "new_name": new_name,
        "result": result,
        "analysis": analysis,
    }


def build_report(file_results: list, summary: str, filepaths: list) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append(f"# Code Analysis Report")
    lines.append(f"Generated: {timestamp}")
    lines.append(f"Files analysed: {len(filepaths)}")
    lines.append("")

    # Project summary only if multiple files
    if len(file_results) > 1 and summary:
        lines.append("---")
        lines.append("## Project Summary")
        lines.append("")
        lines.append(summary)
        lines.append("")

    # Individual file sections
    for data in file_results:
        lines.append("---")
        lines.append(f"## {data['filename']}")
        lines.append("")
        lines.append(f"**Suggested name:** `{data['new_name']}`")
        lines.append("")
        lines.append(data["result"])
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python run.py myfile.py")
        print("  python run.py file1.py file2.py file3.py")
        sys.exit(1)

    filepaths = sys.argv[1:]
    print(f"\nAnalysing {len(filepaths)} file(s)...\n")

    file_results = []
    all_analyses = {}

    # Process every file
    for filepath in filepaths:
        print(f"Processing: {filepath}")
        analysis, data = process_single_file(filepath)

        if data:
            file_results.append(data)
            all_analyses[data["filename"]] = analysis

        print()

    if not file_results:
        print("No files could be processed.")
        sys.exit(1)

    # If multiple files, run summary agent
    summary = ""
    if len(file_results) > 1:
        summary = summary_agent(all_analyses)

    # Build and save the report
    report = build_report(file_results, summary, filepaths)

    print("\n" + "=" * 50)
    print(report)
    print("=" * 50)

    save_report(report)


if __name__ == "__main__":
    main()
