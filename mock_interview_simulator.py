import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Mock Interview Simulator", layout="wide")
st.title("🎙️ Mock Interview Simulator")
st.markdown("Simulate a real interview experience with AI. Answer questions in real-time and get feedback.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "started" not in st.session_state:
    st.session_state.started = False
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "skills" not in st.session_state:
    st.session_state.skills = []

# Sidebar config
with st.sidebar:
    st.header("Setup")
    role = st.text_input("Role", "Software Engineer")
    experience = st.slider("Years of Experience", 0, 20, 6)
    skills_input = st.text_input("Enter skills (comma separated)", "Python, Django, REST APIs")

    show_feedback = st.checkbox("Give feedback after each answer", value=True)

    if st.button("Start Interview"):
        st.session_state.messages = []
        st.session_state.started = True
        st.session_state.skills = [s.strip() for s in skills_input.split(",") if s.strip()]
        # Add system prompt and first question
        intro = f"You are a technical interviewer. Interview a candidate for a {role} role with {experience} years of experience. They are skilled in {', '.join(st.session_state.skills)}. Ask one question at a time. Wait for the candidate's response before continuing."
        st.session_state.messages.append({"role": "system", "content": intro})
        st.session_state.messages.append({"role": "user", "content": "Start the interview."})

        # Trigger assistant's first reply
        response = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=1000
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat if started
if st.session_state.started:
    for msg in st.session_state.messages[2:]:  # skip system & trigger
        if msg["role"] == "assistant":
            st.markdown(f"**Interviewer:** {msg['content']}")
        else:
            st.markdown(f"**You:** {msg['content']}")

    def submit():
        if st.session_state.user_input:
            st.session_state.messages.append({"role": "user", "content": st.session_state.user_input})

            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=st.session_state.messages,
                    temperature=0.7,
                    max_tokens=1000
                )

            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.session_state.user_input = ""
            st.rerun()

    st.text_input("Your Response", value=st.session_state.user_input, key="user_input", on_change=submit)
    st.button("Send", on_click=submit)
else:
    st.info("Configure the interview from the sidebar and click 'Start Interview' to begin.")
