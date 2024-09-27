
from utils import open_ai_llm
from langchain_community.document_loaders import WebBaseLoader
from database_connector import store_db
import json
import ast


def get_eval(url_list):
  job_prifile_list=[]
  loader = WebBaseLoader(url_list)
  documents = loader.load()
  for document in documents:
    result=get_data_from_web(document)
    result_lst=ast.literal_eval(result)
    
    job_prifile_list.extend(result_lst)
  store_db(job_prifile_list)
  return True

def get_data_from_web(documents):
    prompt_template = f"""
    Extract the following information from {documents} in plain JSON format. Make sure the output uses double quotes and is free from any markdown, code blocks, or special characters like newlines ('\\n') or single quotes. The format should be:
    [
        dictof("Job Title": "","Skill Set Required": "","Total Experience Required": "","Location": "")
    ]
    Do not include any text other than the JSON output.
    """

    completion = open_ai_llm(prompt_template)
    result=completion.choices[0].message.content
    return result
    
    
    

