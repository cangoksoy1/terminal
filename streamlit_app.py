import streamlit as st

# CSS to style the page for a professional look
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .logo {
        text-align: center;
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        color: #d92229;
        margin-bottom: 1em;
    }
    .project-card {
        background-color: white;
        padding: 1.5em;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1.5em;
    }
    .project-title {
        font-size: 1.2em;
        font-weight: bold;
        color: #333;
    }
    .project-summary {
        font-size: 0.9em;
        color: #666;
        margin-bottom: 0.5em;
    }
    .category-badge {
        background-color: #d92229;
        color: white;
        padding: 0.5em 1em;
        border-radius: 12px;
        font-size: 0.9em;
        float: right;
    }
    .submit-button {
        background-color: #d92229;
        color: white;
        padding: 0.8em 1.5em;
        border-radius: 25px;
        border: none;
        font-size: 1.1em;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .submit-button:hover {
        background-color: #a5181f;
    }
    </style>
""", unsafe_allow_html=True)

# Logo and title
st.image("Turkish-Airlines-symbol.png", width=100, use_column_width=False)
st.markdown("<div class='title'>Turkish Airlines Innovation Terminal</div>", unsafe_allow_html=True)

# Category selection
category = st.selectbox("Select Category", ["All", "Flight Operations", "Ground Operations", "Sustainability", "In-Flight Entertainment"])

# Sample project submissions (with cards)
projects = [
    {"name": "AI-Driven Flight Scheduling Optimization", "date": "2024-09-01", "summary": "Using AI to optimize flight schedules based on real-time data and passenger demand.", "category": "Flight Operations"},
    {"name": "Sustainable Aviation Fuel Initiative", "date": "2024-08-25", "summary": "Exploring sustainable fuel options for reducing carbon emissions.", "category": "Sustainability"}
]

# Display the projects with the enhanced layout
for project in projects:
    if category == "All" or category == project["category"]:
        st.markdown(f"""
            <div class='project-card'>
                <div class='project-title'>{project['name']}</div>
                <div class='category-badge'>{project['category']}</div>
                <div class='project-summary'><strong>Date:</strong> {project['date']}</div>
                <div class='project-summary'><strong>Summary:</strong> {project['summary']}</div>
            </div>
        """, unsafe_allow_html=True)

# Auto-Prioritize Button
if st.button("Auto-Prioritize", key="auto_prioritize"):
    st.write("Submissions have been prioritized based on relevance.")
