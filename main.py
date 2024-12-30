from langchain_openai import ChatOpenAI
from crewai import Crew
from config import OPENAI_API_KEY, DEFAULT_LLM_MODEL, DEFAULT_TEMPERATURE
from agents import create_agents
from tasks import create_tasks

def run_twitter_analysis(niche):
    # Initialize the LLM
    llm = ChatOpenAI(
        model_name=DEFAULT_LLM_MODEL,
        temperature=DEFAULT_TEMPERATURE
    )
    
    # Create agents
    trend_analyzer, content_strategist, content_creator = create_agents(llm)
    
    # Create tasks
    tasks = create_tasks(trend_analyzer, content_strategist, content_creator, niche)
    
    # Create and run crew
    crew = Crew(
        agents=[trend_analyzer, content_strategist, content_creator],
        tasks=tasks,
        verbose=2
    )
    
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    # This will only run when main.py is run directly
    USER_NICHE = "AI and Technology"
    print("Starting X (Twitter) trend analysis and content generation...")
    result = run_twitter_analysis(USER_NICHE)
    print("\n=== Results ===")
    print(result)
