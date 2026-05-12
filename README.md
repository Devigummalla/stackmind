# StackMind 🧠

StackMind is an AI-powered runtime error explainer for beginner developers. It takes your error tracebacks and code snippets, and provides simple, easy-to-understand explanations of what went wrong and how to fix it.

## Features
- **Root Cause Analysis**: Explains the core issue simply.
- **Why It Happened**: Contextualizes the error.
- **Minimal Fix**: Provides the exact code needed to fix the issue, with copy-to-clipboard support.
- **Prevention Tip**: Helps you avoid the bug in the future.
- **Learn Next**: Suggests related concepts to deepen your understanding.
- **Beginner/Advanced Toggle**: Tailors the explanation depth.

## Setup Instructions

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env` to `.env` (if not present) and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Sample Demo Inputs
**Language**: Python
**Error Traceback**:
```
IndexError: list index out of range
```
**Code Snippet**:
```python
my_list = [1, 2, 3]
print(my_list[3])
```

## Deployment
This app is ready to be deployed on [Streamlit Community Cloud](https://streamlit.io/cloud).
1. Push this repository to GitHub.
2. Go to Streamlit Community Cloud and select "New app".
3. Point to your repository and `app.py`.
4. Add your `GROQ_API_KEY` in the Advanced Settings -> Secrets section.
