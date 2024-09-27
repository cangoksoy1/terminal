import streamlit as st

# Set page layout and configuration
st.set_page_config(layout="wide")

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Page styling */
    body {
        background-color: #f0f2f6;
        font-family: "Courier New", monospace;
    }
    .stApp {
        background-color: #f0f2f6;
        padding: 20px;
    }
    /* Terminal box */
    .terminal-box {
        background-color: #2d2d2d;
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-size: 16px;
        width: 100%;
        margin: auto;
    }
    /* Submission section styling */
    .submission-card {
        background-color: #333333;
        color: white;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    /* Header and title styling */
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
    }
    /* Auto-prioritize button styling */
    .stButton>button {
        background-color: #0066cc;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the header with the logo and title
col1, col2 = st.columns([4, 1])  # Column layout, col2 for logo

with col1:
    st.markdown('<div class="header">Terminal</div>', unsafe_allow_html=True)

with col2:
    st.image("Turkish-Airlines-symbol.png", width=100)  # Adjust the size here

st.markdown("---")  # Add a separator

# Simulated list of project submissions (employees only see the topics)
submissions = [
    {"employee": "Ahmet Yilmaz", "title": "AI-Driven Flight Scheduling Optimization", "date": "2024-09-01"},
    {"employee": "Elif Demir", "title": "Sustainable Aviation Fuel Initiative", "date": "2024-08-25"},
    {"employee": "Murat Kaya", "title": "Predictive Maintenance System for Engines", "date": "2024-09-05"},
    {"employee": "Canan Tekin", "title": "In-Flight Entertainment Personalization", "date": "2024-08-30"},
    {"employee": "Zeynep Oz", "title": "Real-time Baggage Tracking System", "date": "2024-09-10"},
    {"employee": "Emre Aydin", "title": "Green Energy Solutions for Ground Operations", "date": "2024-09-02"},
    {"employee": "Yasemin Korkmaz", "title": "AI-Based Customer Service Chatbot", "date": "2024-09-03"},
    {"employee": "Ali Vural", "title": "Smart Cargo Space Utilization", "date": "2024-08-20"},
    {"employee": "Deniz Karaman", "title": "Passenger Flow Optimization at Airports", "date": "2024-08-15"},
    {"employee": "Mehmet Can", "title": "Dynamic Pricing for Last-Minute Tickets", "date": "2024-09-08"},
]

# Streamlit UX for submission display
st.markdown('<div class="terminal-box">', unsafe_allow_html=True)

st.subheader("Innovation Project Submissions")

# Displaying only topics (employees can click to reveal more)
for submission in submissions:
    if st.checkbox(f"{submission['title']} - {submission['date']}"):
        st.markdown('<div class="submission-card">', unsafe_allow_html=True)
        st.write(f"Submitted by: {submission['employee']}")
        st.write(f"Project Title: {submission['title']}")
        st.write(f"Date: {submission['date']}")
        st.write(f"Description: (Submission details will go here)")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Button for auto-prioritizing submissions
if st.button("Auto-Prioritize"):
    st.write("Prioritized Submissions (Medium and High Priority Only):")
    for submission in submissions[:7]:  # Simulate prioritizing the top 7 submissions
        st.write(f"{submission['title']} - {submission['date']} (High/Medium Priority)")


