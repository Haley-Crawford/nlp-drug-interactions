from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Enable CORS so your Vite frontend can communicate with it safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permits all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Backend is running!", "project": "NLP-Drug-Interactions"}

@app.get("/api")
async def call_api():
    url = 'https://api.fda.gov/download.json'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app.get("/api/test")
def test_endpoint():
    return {"message": "Hello from FastAPI backend"}