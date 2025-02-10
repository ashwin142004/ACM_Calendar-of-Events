import streamlit as st

# Event Data
events = [
    {"date": "Feb 19, 2025", "name": "Orientation", "description": "Introduction to ACM and upcoming activities."},
    {"date": "Feb 22, 2025", "name": "Tech Treasure Hunt", "description": "A fun-filled hunt for tech enthusiasts."},
    {"date": "Mar 5, 2025", "name": "Website Design Competition", "description": "Showcase your web design skills and creativity."},
    {"date": "Mar 18, 2025", "name": "Platform Intro (Cloud and AWS)", "description": "Learn about cloud computing and AWS essentials."},
    {"date": "Mar 30, 2025", "name": "Bug Bounty Hunt", "description": "Test your sherlock skills in a live challenge."}
]

# Page Layout
st.set_page_config(page_title="ACM Calendar", page_icon="📅", layout="wide")

# Logo and Title
col1, col2 = st.columns([1, 4])
with col1:
    st.image("logo.png", width=100)
with col2:
    st.title("ACM Calendar of Events")

st.markdown("---")

# Display Events
for event in events:
    with st.container():
        st.markdown(f"**📅 {event['date']}**")
        st.markdown(f"### {event['name']}")
        st.markdown(f"{event['description']}")
        st.markdown("---")
