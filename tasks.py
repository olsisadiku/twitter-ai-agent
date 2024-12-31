from crewai import Task

def create_tasks(trend_researcher, niche):
    trend_analysis_task = Task(
        description=f"""Analyze current trending topics on X (Twitter) in the {niche} niche.
        
        For each topic you identify:
        1. Explain why it's trending THIS week specifically
        2. Include example viral tweets about this topic
        3. Analyze what made these tweets successful
        
        Format your response exactly as follows:
        
        [NEW_TRENDS]
        • Topic 1: (name)
          Why New: (explanation why it's new this week)
          Viral Tweet 1: (tweet text)
          - URL: (link to tweet)
          - Engagement: (approximate likes/retweets)
          - Why Viral: (analysis)
          Viral Tweet 2: (tweet text)
          - URL: (link to tweet)
          - Engagement: (approximate likes/retweets)
          - Why Viral: (analysis)
        
        (Continue for each trending topic)""",
        expected_output="""A structured analysis of new trending topics with viral tweets, their URLs, and engagement metrics.""",
        agent=trend_researcher
    )

    return [trend_analysis_task] 