import openai
from dotenv import dotenv_values

config = dotenv_values("/home/freshman/trainings/Mastering-OpenAI-Python-APIs-Unleash-ChatGPT-and-GPT4/.env")

client = openai.OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

messages = []

while True:
    try:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200
        )

        messages.append(response.choices[0].message.model_dump(exclude_none=True))
        print(f"Assistant: {response.choices[0].message.content}")

    except KeyboardInterrupt:
        print("Exiting...")
        break
