import streamlit as st

# Event Data
events = [
    {"date": "Feb 10, 2025", "name": "Hackathon", "description": "A 24-hour coding competition."},
    {"date": "Feb 15, 2025", "name": "Tech Talk", "description": "A session on AI advancements."},
    {"date": "Feb 20, 2025", "name": "Workshop", "description": "Hands-on cybersecurity workshop."}
]

# Page Title
st.title("ACM Calendar of Events")

# Display Events
for event in events:
    with st.container():
        st.markdown(f"**📅 {event['date']}**")
        st.markdown(f"### {event['name']}")
        st.markdown(f"{event['description']}")
        st.markdown("---")
