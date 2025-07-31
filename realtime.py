import google.generativeai as genai
from serpapi import GoogleSearch

genai.configure(api_key="AIzaSyDNus3YOkIgSkW8VmLA5E8BiV2B71Dgklw")

model=genai.GenerativeModel('gemini-2.0-flash')

serpapi_key="5256664fe5fe6ba4fc5ed27518ac1ad4e1602608f4d6071043fca6ad57ded062"

def google_search(query):
    param={
        "q":query,
        "h1": "en",
        "gl": "us",
        "api_key": serpapi_key
    }
    
    search=GoogleSearch(param)
    result= search.get_dict()
    
    if "organic_results" in result:
        return "\n".join([res["snippet"] for res in result["organic_results"][:5]])
    return "No result found"

def chat_with_gemini(query):
    search_result= google_search(query)
    
    prompt=f""" I search google for "{query}" and  found the following information:
    {search_result}
    
    based on this, please give me a concise and to the point answer. """
    
    response= model.generate_content(prompt)
    return response.text

user=input("prompt: ")
print(chat_with_gemini(user))
        