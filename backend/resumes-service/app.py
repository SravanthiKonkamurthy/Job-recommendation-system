from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload_resume")
async def upload_resume(resume: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, resume.filename)
    with open(file_path, "wb") as f:
        f.write(await resume.read())
    # For simplicity, just save file
    return {"filename": resume.filename, "message": "Uploaded successfully"}
