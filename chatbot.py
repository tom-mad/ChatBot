import argparse

import openai
from dotenv import dotenv_values

config = dotenv_values("/home/freshman/trainings/Mastering-OpenAI-Python-APIs-Unleash-ChatGPT-and-GPT4/.env")

client = openai.OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end

def main():
    parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT")
    parser.add_argument("--personality", type=str, help="A brief summary of the chatbot's personality", default="friendly and helpful chatbot")
    args = parser.parse_args()

    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            user_input = input(bold(blue("You: ")))
            messages.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=200
            )

            messages.append(response.choices[0].message.model_dump(exclude_none=True))
            print(bold(red("Assistant: ")), response.choices[0].message.content)

        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
