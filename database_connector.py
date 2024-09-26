from utils import my_sql_connection
import json 

cursor,db=my_sql_connection()

# Create table to store job listings
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(255),
    skills TEXT,
    experience VARCHAR(50),
    location VARCHAR(255)
)
""")

# # Insert data into the jobs table

with open("C:/Users/lenovo/Desktop/Job Matching/job_profiles.json",'r') as f:
    job_listings=json.load(f)

for job in job_listings:
    sql = "INSERT INTO jobs (job_title, skills, experience, location) VALUES (%s, %s, %s, %s)"
    values = (job["Job Title"], job["Skill Set Required"], job["Total Experience Required"], job["Location"])
    cursor.execute(sql, values)

db.commit()
