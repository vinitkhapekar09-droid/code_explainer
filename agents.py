from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
)


def call_ai(system, message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content


def reader_agent(code: str) -> str:
    print("[Agent 1 - Reader] Understanding the code...")
    system = """You are a senior software engineer with expertise in code analysis and explanation. 
                Read the given Python code and extract:
                1. What the code does in one Sentence.
                2. The main functions or classes and what each does.
                3. what inputs it takes and what it returns.
                Be factual. No fluff.
            """
    return call_ai(system, f"Here is the code:\n\n{code}")


def explainer_agent(code: str, analysis: str) -> str:
    print("[Agent 2 - Explainer] Writing the explaination and Suggestion ...")

    system = """You are a great technical writer.
                You recieve a code and an analysis of it.
                Write two things:
                Explaination:
                A clear 3-5 sentence explaination a junior developer can understand.
                No jargon. Plain English Only.

                Suggestion:
                One specific improvement the developer could make to this code.
                Be concrete - name the exact function or line to change.
            """
    message = f"""Code:
    {code}

    Analysis:
    {analysis}
    """
    return call_ai(system, message)
