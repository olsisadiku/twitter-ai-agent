from crewai import Task

def create_tasks(analyst):
    viral_analysis = Task(
        description="""Analyze viral tweets to understand what makes them successful.
        
        1. Find currently viral tweets
        2. Analyze their content, style, and engagement
        3. Identify common patterns and elements that contribute to virality
        4. Provide insights on why these specific tweets went viral
        
        Format your response with clear sections:
        [VIRAL_TWEETS]
        • Tweet content
        • Engagement metrics
        • Link to tweet
        • Analysis of why it went viral
        
        [PATTERNS]
        • Common elements across viral tweets
        • Key factors contributing to virality
        • Notable trends
        
        [INSIGHTS]
        • Overall analysis
        • Recommendations for creating viral content""",
        expected_output="""A structured analysis containing:
        1. List of viral tweets with their content, metrics, and links
        2. Analysis of common patterns across viral tweets
        3. Insights and recommendations for viral content creation""",
        agent=analyst
    )
    
    return [viral_analysis] 