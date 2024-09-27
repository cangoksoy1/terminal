import streamlit as st

st.markdown("""
    <style>
    .main {
        background: linear-gradient(180deg, #f0f4f7, #e5e7ea);
        font-family: 'Arial', sans-serif;
    }
    .sidebar {
        background-color: #d92229;
        padding: 1em;
        color: white;
        position: fixed;
        height: 100%;
        width: 250px;
        left: 0;
        top: 0;
    }
    .sidebar h2 {
        color: white;
        font-size: 1.5em;
    }
    .sidebar a {
        color: white;
        padding: 0.5em;
        text-decoration: none;
        display: block;
        margin-bottom: 1em;
    }
    .header {
        padding: 20px;
        font-size: 1.6em;
        font-weight: bold;
        color: #d92229;
    }
    .dashboard {
        margin-left: 270px;
        padding: 20px;
    }
    .card {
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 15px;
        margin-bottom: 20px;
        width: 100%;
    }
    .card h3 {
        font-size: 1.3em;
        color: #333;
    }
    .card p {
        font-size: 0.9em;
        color: #777;
    }
    .auto-prioritize {
        background-color: #d92229;
        color: white;
        padding: 10px 20px;
        font-size: 1.1em;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .auto-prioritize:hover {
        background-color: #a5181f;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.markdown("""
    <div class='sidebar'>
        <h2>Categories</h2>
        <a href='#'>Flight Operations</a>
        <a href='#'>Ground Operations</a>
        <a href='#'>Sustainability</a>
        <a href='#'>In-Flight Entertainment</a>
    </div>
""", unsafe_allow_html=True)

# Header
st.image("terminal.png", width=300, use_column_width=False)

# Dashboard content
st.markdown("<div class='dashboard'>", unsafe_allow_html=True)

# Displaying project submissions in card style
projects = [
    {"name": "AI-Driven Flight Scheduling Optimization", "date": "2024-09-01", "summary": "Using AI to optimize flight schedules based on real-time data and passenger demand.", "category": "Flight Operations"},
    {"name": "Sustainable Aviation Fuel Initiative", "date": "2024-08-25", "summary": "Exploring sustainable fuel options for reducing carbon emissions.", "category": "Sustainability"}
]

# Displaying projects in cards with the new layout
for project in projects:
    st.markdown(f"""
        <div class='card'>
            <h3>{project['name']}</h3>
            <p><strong>Date:</strong> {project['date']}</p>
            <p><strong>Summary:</strong> {project['summary']}</p>
        </div>
    """, unsafe_allow_html=True)

# Auto-Prioritize Button
if st.button("Auto-Prioritize", key="auto_prioritize", help="Prioritize submissions based on relevance"):
    st.write("Submissions have been prioritized.")

st.markdown("</div>", unsafe_allow_html=True)
