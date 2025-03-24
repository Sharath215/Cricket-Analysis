import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Apply dark theme for Matplotlib
plt.style.use("dark_background")

def show_vk_off_stump():
    st.markdown("""  
    <h1 style='text-align: center; color: #FF4500; font-family: "Times New Roman";'>  
    🏏 Virat Kohli's Off-Stump Struggles 🏏  
    </h1>  
    """, unsafe_allow_html=True)

    st.image("assets/VK_Off_Stump.jpg", use_container_width=True)  # ✅ Fix image loading

    # 🔴 2014 England Struggles
    st.markdown("""  
    <h2 style="font-family: 'Times New Roman'; color: #FFD700;">🔴 2014: The Nightmare Against Anderson</h2>  
    """, unsafe_allow_html=True)

    st.image("assets/VK_2014.jpg", width=600)  # ✅ Fix image loading

    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; text-align: left;">
        <p style="font-size: 18px; color: #FFFFFF; font-family: 'Times New Roman'; text-align: left;">
        The 2014 England tour was a baptism by fire for Kohli. James Anderson had him in a relentless loop—  
        ball after ball, tempting him to drive outside off. Time and again, Kohli fell into the trap, edging behind or to the slips.  
        He looked helpless.  
        </p>
        <ul style="color: #FFD700; font-size: 18px;">
            <li>🛑 <b>Runs in the series</b>: 134 in 10 innings</li>
            <li>🛑 <b>Average</b>: 13.40</li>
            <li>🛑 <b>Dismissed by Anderson</b>: 4 times in 49 balls</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 🟢 2018 Redemption Arc
    st.markdown("""  
    <h2 style="font-family: 'Times New Roman'; color: #FFD700;">🟢 2018: The Redemption</h2>  
    """, unsafe_allow_html=True)

    st.image("assets/VK_2018.jpg", width=600)  # ✅ Fix image loading

    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; text-align: left;">
        <p style="font-size: 18px; color: #FFFFFF; font-family: 'Times New Roman'; text-align: left;">
        Four years later, Kohli returned to England a transformed batter. He played patiently,  
        refusing to bite at deliveries he once chased. The result? <b>593 runs</b> at an impressive average of 59.30,  
        dominating England's pacers in their own backyard.  
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""  
    <h2 style="font-family: 'Times New Roman'; color: #FFD700;">⚠️ 2020 - 2025: The Ghost Resurfaces</h2>  
    """, unsafe_allow_html=True)

    st.image("assets/VK_2020.jpg", width=600)  # ✅ Fix image loading
    
    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; text-align: left;">
        
    <p style="font-size: 18px; color: #FFFFFF; font-family: 'Times New Roman'; line-height: 1.6; margin-bottom: 15px; text-align: left;">
        It all started in <b>Wellington, 2020</b>. Kyle Jamieson found the edge, and Kohli walked back, head down.  
        As a Test cricket fan, something felt wrong in my inner mind. It was the same mistake from 2014—reaching for a ball he didn't need to play.
        But this time, the problem didn’t just come and go—it stayed. Over the next few years, it haunted Kohli.
    </p>

    <p style="font-size: 18px; color: #FFFFFF; font-family: 'Times New Roman'; line-height: 1.6; margin-bottom: 15px; text-align: left;">
        Fast forward to <b>2024 at the MCG</b>, and history repeated itself. Scott Boland, with his relentless accuracy, set him up.  
        A delivery outside off, the slight movement, the edge… another walk back.
    </p>

    <p style="font-size: 18px; color: #FFFFFF; font-family: 'Times New Roman'; line-height: 1.6; margin-bottom: 0; text-align: left;">
        Five years on, the off-stump struggle remains.  
        The problem that Anderson exposed, that Jamieson reignited, and that Boland exploited—it’s still here. In the BGT series 24/25, All of Kohli's dismissals were either caught behind or at slips.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # Test Stats Table
    st.markdown("""
    <h3 style="font-family: 'Times New Roman'; color: #FFD700;">📊 Kohli's Test Stats (2021 - Present)</h3>
    """, unsafe_allow_html=True)

    data = {
        "Year": ["2020", "2021", "2022", "2023", "2024*"],
        "Matches": [3, 11, 6, 8, 10],
        "Innings": [6, 19, 11, 12, 19],
        "Runs": [116, 536, 265, 671, 417],
        "Average": [19.33, 28.21, 26.50, 55.91, 24.52],
        "Strike Rate": [40.98, 44.07, 39.43, 54.73, 61.96],
        "50+ Scores": [1, 4, 1, 4, 2]
    }

    df = pd.DataFrame(data)

    st.dataframe(df.style.set_properties(**{
        "background-color": "#1E1E1E",
        "color": "#FFFFFF",
        "border": "1px solid #444"
    }).set_table_styles([
        {"selector": "thead th", "props": [("background-color", "#FF4500"), ("color", "#000000"), ("font-weight", "bold")]}
    ]))

    # Graphs Layout
    col1, col2 = st.columns(2)

    # Runs & Average Graph
    with col1:
        st.markdown("<h3 style='color: #FFD700;'>📈 Runs & Batting Average</h3>", unsafe_allow_html=True)

        years = ["2020", "2021", "2022", "2023", "2024*"]
        runs = [116, 536, 265, 671, 417]
        average = [19.33, 28.21, 26.50, 55.91, 24.52]

        fig, ax1 = plt.subplots(figsize=(6.5, 4.5))

        sns.lineplot(x=years, y=runs, marker="o", color="#00BFFF", label="Total Runs", linewidth=2, ax=ax1)
        ax1.set_ylabel("Total Runs", color="#00BFFF", fontsize=12)
        ax1.tick_params(axis="y", labelcolor="#00BFFF")

        ax2 = ax1.twinx()
        sns.lineplot(x=years, y=average, marker="s", linestyle="--", color="#32CD32", label="Batting Average", linewidth=2, ax=ax2)
        ax2.set_ylabel("Average", fontsize=12)

        ax1.set_xlabel("Year", fontsize=12)
        ax1.set_title("Kohli's Performance Over Years", fontsize=13, fontweight="bold")

        ax1.legend(loc="upper left", fontsize=10, frameon=True, fancybox=True, edgecolor="white")
        ax2.legend(loc="upper right", fontsize=10, frameon=True, fancybox=True, edgecolor="white")

        st.pyplot(fig)

    # Strike Rate Graph
    with col2:
        st.markdown("<h3 style='color: #FFD700;'>📈 Strike Rate Trend</h3>", unsafe_allow_html=True)

        strike_rate = [40.98, 44.07, 39.43, 54.73, 61.96]

        fig2, ax3 = plt.subplots(figsize=(6.5, 4.5))

        sns.lineplot(x=years, y=strike_rate, marker="^", linestyle=":", color="#FF4500", label="Strike Rate", linewidth=2, ax=ax3)
        ax3.set_ylabel("Strike Rate", fontsize=12)
        ax3.set_xlabel("Year", fontsize=12)
        ax3.set_title("Kohli's Strike Rate (2020 - Present)", fontsize=13, fontweight="bold")

        ax3.legend(loc="upper left", fontsize=10, frameon=True, fancybox=True, edgecolor="white")

        st.pyplot(fig2)
    
    # 🏏 The Ultimate Fab 4 Reshuffle - Kohli’s Test Struggles
    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px;">
        <h2 style="color: #FF4500; text-align: center;">🔄 The Fab 4 Reshuffle</h2>
        <p style="font-size: 18px; color: #FFD700; font-weight: bold;">
        After 2019, Virat Kohli’s Test form took a shocking dip.  
        The man who once dictated Test cricket found himself struggling for runs,  
        and the centuries that once came naturally became an impossible task.  
        </p>
        <ul style="color: #FFFFFF; font-size: 18px;">
        <li>⚠️ No Test century between November 2019 and March 2023</li>
        <li>⚠️ Average dropped from 54.97  to 46.8</li>
        <li>⚠️ Home and away struggles</li>
        <li>⚠️ Root overtook him as the leading Fab 4 batter</li>
        <li>✅ Finally ended the drought with 186 vs Australia (2023)</li>
        <li>✅ Showed glimpses of form but still inconsistent</li>
        </ul>
        <h2 style="color: #00BFFF; text-align: center;">🤔 Will Kohli Ever Dominate in Tests Again?</h2>
    </div>
    """, unsafe_allow_html=True)


    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
