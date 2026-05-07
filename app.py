from flask import Flask, render_template, request
from utils.resume_parser import extract_text
from utils.ats_score import calculate_ats_score
from utils.ai_feedback import generate_feedback
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    resume = request.files['resume']
    job_description = request.form['job_description']

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        resume.filename
    )

    resume.save(filepath)

    resume_text = extract_text(filepath)

    ats_score, matched_skills, missing_skills = calculate_ats_score(
        resume_text,
        job_description
    )

    feedback = generate_feedback(
        resume_text,
        job_description
    )

    return render_template(
        'index.html',
        ats_score=ats_score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        feedback=feedback
    )

if __name__ == '__main__':
    app.run(debug=True)