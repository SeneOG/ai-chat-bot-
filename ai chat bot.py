import os
import sys
import openai


def _get_api_key():
    # Prefer environment variable for security
    return os.getenv("OPENAI_API_KEY")


def chat_with_gpt(prompt, messages=None, model="gpt-3.5-turbo"):
    """Send `prompt` (and optional `messages` history) to OpenAI ChatCompletion.

    Returns tuple of (assistant_text, updated_messages).
    """
    if messages is None:
        messages = []

    messages.append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=512,
            temperature=0.7,
        )
        assistant_text = response.choices[0].message["content"].strip()
        messages.append({"role": "assistant", "content": assistant_text})
        return assistant_text, messages
    except Exception as exc:
        # Return a readable error message but keep the conversation history
        return f"Error: {exc}", messages


def main():
    api_key = _get_api_key()
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Set it with: setx OPENAI_API_KEY \"<your_key>\" (Windows) or export OPENAI_API_KEY=... (Unix)")
        sys.exit(1)

    openai.api_key = api_key

    print("Simple chat. Type 'quit' or 'exit' to stop.")

    # Optional system instruction to set behavior
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    try:
        while True:
            try:
                user_input = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting chat.")
                break

            if not user_input:
                continue

            if user_input.lower() in ("quit", "exit", "bye"):
                print("Chatbot: Goodbye! Have a nice day.")
                break

            reply, messages = chat_with_gpt(user_input, messages=messages)
            print("Chatbot:", reply)
    except KeyboardInterrupt:
        print("\nInterrupted. Bye!")


if __name__ == "__main__":
    main()