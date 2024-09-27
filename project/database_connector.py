from utils import my_sql_connection
import json 

cursor,db=my_sql_connection()
def store_db(job_listings):
    # Create table to store job listings
    try:
        cursor.execute("DROP TABLE jobs")
    except Exception as e:
        pass
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        job_title VARCHAR(255),
        skills TEXT,
        experience VARCHAR(255),
        location VARCHAR(255)
    )
    """)

    print(job_listings)
    for job in job_listings:
        sql = "INSERT INTO jobs (job_title, skills, experience, location) VALUES (%s, %s, %s, %s)"
        values = (job["Job Title"], job["Skill Set Required"], job["Total Experience Required"], job["Location"])
        cursor.execute(sql, values)
    db.commit()
    return {'status':"success"}


