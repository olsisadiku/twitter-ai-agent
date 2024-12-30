from crewai import Task

def create_tasks(trend_analyzer, content_strategist, content_creator, niche):
    trend_analysis_task = Task(
        description=f"""Analyze X (Twitter) to identify today's top trending topics. 
        Focus on:
        1. Overall trending topics
        2. Trending topics within the {niche} niche
        3. Posts with highest engagement
        4. Key hashtags and their performance
        
        Provide a structured analysis of findings.""",
        agent=trend_analyzer
    )

    strategy_task = Task(
        description=f"""Based on the trend analysis, develop a content strategy for the {niche} niche:
        1. Identify which trends align with the niche
        2. Analyze why these trends would resonate with the target audience
        3. Suggest optimal posting times
        4. Recommend relevant hashtags
        
        Create a strategic brief for content creation.""",
        agent=content_strategist
    )

    content_creation_task = Task(
        description=f"""Using the trend analysis and strategy, create:
        1. 5 unique tweet suggestions
        2. Each tweet should be optimized for engagement
        3. Include relevant hashtags
        4. Suggest any media types to include (images, videos, polls)
        
        Ensure tweets are authentic and aligned with {niche} niche voice.""",
        agent=content_creator
    )

    return [trend_analysis_task, strategy_task, content_creation_task] 