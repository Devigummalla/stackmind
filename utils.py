import os
import json
from groq import Groq
from prompts import SYSTEM_PROMPT

def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your_api_key":
        raise ValueError("Please set a valid GROQ_API_KEY in the .env file.")
    return Groq(api_key=api_key)

def explain_error(language, traceback, code_snippet, is_advanced=False):
    client = get_groq_client()
    
    context = "Advanced Mode: Provide more technical depth." if is_advanced else "Beginner Mode: Keep it very simple."
    
    user_prompt = f"""
Language: {language}
Mode: {context}

Error Traceback:
{traceback}

Code Snippet (Optional):
{code_snippet}

Please explain this error and provide the output in JSON format with the following keys:
- root_cause
- why_it_happened
- minimal_fix
- prevention_tip
- learn_next
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.2,
    )
    
    try:
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        raise ValueError(f"Failed to parse LLM response: {e}")
