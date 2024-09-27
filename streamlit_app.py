import streamlit as st

# Title and Logo
st.markdown("<h1 style='text-align: center; color: black;'>Terminal</h1>", unsafe_allow_html=True)
st.image("Turkish-Airlines-symbol.png", width=100, use_column_width=False)

# Simulated GPT summaries for project ideas
projects = [
    {"topic": "AI-Driven Flight Scheduling Optimization", "date": "2024-09-01", "summary": "Using AI to optimize flight schedules based on real-time data and passenger demand."},
    {"topic": "Sustainable Aviation Fuel Initiative", "date": "2024-08-25", "summary": "Project to explore sustainable fuel options for reducing carbon emissions in aviation."},
    {"topic": "Predictive Maintenance System for Engines", "date": "2024-09-05", "summary": "Implementing AI-driven predictive models to detect engine maintenance needs before failure."},
    {"topic": "In-Flight Entertainment Personalization", "date": "2024-08-30", "summary": "Personalizing in-flight entertainment for passengers based on viewing preferences and AI recommendations."},
    {"topic": "Real-time Baggage Tracking System", "date": "2024-09-10", "summary": "A real-time tracking solution to monitor and update passengers about their baggage location."},
    {"topic": "Green Energy Solutions for Ground Operations", "date": "2024-09-02", "summary": "Introducing green energy systems to power airport ground operations and reduce environmental footprint."},
    {"topic": "AI-Based Customer Service Chatbot", "date": "2024-09-03", "summary": "Deploying a chatbot powered by AI to enhance customer service and reduce wait times."},
    {"topic": "Smart Cargo Space Utilization", "date": "2024-08-20", "summary": "Using AI and IoT to optimize cargo space and improve logistics efficiency."},
    {"topic": "Passenger Flow Optimization at Airports", "date": "2024-08-15", "summary": "Improving passenger flow through airports using AI to reduce congestion and enhance security."},
    {"topic": "Dynamic Pricing for Last-Minute Tickets", "date": "2024-09-08", "summary": "AI-driven dynamic pricing models to adjust prices for last-minute flight tickets based on demand."}
]

# Layout for project ideas
st.markdown("<h2 style='text-align: left; color: black;'>Project Submissions</h2>", unsafe_allow_html=True)

# Display the projects
for project in projects:
    st.markdown(f"<div style='border:1px solid black; padding:10px; margin:5px;'>"
                f"<strong>Topic:</strong> {project['topic']}<br>"
                f"<strong>Date:</strong> {project['date']}<br>"
                f"<strong>Summary:</strong> {project['summary']}</div>", unsafe_allow_html=True)

# Auto-prioritize button
if st.button("Auto-Prioritize"):
    st.write("Prioritization in progress...")


