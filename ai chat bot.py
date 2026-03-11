import openai
openai.api_key = "hsk-proj-s0fUrcgsRbxR3ZM41Co_erKvnVhLAepHILRAT0L8-9bvCwvuexxvfyhl0vKEjcXEyo38caT5kDT3BlbkFJR2f4QerEcQoj6JytJnh7VUHg00LFcS5t_JuV0_WrWDTsyHzaYYcBuyNcQPn-F6w4853x79DgIA"
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