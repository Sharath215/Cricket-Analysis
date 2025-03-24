


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ✅ Apply dark theme for matplotlib
plt.style.use("dark_background")

def show_jr_purple_patch():
    # 🌟 Title - Center Aligned
    st.markdown("<h1 style='text-align: center; color: #FFA500;'>🔥 Joe Root's Redemption: Silencing the Doubters</h1>", unsafe_allow_html=True)

    # 🏏 Hero Image - Properly Sized
    st.image("assets/JR_Captain.jpg", width=700, use_container_width=True)

    # 🏏 Introduction - Before Jumping into Crisis
    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px;">
        <p style="font-size: 18px; color: #FFFFFF; text-align: left;">
        <b>Joe Root</b> has been England’s batting backbone for over a decade.  
        From his debut in 2012 to leading England as captain, he was a part of cricket’s Fab 4,  
        alongside Virat Kohli, Steve Smith, and Kane Williamson.  
        <br><br>
        However, between <b>2017 and 2020</b>, Root’s performances declined significantly.  
        Fans and critics started questioning his ability to convert starts into big scores,  
        making him the weakest member of the Fab 4.  
        <br><br>
        But then, everything changed. Root **reinvented himself post-2021** and shut down all doubts.  
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")  # 🔹 Separator for better readability

    # 📉 Joe Root's Conversion Rate Struggles (2017 - 2020)
    st.markdown("<h2 style='color: #FF4500;'>⚠️ The Conversion Crisis (2017 - 2020)</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("assets/JR_Conversion.jpg", width=600)

    with col2:
        st.markdown("""
        <p style="font-size: 18px; color: #FFFFFF; text-align: left;">
        Root’s biggest problem during this period was failing to convert 50s into 100s.  
        While Smith and Kohli dominated, Root struggled to finish strong. 
         
        <ul style="color: #FFFFFF; font-size: 18px;">
        <li>2017: 8 fifties, only 2 hundreds ❌</li>   
        <li>2018: 6 fifties, just 1 hundred ❌</li>   
        <li>2019: 4 fifties, 2 hundreds ❌</li>   
        <li>2020: 4 fifties, NO hundreds ❌</li>  
        </ul>
        
        His **Test average dropped**, and he lost his No.1 ranking.  
        Critics began to question whether he was still a part of the **Fab 4**.
        </p>
        """, unsafe_allow_html=True)

    st.write("---")  

    # 📜 The Story: From Doubts to Dominance (2021+)
    st.markdown("<h2 style='color: #32CD32;'>💪 The Redemption (2021-Present)</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px;">
    <p style="font-size: 18px; color: #FFFFFF;">
    After the <span style="color: #32CD32; font-weight: bold;">COVID break</span>, Root transformed into a Run Machine in Tests.  
    <ul style="color: #FFFFFF; font-size: 18px;">
    
    <li>📈 <span style="color: #FFD700;"><b>Record-breaking centuries</b></span> when England struggled</li>
          
    <li>🔥 <b>Most Test runs</b> in 2021 - the ultimate workhorse </li>
        
    <li>💪 Proved his critics wrong, making himself <b>England’s backbone</b> </li>
        
    </ul>
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")  

    # 📊 Joe Root's Test Stats Table
    st.subheader("📊 Joe Root's Test Stats (2021 - Present)")

    data = {
        "Year": ["2021", "2022", "2023", "2024*", "2025*"],
        "Matches": [15, 15, 8, 17, 6],
        "Innings": [29, 27, 14, 31, 12],
        "Runs": [1708, 1098, 787, 1556, 855],
        "Average": [61.00, 45.75, 65.58, 55.57, 71.25],
        "Strike Rate": [56.2, 63.76, 76.33, 63.38, 72.41],
        "Centuries": [6, 5, 4, 6, 4]
    }

    df = pd.DataFrame(data)

    st.dataframe(df.style.set_properties(**{
        "background-color": "#1E1E1E",
        "color": "#FFFFFF",
        "border": "1px solid #444"
    }).set_table_styles([
        {"selector": "thead th", "props": [("background-color", "#FFA500"), ("color", "#000000"), ("font-weight", "bold")]}
    ]))

    st.write("---")  

    # 📈 Performance Graph
    st.subheader("📈 Joe Root’s Test Performance (2021 - 2025)")

    years = ["2021", "2022", "2023", "2024*", "2025*"]
    runs = [1708, 1098, 787, 1556, 855]
    average = [61.00, 45.75, 65.58, 55.57, 71.25]
    centuries = [6, 5, 4, 6, 4]

    fig, ax1 = plt.subplots(figsize=(7, 4))

    sns.lineplot(x=years, y=runs, marker="o", color="#00BFFF", label="Total Runs", linewidth=2, ax=ax1)
    ax1.set_ylabel("Total Runs", color="#00BFFF", fontsize=12)
    ax1.tick_params(axis="y", labelcolor="#00BFFF")

    # Second y-axis for Average and Centuries
    ax2 = ax1.twinx()
    sns.lineplot(x=years, y=average, marker="s", linestyle="--", color="#32CD32", label="Batting Average", linewidth=2, ax=ax2)
    sns.lineplot(x=years, y=centuries, marker="^", linestyle=":", color="#FFD700", label="Centuries", linewidth=2, ax=ax2)
    ax2.set_ylabel("Average / Centuries", fontsize=12)

    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_title("📊 Joe Root's Transformation (2021 - 2025)", fontsize=14, fontweight="bold")

    ax1.legend(loc="upper left", fontsize=10, frameon=True, fancybox=True, edgecolor="white")
    ax2.legend(loc="upper right", fontsize=10, frameon=True, fancybox=True, edgecolor="white")

    st.pyplot(fig)
    
    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px;">
        <h2 style="color: #FF4500; text-align: center;">🔄 The Fab 4 Reshuffle</h2>
        <p style="font-size: 16px; color: #FFD700; font-weight: bold;">
        By 2025, Root had completely <b>flipped the Fab 4 narrative</b>.  
        </p>
        <ul style="color: #FFFFFF; font-size: 16px;">
        <li>🔥 Most consistent Test batter post-2021</li>
        <li>💪 Thrived under Bazball’s attacking style</li>
        <li>🏏 Silenced all doubters who questioned his Fab 4 status</li>
        </ul>
        <h2 style="color: #00BFFF; text-align: center;">🌟 The New No.1?</h2>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")  

    # ⬅️ Back Button
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
