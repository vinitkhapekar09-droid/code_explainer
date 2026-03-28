# Code Explainer

Code Explainer is a Python CLI tool that analyzes one or more Python files and generates a Markdown report with:
- a plain-English explanation,
- one concrete code improvement suggestion,
- a better filename suggestion,
- and (for multi-file runs) a project-level architecture summary.

It uses a multi-agent design powered by Groq (OpenAI-compatible API).

## What It Does

For each input file, the tool runs specialized agents in sequence:
1. Reader agent: Understands what the file does, key functions/classes, and inputs/outputs.
2. Explainer agent: Produces a junior-friendly explanation and one actionable improvement.
3. Namer agent: Suggests a clearer snake_case filename.

When multiple files are provided, a summary agent also generates:
- overall project overview,
- how files connect,
- highest-impact improvement for the codebase.

The final result is printed to the terminal and saved to `reports/report_YYYY-MM-DD_HH-MM-SS.md`.

## Features

- Analyze one file or multiple files in one command
- Generate readable per-file explanations
- Suggest practical, concrete improvements
- Recommend better filenames automatically
- Produce project-level summary for multi-file analysis
- Save every run as a timestamped Markdown report

## Tech Stack

- Python
- OpenAI Python SDK
- Groq API (OpenAI-compatible endpoint)
- python-dotenv
- Model: `llama-3.3-70b-versatile`

## Requirements

- Python 3.12+
- A Groq API key

## Setup

1. Clone the repository

```bash
git clone <your-repo-url>
cd code_explainer
```

2. Create and activate a virtual environment

Windows (PowerShell):

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create `.env` in the project root

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Analyze a single file:

```bash
python run.py agents.py
```

Analyze multiple files:

```bash
python run.py agents.py run.py
```

Generic form:

```bash
python run.py <file1.py> <file2.py> ...
```

## Output

Each run generates:
- terminal output with file-by-file results,
- a Markdown report in the `reports` directory.

Report sections include:
- per-file analysis and explanation,
- suggested filename,
- project summary (multi-file only).

## Project Structure

- `agents.py`: AI agents (`reader_agent`, `explainer_agent`, `namer_agent`, `summary_agent`)
- `run.py`: CLI entry point, orchestration, and report generation
- `requirements.txt`: pip dependencies
- `pyproject.toml`: project metadata and dependency declarations
- `reports/`: generated analysis reports (created automatically)

## Notes

- API errors are caught and returned as readable messages.
- If a file cannot be read, it is skipped and processing continues for other files.

## License

MIT


