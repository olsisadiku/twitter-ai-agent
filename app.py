import streamlit as st
from main import run_twitter_analysis
import json

# Set page config
st.set_page_config(
    page_title="X Trend Analyzer & Content Generator",
    page_icon="🐦",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .results-container {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🐦 X Trend Analyzer & Content Generator")
st.markdown("---")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    niche = st.text_input("Your Niche", value="AI and Technology")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This tool helps you:
    - Analyze trending topics on X
    - Get content suggestions
    - Generate tweet ideas
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Trend Analysis & Content Generation")
    st.markdown("Get trending topics and content suggestions for your niche.")
    
    if st.button("Generate Content Ideas", type="primary"):
        with st.spinner('Analyzing trends and generating content...'):
            try:
                # Create placeholder containers
                trend_container = st.empty()
                strategy_container = st.empty()
                tweets_container = st.empty()
                
                # Run analysis
                result = run_twitter_analysis(niche)
                
                # Parse and display results in a structured way
                st.success("Analysis Complete!")
                
                # Display results in tabs
                tab1, tab2, tab3 = st.tabs(["📊 Trend Analysis", "📈 Strategy", "✍️ Tweet Suggestions"])
                
                with tab1:
                    st.markdown("### Today's Trending Topics")
                    st.markdown(result.split("Strategy")[0] if "Strategy" in result else "No trends found")
                
                with tab2:
                    st.markdown("### Content Strategy")
                    strategy_section = result.split("Strategy")[1].split("Tweet Suggestions")[0] if "Strategy" in result and "Tweet Suggestions" in result else "No strategy generated"
                    st.markdown(strategy_section)
                
                with tab3:
                    st.markdown("### Tweet Suggestions")
                    tweets_section = result.split("Tweet Suggestions")[1] if "Tweet Suggestions" in result else "No tweets generated"
                    
                    # Parse and display tweets in cards
                    tweets = tweets_section.split("\n")
                    for tweet in tweets:
                        if tweet.strip():
                            st.markdown(f"""
                            <div style='background-color: white; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border: 1px solid #ddd;'>
                                {tweet}
                            </div>
                            """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

with col2:
    st.header("Quick Stats")
    
    # Metrics placeholder (you can replace these with real metrics from your analysis)
    st.metric(label="Trending Topics Found", value="5")
    st.metric(label="Suggested Tweets", value="5")
    
    # Tips box
    st.markdown("### Tips for Better Results")
    st.info("""
    - Be specific with your niche
    - Try different variations
    - Best to run during peak hours
    - Save your favorite suggestions
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Your AI Agent") 