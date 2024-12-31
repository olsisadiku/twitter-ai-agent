from langchain_openai import ChatOpenAI
from crewai import Crew
from agents import create_agents
from tasks import create_tasks
from config import DEFAULT_LLM_MODEL, DEFAULT_TEMPERATURE

def analyze_viral_content():
    llm = ChatOpenAI(
        model_name=DEFAULT_LLM_MODEL,
        temperature=DEFAULT_TEMPERATURE
    )
    
    analyst = create_agents(llm)
    tasks = create_tasks(analyst)
    
    crew = Crew(
        agents=[analyst],
        tasks=tasks,
        verbose=True
    )
    
    result = crew.kickoff()
    return str(result)

if __name__ == "__main__":
    result = analyze_viral_content()
    print("\n=== Analysis Results ===")
    print(result)
