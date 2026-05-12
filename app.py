import streamlit as st
import time
from dotenv import load_dotenv
from utils import explain_error

# Load environment variables
load_dotenv(override=True)

st.set_page_config(
    page_title="StackMind - AI Error Explainer",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark modern UI
st.markdown("""
<style>
    /* Dark mode / modern UI CSS tweaks */
    .stTextArea textarea {
        font-family: monospace;
    }
    div[data-testid="stMarkdownContainer"] .card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #1E1E1E;
        margin-bottom: 1rem;
        border: 1px solid #333;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    div[data-testid="stMarkdownContainer"] .card h3 {
        margin-top: 0;
        color: #4da6ff;
        font-size: 1.25rem;
        margin-bottom: 0.75rem;
    }
    div[data-testid="stMarkdownContainer"] .card p {
        margin-bottom: 0;
        color: #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 StackMind")
st.markdown("### Your AI-powered runtime error explainer")

with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        language = st.selectbox("Programming Language", ["Python", "JavaScript", "TypeScript", "Java", "C++", "Go", "Rust", "Other"])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        is_advanced = st.toggle("Advanced Explanation")

    traceback = st.text_area("Error Traceback (Paste your error here)", height=150, placeholder="Traceback (most recent call last):\n...")
    code_snippet = st.text_area("Code Snippet (Optional)", height=150, placeholder="def my_function():\n    pass")

    if st.button("Explain My Error", type="primary", use_container_width=True):
        if not traceback.strip():
            st.error("Please provide an error traceback.")
        else:
            with st.spinner("Analyzing your error..."):
                try:
                    result = explain_error(language, traceback, code_snippet, is_advanced)
                    
                    st.success("Analysis Complete!")
                    
                    st.markdown('<div class="card"><h3>🔍 Root Cause</h3><p>{}</p></div>'.format(result.get("root_cause", "")), unsafe_allow_html=True)
                    st.markdown('<div class="card"><h3>🤔 Why It Happened</h3><p>{}</p></div>'.format(result.get("why_it_happened", "")), unsafe_allow_html=True)
                    
                    st.markdown('<div class="card"><h3>🛠️ Minimal Fix</h3></div>', unsafe_allow_html=True)
                    st.code(result.get("minimal_fix", ""), language=language.lower() if language != "Other" else "python")
                    
                    st.markdown('<div class="card"><h3>🛡️ Prevention Tip</h3><p>{}</p></div>'.format(result.get("prevention_tip", "")), unsafe_allow_html=True)
                    st.markdown('<div class="card"><h3>📚 Learn Next</h3><p>{}</p></div>'.format(result.get("learn_next", "")), unsafe_allow_html=True)
                    
                except ValueError as ve:
                    st.error(str(ve))
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'>StackMind • Built for beginners.</div>", unsafe_allow_html=True)
