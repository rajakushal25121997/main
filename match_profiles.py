from PyPDF2 import PdfReader
from utils import embeddings_openai, my_sql_connection, open_ai_llm

cursor,db=my_sql_connection()
embeddings = embeddings_openai()


# Parse the resume PDF
def parse_resume(pdf_file):
    reader = PdfReader(pdf_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text()
    return resume_text

resume_text = parse_resume("C:/Users/lenovo/Desktop/Job Matching/Hansika_upd.pdf")

cursor.execute("SELECT * FROM jobs")
jobs = cursor.fetchall()

job_docs = [{"page_content": f"{job[1]} {job[2]} {job[3]} {job[4]}"} for job in jobs]

job_matching_prompt=f"""
I am providing you some job profiles {job_docs} and a resume {resume_text} please read resume text and match with job profiles and return the most matches job profiles from resume
return the response in this format nothing else 
[
    dictof("Job Title": "","Skill Set Required": "","Total Experience Required": "","Location": "")
]
no preamble no other text no markdown
"""

matches=open_ai_llm(job_matching_prompt)

with open('matched_job_profiles.json',"w") as f:
    f.write(matches.choices[0].message.content)

