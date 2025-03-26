import streamlit as st
from pathlib import Path

# ✅ Set page configuration FIRST
st.set_page_config(page_title="Cricket Template Analysis", layout="wide")

st.markdown("""
    <style>
        /* Hide the built-in Streamlit sidebar menu */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        /* Hide extra elements inside the sidebar while keeping custom navigation */
        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child:not(:has(button)) {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Load CSS after setting page config
with open(r"styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"  # Default page
if "selected_player" not in st.session_state:
    st.session_state.selected_player = None  # Store player selection

# ✅ Sidebar Navigation
st.sidebar.button("### ---- Navigation Options below ----")


if st.sidebar.button("🔍 Deep Dive into Trigger Movements"):
    st.session_state.page = "Trigger"
if st.sidebar.button("🏏 VK's Outside Off Stump Issues"):
    st.session_state.page = "vk_issues"
if st.sidebar.button("🔥 JR's Recent Purple Patch"):
    st.session_state.page = "jr_purple_patch"
if st.sidebar.button("📊 View Test Stats"):
    st.session_state.page = "test_stats"
if st.sidebar.button("📤 Upload & Analyze Image"):
    st.session_state.page = "upload"
if st.sidebar.button("ℹ️ About This Project"):
    st.session_state.page = "about"

# ✅ Handle Navigation Dynamically

if st.session_state.page == "Trigger":
    from pages.trigger_info import trigger_explain
    trigger_explain()
    
if st.session_state.page == "vk_issues":
    from pages.vk_offstump import show_vk_off_stump
    show_vk_off_stump()

elif st.session_state.page == "jr_purple_patch":
    from pages.jr_purple_patch import show_jr_purple_patch
    show_jr_purple_patch()

elif st.session_state.page == "test_stats":
    from pages.test_stats import show_test_stats
    show_test_stats()

elif st.session_state.page == "upload":
    if st.session_state.selected_player == "VK":
        from pages.vk_input import show_vk_input
        show_vk_input()
    elif st.session_state.selected_player == "JR":
        from pages.jr_input import show_jr_input
        show_jr_input()
    else:
        st.warning("⚠️ Please select a player from the home page first!")
        if st.button("🔙 Back to Home"):
            st.session_state.page = "home"
            st.rerun()

elif st.session_state.page == "result":
    from pages.result import show_result  # ✅ Correct Placement of Result Page
    show_result()

elif st.session_state.page == "about":
    from pages.about import show_about
    show_about()

elif st.session_state.page == "home":
    # ✅ Render Home Page
    st.markdown("<h1>🏏 Cricket Template Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p>Compare shots with Prime vs Non-Prime Techniques</p>", unsafe_allow_html=True)

    # Player Selection
    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/VK.jpg", caption="Virat Kohli", use_container_width=True)
        if st.button("Select Virat Kohli"):
            st.session_state.selected_player = "VK"
            st.session_state.page = "upload"  # Redirect to upload section
            st.rerun()

    with col2:
        st.image("assets/JR.jpg", caption="Joe Root", use_container_width=True)
        if st.button("Select Joe Root"):
            st.session_state.selected_player = "JR"
            st.session_state.page = "upload"  # Redirect to upload section
            st.rerun()

    # Display selected player
    if st.session_state.selected_player:
        st.success(f"✅ Selected Player: {st.session_state.selected_player}")
