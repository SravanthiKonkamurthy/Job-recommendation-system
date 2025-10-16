from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

jobs = [
    {"title": "Data Engineer", "company": "Amazon", "skills": ["Python", "AWS", "ETL"], "location": "Seattle"},
    {"title": "Cloud Engineer", "company": "Google", "skills": ["GCP", "Kubernetes"], "location": "Mountain View"},
    {"title": "Backend Developer", "company": "Microsoft", "skills": ["Python", "FastAPI"], "location": "Redmond"},
]

@app.get("/recommendations")
def get_recommendations():
    # Simple rule: return all jobs for now
    return jobs
