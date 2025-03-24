import streamlit as st

# ✅ Must be the first command


def show_about():
    # 🔹 Custom Styles for a sleek UI
    st.markdown(
        """
        <style>
            /* Background */
            .stApp { background-color: #101820; }

            /* Title Styling */
            h1 { color: #ffcc00; text-align: center; font-size: 3rem; font-weight: bold; }
            
            /* Section Headers */
            h2, h3 { color: #00d4ff; margin-top: 1.5rem; font-weight: bold; }

            /* Text */
            p, li { color: #e0e0e0; font-size: 1.1rem; line-height: 1.6; }

            /* Divider */
            hr { border: 1px solid #ffcc00; margin: 20px 0; }

            /* Buttons */
            .stButton>button {
                background-color: #333845; color: #e0e0e0;
                border-radius: 10px; border: 1px solid #555;
                transition: all 0.3s;
            }
            .stButton>button:hover { background-color: #444c5c; color: white; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 🔹 Title
    st.markdown("<h1>🏏 About This Project</h1>", unsafe_allow_html=True)

    # 🔹 Project Overview
    st.markdown("---")
    st.markdown("## 🚀 What is This Project About?")
    st.markdown(
        """
        This **AI-powered Cricket Analysis** tool helps evaluate batting techniques using **Deep Learning** and **Pose Estimation**.  
        By analyzing player movements and comparing them with **ideal batting templates**, we assess whether a shot is technically sound.
        """
    )

    # 🔹 How It Works
    st.markdown("---")
    st.markdown("## ⚙️ How It Works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🔍 Pose Estimation")
        st.markdown(
            """
            - Detects **body movements** & **bat angles**.  
            - Identifies errors in footwork & shot selection.
            """
        )

    with col2:
        st.markdown("### 📊 Deep Learning Analysis")
        st.markdown(
            """
            - Compares shots with **trained models**.  
            - Provides a **real-time similarity score**.
            """
        )

    with col3:
        st.markdown("### 🏆 Insights & Feedback")
        st.markdown(
            """
            - Highlights **key areas of improvement**.  
            - Helps players adjust their technique **scientifically**.
            """
        )

    # 🔹 Player-Specific Analysis
    st.markdown("---")
    st.markdown("## 🏏 Player-Specific Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏆 Virat Kohli Model")
        st.markdown(
            """
            - 📅 **2020-2025 Data (plus 2014 images)**.  
            - 🎯 Focuses on **off-stump struggles vs. pace**.  
            - ❌ Detects faulty movements **(early trigger, backfoot issues)**.
            """
        )

    with col2:
        st.markdown("### 🌟 Joe Root Model")
        st.markdown(
            """
            - 📅 **2021-2025 Peak Performance Data**.  
            - 🎯 Evaluates **template-based shot selection**.  
            - ✅ Checks **foot placement & bat flow consistency**.
            """
        )

    # 🔹 Technologies Used
    st.markdown("---")
    st.markdown("## 🛠️ Technologies Powering This")
    
    tech_list = [
        "🤖 **Deep Learning** (ConvNeXt, Autoencoders)",
        "🎯 **Pose Estimation** (OpenPose, BlazePose)",
        "🕵️‍♂️ **Computer Vision** (OpenCV, Keypoint Detection)",
        "💻 **Python & AI** (Streamlit, FastAPI, NumPy, Pandas)",
        "📡 **Web Scraping** (BeautifulSoup, Cricbuzz API)"
    ]

    for tech in tech_list:
        st.markdown(f"- {tech}")

    # 🔹 Special Acknowledgment
    st.markdown("---")
    st.markdown("<h3 style='text-align:center;'>🙏 Special Acknowledgment</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        **A huge thanks to [Prasanna Agoram](https://twitter.com/PrasannaAgoram) for reshaping my perspective on cricket analysis.**  
        His insights have played a key role in shaping this project's methodology.  
        """
    )

    # 🔹 Final Note
    st.markdown("---")
    st.markdown("<h3 style='text-align:center;'>🏏 AI Meets Cricket – Developed with ❤️</h3>", unsafe_allow_html=True)

    # 🔹 Back Button
    st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
