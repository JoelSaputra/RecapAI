# RecapAI

This mini project is to recap financial news sourced from Finnhub, and summarize it using Google's Gemini API (`gemini-3.1-flash-lite` for summarization, `gemini-2.5-flash` for filtering).

The deployment of this project is in the bloomberg-lite project — RecapAI is being built and tested as a standalone side project first, and will later be ported into `bloomberg-lite`'s backend as a real feature once proven out here.

## How it works

1. **Fetch** — pulls the latest ~100 general market news articles from Finnhub's API.
2. **Filter** — Gemini narrows those down to the top 30 articles most relevant to the stock market and macroeconomic impact.
3. **Summarize** — Gemini produces, for each filtered article, 3 bullet points (a summary, a second summary sentence, and who/what is most impacted in market terms), returned as structured JSON.
4. **Store** — the summarized batch is saved to a local SQLite database, replacing the previous batch each time (not accumulated).
5. **Serve** — a lightweight endpoint reads straight from SQLite so the frontend never has to wait on Finnhub/Gemini directly.

The whole refresh cycle (fetch → filter → summarize → store) runs automatically on a schedule — every 2 hours, between 8am and 8pm — so news stays reasonably fresh without hammering either API's rate limits.

## Tech stack

- **Python / FastAPI** — backend API
- **Finnhub API** — news source
- **Google Gemini API** (`google-genai`) — filtering and summarization
- **SQLite** — local storage/cache
- **APScheduler** — scheduled background refresh

## Project setup

1. Clone the repo and create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API keys:
   ```
   FINNHUB_API_KEY=your_finnhub_key_here
   GEMINI_API_KEY=your_gemini_key_here
   ```

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints

| Endpoint | Purpose |
|---|---|
| `GET /news-getter` | Triggers a full fetch → filter → summarize → store refresh cycle. Runs automatically on the scheduler; not meant to be polled directly. |
| `GET /news` | Returns the currently stored summarized articles from SQLite. This is the endpoint a frontend should actually poll. |

## Status

- [x] Finnhub fetching
- [x] Gemini filtering + summarization
- [x] SQLite storage
- [x] Scheduled background refresh (8am-8pm, every 2 hours)
- [x] Serve endpoint
- [ ] Frontend
- [ ] Integration into `bloomberg-lite`
