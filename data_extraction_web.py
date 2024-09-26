from langchain_community.document_loaders import WebBaseLoader
from utils import open_ai_llm


urls = ["https://www.freshersnow.com/off-campus-drives/"]

loader = WebBaseLoader(urls)
documents = loader.load()  # list with same length of urls list


prompt_template = f"""
Extract the following information from {documents} in plain JSON format. Make sure the output uses double quotes and is free from any markdown, code blocks, or special characters like newlines ('\\n') or single quotes. The format should be:
[
    dictof("Job Title": "","Skill Set Required": "","Total Experience Required": "","Location": "")
]
Do not include any text other than the JSON output.
"""


completion = open_ai_llm(prompt_template)
result=completion.choices[0].message.content
print(result)
with open('job_profiles.json',"w") as f:
    f.write(result)
    
    

