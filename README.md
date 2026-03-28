# Code Explainer

An AI-powered tool that analyzes Python code and generates clear explanations along with improvement suggestions using multi-agent LLM orchestration.

## Project Overview

**Code Explainer** uses two specialized AI agents to break down Python code:
- **Reader Agent**: Analyzes the code to understand its purpose, main functions/classes, and inputs/outputs
- **Explainer Agent**: Writes clear, beginner-friendly explanations and provides specific improvement suggestions

The tool leverages the Groq API with the Llama 3.3 70B model for fast and accurate code analysis.

## Features

- 📖 Clear code explanations for junior developers
- 🔍 Automatic code analysis and structure identification
- 💡 Specific, actionable improvement suggestions
- ⚡ Fast processing using Groq's API
- 🤖 Multi-agent LLM approach for comprehensive analysis

## Requirements

- Python 3.8+
- OpenAI compatible API (Groq)
- GROQ_API_KEY environment variable

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd code_explainer
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # On Windows
source .venv/bin/activate     # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the code explainer on any Python file:

```bash
python run.py <path_to_python_file>
```

### Example

```bash
python run.py agents.py
```

Output will include:
- Code analysis (what it does, functions/classes, inputs/outputs)
- Clear explanation suitable for junior developers
- Specific improvement suggestion

## Project Structure

- `agents.py` - Core AI agents (reader_agent, explainer_agent)
- `run.py` - Main entry point and CLI handler
- `main.py` - Project scaffold
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create this file)

## Technologies Used

- **Groq API** - High-performance inference
- **Llama 3.3 70B** - LLM engine
- **OpenAI SDK** - API client

## License

MIT

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
