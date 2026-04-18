import pyttsx3
from openai import OpenAI

client = OpenAI()
voice = pyttsx3.init()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        # voice.say("Bye Boi")
        # voice.runAndWait()
        print("Chatbot ended.")
        break
    
    voice.runAndWait()
    prompt = (
        "Answer in easy english but in 1 line  only: " + user_input
    )  # this is prompt engineering
    response = client.responses.create(
        model="gpt-4.1-mini", input=prompt, max_output_tokens=50
    )

    print("AI:", response.output_text)
    voice.say(response.output_text)
 
