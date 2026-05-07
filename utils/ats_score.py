COMMON_SKILLS = [
    'python',
    'java',
    'sql',
    'aws',
    'docker',
    'kafka',
    'flask',
    'rest api',
    'javascript',
    'microservices',
    'react',
    'mongodb',
    'postgresql',
    'ci/cd',
    'machine learning',
    'oop',
    'agile'
]

def clean_text(text):

    return text.lower()

def calculate_ats_score(resume_text, job_description):

    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    matched = []
    missing = []

    for skill in COMMON_SKILLS:

        if skill in resume_text and skill in job_description:
            matched.append(skill)

        elif skill in job_description:
            missing.append(skill)

    total_required = len(matched) + len(missing)

    if total_required == 0:
        score = 0

    else:
        score = int(
            (len(matched) / total_required) * 100
        )

    return score, matched, missing