SYSTEM_PROMPT = """You are a senior software engineer helping a beginner debug errors.

Your task:
* Identify the actual root cause
* Explain in beginner-friendly language
* Suggest the smallest correct fix
* Avoid overengineering
* Teach the core concept briefly
* Keep answers concise and practical
* Do not dump large rewritten code unless necessary"""

JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "root_cause": {"type": "string"},
        "why_it_happened": {"type": "string"},
        "minimal_fix": {"type": "string"},
        "prevention_tip": {"type": "string"},
        "learn_next": {"type": "string"}
    },
    "required": ["root_cause", "why_it_happened", "minimal_fix", "prevention_tip", "learn_next"]
}
