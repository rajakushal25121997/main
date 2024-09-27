from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from typing import List
import fitz
import ast


import requests
from bs4 import BeautifulSoup
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from urllib.parse import urljoin, urlparse
from collections import deque



from data_extraction_web import get_eval
from match_profiles import match_job_profile

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text()
    print(text)
    pdf_document.close()  # Close the document
    data=match_job_profile(text)
    
    return {"filename": file.filename, "profiles": ast.literal_eval(data['profiles'])}

@app.post("/load-urls/")
async def load_urls(urls: str = Form(...)):
    urls_list = [url.strip() for url in urls.split(',')]
    url_list=get_all_links(urls_list)
    if get_eval(url_list):  
        return {"status": 'Successfully'}


def get_all_links(base_url):

    all_links = []
    for url_link in base_url:
        visited = set()
        queue = deque([url_link])
        while queue:
            url = queue.popleft()
            if url in visited:
                continue

            visited.add(url)
            all_links.append(url)

            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find all anchor tags
                for link in soup.find_all('a', href=True):
                    full_url = urljoin(url_link, link['href'])
                    # Ensure the link is within the same domain
                    if urlparse(full_url).netloc == urlparse(url_link).netloc:
                        queue.append(full_url)
            except Exception as e:
                print(f"Error retrieving {url}: {e}")

    return all_links
