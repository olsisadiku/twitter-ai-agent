import streamlit as st
from main import analyze_viral_content

st.title("🦜 Twitter Viral Content Analyzer")

if st.button("Analyze Viral Tweets"):
    with st.spinner("Analyzing viral tweets..."):
        results = analyze_viral_content()
        
        # Display results in a nice format
        sections = results.split("[")
        
        for section in sections:
            if "VIRAL_TWEETS]" in section:
                st.header("📊 Viral Tweets")
                st.write(section.replace("VIRAL_TWEETS]", ""))
            elif "PATTERNS]" in section:
                st.header("🔍 Patterns")
                st.write(section.replace("PATTERNS]", ""))
            elif "INSIGHTS]" in section:
                st.header("💡 Insights")
                st.write(section.replace("INSIGHTS]", "")) 