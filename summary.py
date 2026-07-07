import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def summarize_news(headline: str, url: str):

    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=f"Summarize this news in 4 sentences:\n\nHeadline: {headline}\n\n{url}"
    )

    return interaction.output_text

