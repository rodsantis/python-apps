from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()


def get_car_ai_bio(model, brand, year):
    prompt = f"Get me a sales description for the following car with only 250 characters: {model} {brand} {year}."
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )
    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt,
        instructions="Be technical like a dealership seller's person!"
    )
    return response.output_text