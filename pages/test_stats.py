import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to get player stats from Cricbuzz
def get_player_stats(player_url):
    response = requests.get(player_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stats = {}

    try:
        # Locate the batting career summary table
        table = soup.find('table', class_='table cb-col-100 cb-plyr-thead')  # Update class name if required
        row = table.find('tbody').find_all('tr')[0]  # First row for Test stats
        cols = row.find_all('td')

        stats = {
            "Matches": cols[1].text.strip(),
            "Innings": cols[2].text.strip(),
            "Runs": cols[3].text.strip(),
            "Average": cols[6].text.strip(),
            "Strike Rate": cols[7].text.strip()
        }
    except AttributeError:
        return None

    return stats

# URLs for Virat Kohli and Joe Root
virat_url = "https://www.cricbuzz.com/profiles/1413/virat-kohli"
joe_url = "https://www.cricbuzz.com/profiles/8019/joe-root"

# Fetch stats
virat_stats = get_player_stats(virat_url)
joe_stats = get_player_stats(joe_url)

def show_test_stats():
    st.title("🏏 Test Career Stats")

    if not virat_stats or not joe_stats:
        st.error("Failed to fetch stats. Please try again later.")
        return

    st.subheader("Player Comparison")

    # Add images above the table
    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/VK.jpg", caption="Virat Kohli", use_container_width=True)

    with col2:
        st.image("assets/JR.jpg", caption="Joe Root", use_container_width=True)

    # Create a table-friendly structure
    data = {
        "Stat": ["Matches", "Innings", "Runs", "Average", "Strike Rate"],
        "Virat Kohli": [
            virat_stats["Matches"],
            virat_stats["Innings"],
            virat_stats["Runs"],
            virat_stats["Average"],
            virat_stats["Strike Rate"]
        ],
        "Joe Root": [
            joe_stats["Matches"],
            joe_stats["Innings"],
            joe_stats["Runs"],
            joe_stats["Average"],
            joe_stats["Strike Rate"]
        ]
    }

    # Display as a table
    st.table(data)

    # ✅ Back Button
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
