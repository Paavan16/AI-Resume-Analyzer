import ollama

def generate_feedback(resume_text, job_description):

    prompt = f"""
    Analyze this resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give:
    1. ATS score explanation
    2. Missing skills
    3. Resume improvement suggestions
    4. Better professional summary suggestions
    5. Important ATS keywords missing
    """

    response = ollama.chat(
        model='llama3',

        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']