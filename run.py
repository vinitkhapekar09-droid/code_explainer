import sys
from agents import reader_agent, explainer_agent


def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py <path_to_python_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Read the file
    try:
        with open(filepath, "r") as f:
            code = f.read()

    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

    print(f"\nAnalysing file: {filepath}\n")

    # Agent 1 reads and Understands
    analysis = reader_agent(code)

    # Agent 2 Explains and Suggests
    result = explainer_agent(code, analysis)

    print("\n" + "=" * 50 + "\n")
    print(result)
    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
