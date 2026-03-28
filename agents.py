from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
)


def call_ai(system, message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": message},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"  AI call failed: {e}")
        return "Error: could not get response from AI"


def reader_agent(filename: str, code: str) -> str:
    print(f"  [Reader] Understanding {filename}...")

    system = """You are a senior developer.
Read the given Python code and extract:
1. What this file does in one sentence
2. The main functions or classes and what each does
3. What inputs it takes and what outputs it returns
Be factual. No fluff."""

    return call_ai(system, f"Filename: {filename}\n\nCode:\n{code}")


def explainer_agent(filename: str, code: str, analysis: str) -> str:
    print(f"  [Explainer] Writing explanation for {filename}...")

    system = """You are a great technical writer.
You receive code and an analysis of it.
Write two things:

EXPLANATION:
A clear 3-5 sentence explanation a junior developer can understand.
No jargon. Plain English only.

SUGGESTION:
One specific improvement the developer could make to this code.
Be concrete — name the exact function or line to change."""

    message = f"""Filename: {filename}

Code:
{code}

Analysis:
{analysis}"""

    return call_ai(system, message)


def namer_agent(filename: str, analysis: str) -> str:
    print(f"  [Namer] Suggesting better filename for {filename}...")

    system = """You are a developer who follows clean code naming conventions.
Based on what a Python file does, suggest a better snake_case filename.
Output only the filename with .py extension. Nothing else."""

    return call_ai(system, f"Current name: {filename}\n\nThis file does:\n{analysis}")


def summary_agent(all_analyses: dict) -> str:
    print("\n  [Summarizer] Writing project summary...")

    system = """You are a senior software architect.
You are given analyses of multiple files from the same project.
Write a project summary covering:

PROJECT OVERVIEW:
What this project does overall in 2-3 sentences.

HOW THE FILES CONNECT:
How these files work together. Which calls which.

BIGGEST IMPROVEMENT:
The single most impactful improvement for the whole codebase.

Be specific and practical."""

    # Build a readable summary of all files
    combined = ""
    for filename, analysis in all_analyses.items():
        combined += f"\nFILE: {filename}\n{analysis}\n"

    return call_ai(system, f"Here are all the file analyses:\n{combined}")
