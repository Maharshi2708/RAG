from langchain_community.chat_models import ChatOllama

def llm():
    return ChatOllama(model="phi3")

def generate_answer(prompt, query):
    llm_instance = llm()
    response = llm_instance.invoke(prompt + f"\n\nQuestion: {query}\nAnswer:")
    return response.content.strip()