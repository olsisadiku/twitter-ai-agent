import streamlit as st
from main import analyze_trends
from datetime import datetime

# Page config
st.set_page_config(page_title="X Trend Analyzer", page_icon="🐦", layout="wide")

# Custom styling for dark theme
st.markdown("""
    <style>
    /* Dark theme styles */
    .stApp {
        background-color: #0E1117;
        color: #E7E9EA;
    }
    
    .topic-header {
        font-size: 20px;
        font-weight: bold;
        color: #1DA1F2;
        margin: 20px 0 10px 0;
    }
    .viral-tweet {
        background-color: #15202B;
        color: #E7E9EA;
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        border: 1px solid #333;
        position: relative;
    }
    .tweet-link {
        position: absolute;
        top: 10px;
        right: 10px;
        color: #1DA1F2;
        text-decoration: none;
        padding: 5px 10px;
        border-radius: 15px;
        border: 1px solid #1DA1F2;
        font-size: 12px;
    }
    .tweet-link:hover {
        background-color: rgba(29, 161, 242, 0.1);
    }
    .engagement-stats {
        color: #1DA1F2;
        font-size: 14px;
        margin: 5px 0;
    }
    .analysis-text {
        color: #E7E9EA;
        margin: 10px 0;
        background-color: rgba(29, 161, 242, 0.1);
        padding: 10px;
        border-radius: 8px;
    }
    .stMarkdown {
        color: #E7E9EA !important;
    }
    .main-text {
        color: #E7E9EA;
    }
    strong {
        color: #1DA1F2;
    }
    
    /* Override Streamlit's default styles */
    .stButton button {
        background-color: #1DA1F2;
        color: white;
    }
    .stButton button:hover {
        background-color: #1991DA;
        color: white;
    }
    .streamlit-expanderHeader {
        color: #E7E9EA;
        background-color: #15202B;
    }
    .streamlit-expanderContent {
        background-color: #15202B;
        color: #E7E9EA;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🐦 X Trend Analyzer")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    niche = st.text_input("Your Niche", value="AI and Technology")
    st.markdown("---")
    st.markdown("""
    <div class="main-text">
    <h3>About</h3>
    This tool helps you:
    <ul>
        <li>Find new trending topics</li>
        <li>Analyze viral tweets</li>
        <li>Understand engagement patterns</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Main content
if st.button("Analyze New Trends", type="primary"):
    with st.spinner("Analyzing trending topics and viral tweets..."):
        try:
            results = analyze_trends(niche)
            if results:
                results_str = str(results)
                
                if "[NEW_TRENDS]" in results_str:
                    trends_text = results_str.split("[NEW_TRENDS]")[1]
                    topics = [t.strip() for t in trends_text.split("•") if t.strip()]
                    
                    for topic in topics:
                        if topic:
                            # Split topic into components
                            parts = topic.split("Viral Tweet")
                            topic_info = parts[0].strip()
                            
                            # Display topic header and info
                            st.markdown(f"""
                            <div class="topic-header">{topic_info.split('Why New:')[0]}</div>
                            <div class="analysis-text">
                                <strong>Why Trending:</strong> {topic_info.split('Why New:')[1].strip()}
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Display viral tweets
                            for i, tweet in enumerate(parts[1:], 1):
                                tweet_parts = tweet.split("-")
                                tweet_text = tweet_parts[0].strip()
                                
                                # Get URL from the tweet parts
                                url_line = next((p for p in tweet_parts if "URL:" in p), None)
                                tweet_url = url_line.split("URL:")[1].strip() if url_line else "#"
                                
                                engagement = next((p for p in tweet_parts if "Engagement:" in p), "").strip()
                                analysis = next((p for p in tweet_parts if "Why Viral:" in p), "").strip()
                                
                                st.markdown(f"""
                                <div class="viral-tweet">
                                    <a href="{tweet_url}" target="_blank" class="tweet-link">View on X</a>
                                    {tweet_text}
                                    <div class="engagement-stats">{engagement.replace('Engagement:', '')}</div>
                                    <div class="analysis-text"><strong>Why Viral:</strong> {analysis.replace('Why Viral:', '')}</div>
                                </div>
                                """, unsafe_allow_html=True)
                else:
                    st.warning("No trending topics found in the analysis.")
                
                # Add debug expander
                with st.expander("Debug Output"):
                    st.text(results_str)
            else:
                st.error("No results were returned from the analysis.")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            if 'results_str' in locals():
                st.text("Raw output for debugging:")
                st.text(results_str)

# Footer
st.markdown("---")
st.markdown('<p style="color: #E7E9EA;">Made with ❤️ by Your AI Agent</p>', unsafe_allow_html=True) 