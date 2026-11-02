import openai
OPENAI_API_KEY=your-new-key-here
def chat_with_gpt(prompt):
    response = openai.chatcompletions.create(
        model = "gpt-3.5-turbo",
        massages = [{"role": "user" , "content": prompt}]
    )
    return response.choices[0].massage.content.strip()
if __name__ == "__main":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit" , "exit" , "bye"]:
            print("chatbot: Good bye! Have a nice day")
            break
        response = chat_with_gpt(user_input)
        print("chatbot: " , response)