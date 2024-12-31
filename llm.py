from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, DEFAULT_LLM_MODEL, DEFAULT_TEMPERATURE

def init_llm():
    """Initialize and return OpenAI LLM"""
    llm = ChatOpenAI(
        model_name=DEFAULT_LLM_MODEL,
        temperature=DEFAULT_TEMPERATURE
    )
    
    return llm 