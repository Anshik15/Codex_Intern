import google.generativeai as genai

genai.configure(api_key="AIzaSyDNus3YOkIgSkW8VmLA5E8BiV2B71Dgklw")

model=genai.GenerativeModel('gemini-2.0-flash')
chat_history=[]
while True:
    q=input("how I can help you: ")
    chat_history.append(f"user: {q}")
    prompt="\n".join(chat_history) + "\nAI:"
    response=model.generate_content(prompt)
    chat_history.append(f"AI : {response.text}")
    print(f"AI: {response.text}")
    if q.lower()== "exit":
        break

print(chat_history)

