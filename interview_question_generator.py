import openai
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = openai.OpenAI(api_key=api_key)


def generate_questions(role, experience, skills, question_types):
    prompt = f"""
    You are a senior engineering interviewer.
    Generate {', '.join(question_types)} interview questions for a {role} with {experience} years of experience.
    The candidate is skilled in {', '.join(skills)}.

    Provide:
    - A clear question
    - Type (e.g., Coding, System Design, Behavioral)
    - A short expected answer or evaluation guideline
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert technical interviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content.strip()


# Streamlit UI
st.set_page_config(page_title="AI Interview Question Generator")
st.title("AI Interview Question Generator")

role = st.text_input("Role Title", "Engineering Manager")
experience = st.slider("Years of Experience", 1, 20, 7)
skills = st.text_input("Key Skills (comma-separated)", "Java, Spring Boot, Kubernetes")
question_types = st.multiselect(
    "Question Types",
    ["Coding", "System Design", "LLM/AI"],
    default=["Coding", "System Design", "LLM/AI"]
)

if st.button("Generate Questions"):
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    output = generate_questions(role, experience, skills_list, question_types)
    st.markdown("---")
    st.subheader("Generated Questions")
    st.text_area("Questions", output, height=400)
