import openai
from dotenv import dotenv_values

config = dotenv_values("/home/freshman/trainings/Mastering-OpenAI-Python-APIs-Unleash-ChatGPT-and-GPT4/.env")

client = openai.OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is the best color on earth according to diffrent countries?"}],
    max_tokens=200
)

print(completion)