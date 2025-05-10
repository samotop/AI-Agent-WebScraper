from fastapi import FastAPI
from pydantic import BaseModel
from web_analyzer import analyze_website_data
import time

app = FastAPI()


class ScrapeRequest(BaseModel):
    url: str


@app.post("/scrape")
def scrape_website(data: ScrapeRequest):
    url = data.url
    response = analyze_website_data(url)
    return {"result": response}

