import requests

def chat_cli():
    print("Welcome to the Chat App! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": user_input},
                headers={"Content-Type": "application/json"},
            )
            if response.status_code == 200:
                bot_response = response.json().get("response", "")
                print(f"Bot: {bot_response}")
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
