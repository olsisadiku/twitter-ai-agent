from crewai import Agent
from langchain_openai import ChatOpenAI
from config import DEFAULT_LLM_MODEL, DEFAULT_TEMPERATURE

def create_agents(llm):
    trend_analyzer = Agent(
        role='Trend Analyzer',
        goal='Analyze X (Twitter) for trending topics and their engagement metrics',
        backstory="""You are an expert social media analyst with deep understanding 
        of viral content and trending patterns on X. You excel at identifying emerging 
        trends and understanding why certain content performs well.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    content_strategist = Agent(
        role='Content Strategist',
        goal='Analyze trends and create tailored content suggestions',
        backstory="""You are a skilled content strategist who understands how to 
        adapt trending topics to specific niches while maintaining authenticity. 
        You excel at crafting engaging tweets that resonate with target audiences.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    content_creator = Agent(
        role='Content Creator',
        goal='Create unique and engaging tweet suggestions',
        backstory="""You are a creative content creator who knows how to write 
        viral tweets. You understand the perfect balance between trending topics 
        and unique perspectives, and know how to use X's features effectively.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    return trend_analyzer, content_strategist, content_creator 