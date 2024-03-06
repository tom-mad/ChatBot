import openai
from dotenv import dotenv_values

config = dotenv_values("/home/freshman/trainings/Mastering-OpenAI-Python-APIs-Unleash-ChatGPT-and-GPT4/.env")

client = openai.OpenAI(
    api_key=config["OPENAI_API_KEY"],
)


while True:
    try:
        user_input = input("You: ")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=200
        )
        print(response.choices[0].message.content)
    except KeyboardInterrupt:
        print("Exiting...")
        break
