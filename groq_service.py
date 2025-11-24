import streamlit as st
from openai import OpenAI

def get_groq_client():
    """Initializes and returns the OpenAI client for Groq."""
    # Check for key at root or under [api_keys] section
    api_key = st.secrets.get("GROQ_API_KEY")
    if not api_key and "api_keys" in st.secrets:
        api_key = st.secrets["api_keys"].get("GROQ_API_KEY")
        
    if not api_key:
        return None
    
    return OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key
    )

def score_job(job_description, profile_content):
    """
    Scores a job opportunity against a user profile using Groq's Llama 3.3 model.
    
    Args:
        job_description (str): The text of the job advertisement.
        profile_content (str): The user's LinkedIn profile content or resume summary.
        
    Returns:
        str: The model's analysis and score.
    """
    client = get_groq_client()
    if not client:
        return "Error: GROQ_API_KEY not found in secrets."

    prompt = f"""
    You are a career coach and recruiter. 
    Analyze the following Job Description against the Candidate Profile.
    
    Candidate Profile:
    {profile_content}
    
    Job Description:
    {job_description}
    
    Task:
    1. Give a match score from 0-100.
    2. List 3 key strengths of the candidate for this role.
    3. List 3 potential gaps or areas to address.
    4. Provide a brief verdict: "Apply", "Consider", or "Skip".
    
    Format the output clearly with markdown.
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful career assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1024,
            stream=False
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error communicating with Groq: {str(e)}"
