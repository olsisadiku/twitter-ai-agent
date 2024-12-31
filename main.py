from langchain_openai import ChatOpenAI
from crewai import Crew
from config import DEFAULT_LLM_MODEL, DEFAULT_TEMPERATURE
from agents import create_agents
from tasks import create_tasks

def analyze_trends(niche):
    # Initialize LLM
    llm = ChatOpenAI(
        model_name=DEFAULT_LLM_MODEL,
        temperature=DEFAULT_TEMPERATURE
    )
    
    # Create agent (just trend researcher)
    trend_researcher = create_agents(llm)
    
    # Create tasks
    tasks = create_tasks(trend_researcher, niche)
    
    # Create crew
    crew = Crew(
        agents=[trend_researcher],
        tasks=tasks,
        verbose=True
    )
    
    # Run the analysis and get result
    result = crew.kickoff()
    return str(result)

if __name__ == "__main__":
    niche = "AI and Technology"
    result = analyze_trends(niche)
    print("\n=== Results ===")
    print(result)
