# AI Agent WebScraper

This project demonstrates an AI-powered web scraping tool using LangChain, FastAPI, and Retool.

## What it does

- Accepts a URL input from the user via Retool UI
- Sends the request to a FastAPI backend
- A LangChain agent analyzes and summarizes content from the website
- Displays the final result back in the Retool interface

## Tech Stack

- **LangChain** – for AI agent creation and orchestration
- **FastAPI** – to build the REST API backend
- **Retool** – to create the front-end interface
- **Ngrok** – to expose the local backend for external access

## How to Run

1. Clone the repo:
   ```
   git clone https://github.com/samotop/AI-Agent-WebScraper.git
   cd AI-Agent-WebScraper
   ```

2. Create virtual environment and install dependencies:
   ```
   pipenv install
   pipenv shell
   ```

3. Start the FastAPI server:
   ```
   uvicorn api.api:app --reload
   ```

4. Start ngrok to expose the API:
   ```
   ngrok http 8000
   ```

5. Open Retool, create a REST query and call the API:
   ```
   POST https://xxxxxx.ngrok-free.app/scrape
   body:
   {
     "url": "https://example.com"
   }
   ```
