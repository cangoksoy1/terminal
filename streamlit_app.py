import streamlit as st

# Title and Logo
st.markdown("<h1 style='text-align: center; color: black;'>Terminal</h1>", unsafe_allow_html=True)
st.image("Turkish-Airlines-symbol.png", width=100, use_column_width=False)

# Simulated GPT summaries for project ideas with categories
projects = [
    {"topic": "AI-Driven Flight Scheduling Optimization", "date": "2024-09-01", "summary": "Using AI to optimize flight schedules based on real-time data and passenger demand.", "category": "Flight Operations"},
    {"topic": "Sustainable Aviation Fuel Initiative", "date": "2024-08-25", "summary": "Project to explore sustainable fuel options for reducing carbon emissions in aviation.", "category": "Sustainability"},
]

# Create a dropdown to filter projects by category
categories = ["All", "In-Flight Entertainment", "Ground Operations", "Flight Operations", "Sustainability", 
              "Engineering & Maintenance", "Customer Service", "Logistics", "Revenue Management"]
selected_category = st.selectbox("Select Category", categories)

# Filter projects based on the selected category
if selected_category == "All":
    filtered_projects = projects
else:
    filtered_projects = [project for project in projects if project["category"] == selected_category]

# Layout for filtered project ideas
st.markdown("<h2 style='text-align: left; color: black;'>Project Submissions</h2>", unsafe_allow_html=True)

# Display the filtered projects
for project in filtered_projects:
    st.markdown(f"<div style='border:1px solid black; padding:10px; margin:5px;'>"
                f"<strong>Topic:</strong> {project['topic']}<br>"
                f"<strong>Date:</strong> {project['date']}<br>"
                f"<strong>Summary:</strong> {project['summary']}<br>"
                f"<strong>Category:</strong> {project['category']}</div>", unsafe_allow_html=True)

# Auto-prioritize button
if st.button("Auto-Prioritize"):
    st.write("Prioritization in progress...")

