from crewai import Agent
from langchain.tools import Tool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_viral_tweets(query=None):
    """Scrape viral tweets from Twitter's explore page"""
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    # Initialize the Chrome WebDriver with proper service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Go to Twitter's trending page
        driver.get('https://twitter.com/explore/tabs/trending')
        time.sleep(10)  # Give more time to load
        
        # Scroll a bit to load more content
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        
        # Find tweets
        tweets_data = []
        articles = driver.find_elements(By.CSS_SELECTOR, 'article[data-testid="tweet"]')
        
        for article in articles[:5]:
            try:
                # Get tweet text
                tweet_text_element = article.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
                tweet_text = tweet_text_element.text if tweet_text_element else "No text available"
                
                # Get username
                username_element = article.find_element(By.CSS_SELECTOR, 'div[data-testid="User-Name"]')
                username = username_element.text if username_element else "Unknown user"
                
                # Get tweet link
                link_element = article.find_element(By.CSS_SELECTOR, 'a[href*="/status/"]')
                link = link_element.get_attribute('href') if link_element else "No link available"
                
                tweets_data.append({
                    "text": tweet_text,
                    "username": username,
                    "link": link
                })
                
            except Exception as e:
                continue
        
        if not tweets_data:
            return "No tweets found. Please try again."
            
        # Format output
        output = "[VIRAL_TWEETS]\n"
        for tweet in tweets_data:
            output += f"""
            Tweet: {tweet['text']}
            By: {tweet['username']}
            Link: {tweet['link']}
            ---
            """
        
        return output
        
    except Exception as e:
        return f"Error occurred while scraping: {str(e)}"
        
    finally:
        driver.quit()

def create_agents(llm):
    scrape_tool = Tool(
        name="scrape_viral_tweets",
        description="Scrape Twitter to find currently viral tweets and analyze why they're trending",
        func=scrape_viral_tweets
    )
    
    twitter_analyst = Agent(
        role='Viral Content Analyst',
        goal='Analyze why certain tweets go viral and identify patterns in viral content',
        backstory="""You are an expert in viral content analysis. You understand what makes 
        content spread on social media and can identify key elements that contribute to virality. 
        Your analysis helps others understand the mechanics of viral content.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[scrape_tool]
    )
    
    return twitter_analyst 