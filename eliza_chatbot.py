import random

# Eliza-style responses
responses = [
    "Tell me more about that.",
    "Why do you say that?",
    "How does that make you feel?",
    "Can you elaborate?",
    "I see. What else comes to mind?"
]

def eliza_response(user_input):
    return random.choice(responses)

def main():
    print("Eliza: Hello! I'm Eliza. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Eliza: Goodbye!")
            break
        response = eliza_response(user_input)
        print(f"Eliza: {response}")

if __name__ == "__main__":
    main()
