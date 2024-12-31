from crewai import Agent

def create_agents(llm):
    trend_researcher = Agent(
        role='Trend Researcher',
        goal='Find and analyze new trending topics and viral tweets on X',
        backstory="""You are an expert social media analyst who specializes in 
        identifying trending topics and viral content on X. You focus on finding 
        topics that are NEW this week and weren't trending last week. You also 
        analyze what makes certain tweets go viral. You have deep knowledge of 
        current events and social media trends.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    return trend_researcher 