from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    # You can add code here to process the PDF content
    return {"filename": file.filename}

@app.post("/load-urls/")
async def load_urls(urls: str = Form(...)):
    url_list = [url.strip() for url in urls.split(',')]
    # Add logic to process the URLs here
    return {"urls": url_list}

