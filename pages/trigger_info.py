import streamlit as st  

# Custom CSS for enhanced styling
st.markdown("""
    <style>
        /* Set font to Times New Roman */
        * {
            font-family: "Times New Roman", serif;
        }

        /* Align all text to the left like a book */
        .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader {
            text-align: left !important;
        }

        /* Balance font sizes for readability */
        .stTitle { font-size: 32px !important; }
        .stHeader { font-size: 26px !important; }
        .stSubheader { font-size: 22px !important; }
        .stMarkdown p { font-size: 18px !important; }

        /* Reduce video size and add smooth appearance */
        video {
            width: 75% !important;
            border-radius: 12px;
            box-shadow: 3px 3px 12px rgba(0,0,0,0.2);
        }

        /* Center the back button */
        .stButton>button {
            width: 200px !important;
            font-size: 18px !important;
            font-weight: bold;
            border-radius: 10px;
            background-color: #1e90ff; /* Blue color */
            color: white;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

def trigger_explain():
    # Page Title
    st.title("🔄 Understanding Trigger Movements in Cricket")  
    st.write("### The Key to Better Batting Balance and Shot Selection")  
    st.markdown("---")

    # Introduction  
    st.subheader("🏏 What is Trigger Movement?")
    st.write("""
    In cricket, trigger movement refers to the small foot movements a batsman makes just before the bowler releases the ball. 
    These movements help maintain balance, improve shot execution, and adapt to different types of deliveries. 
    A well-timed trigger movement ensures the batsman is in sync with the bowler’s rhythm, enhancing their ability 
    to react to swing, seam, or pace effectively.
    """)

    # Steps Involved
    st.subheader("🔄 Steps Involved in a Good Trigger Movement")
    st.markdown("""
    <ul>
        <li><b>Initial Setup (Stance & Balance):</b> A solid, balanced stance with eyes level and weight evenly distributed.</li>
        <li><b>First Trigger Movement:</b> A small movement as the bowler lands the front foot, preparing for the shot.</li>
        <li><b>Second Trigger Movement:</b> The final adjustment as the ball is released to react to swing, seam, or bounce.</li>
        <li><b>Reading the Pitch of the Ball:</b> Assessing the length mid-air and shifting weight accordingly.</li>
        <li><b>Contact & Shot Execution:</b> Ensuring stability and clean shot execution.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Trigger Movement Types with Videos
    st.subheader("🎥 Types of Trigger Movements")

    # Back and Across Movement
    st.markdown("### 1️⃣ Back and Across Movement")
    st.write("""
    📌 The back foot moves slightly towards the middle stump, while the front foot comes across it.  
    ✅ Helps in covering off-stump and playing deliveries outside off.
    """)
    st.video("assets/Back_Across_JR.mp4", format="video/mp4")

    # Back Press Movement
    st.markdown("### 2️⃣ Back Press Movement")
    st.write("""
    📌 The batsman shifts their weight onto the back foot, preparing for short-pitched deliveries.  
    ✅ Ideal for handling bounce and playing shots square of the wicket.
    """)
    st.video("assets/Back_Press_FaF.mp4", format="video/mp4")

    # Front Press Movement
    st.markdown("### 3️⃣ Front Press Movement")
    st.write("""
    📌 The batsman makes a small forward movement with their front foot before the bowler releases the ball.  
    ✅ Helps in getting into position early for full-length deliveries and playing straight-bat shots effectively.
    """)
    st.video("assets/Front_Press_RP.mp4", format="video/mp4")

    # Double Front Press Movement
    st.markdown("### 4️⃣ Double Front Press Movement")
    st.write("""
    📌 The batsman makes two small forward movements with their front foot before the bowler releases the ball.  
    ✅ Helps in committing early to full deliveries and ensures better control over drives and front-foot play.
    """)
    st.video("assets/Double_Front_Press_JT.mp4", format="video/mp4")

    st.markdown("---")

    # Additional Content on Trigger Movement Analysis
    st.subheader("📊 Analyzing Trigger Movements for Kohli & Root")
    st.write("""
    Every batsman has a unique trigger movement that works best for them because apart from foot movement, 
    many factors influence batting performance. A batsman has only a split second to make a decision, 
    and the trigger movement helps align them to play the ball effectively.

    In this project, I have collected images of batsmen at the five key steps of trigger movement over the years.  
    - **Virat Kohli (2020-2025):** During this period, Kohli faced challenges in Test cricket.  
      To analyze his struggles, I gathered images of his trigger movements from these years and trained a model.  
    - **Joe Root (2020-2025):** In contrast, Root was in a golden phase, consistently scoring centuries.  
      Using the same methodology, I captured his trigger movements to understand what made his technique successful.

    By comparing these two players, we gain insight into how small adjustments in trigger movement 
    can impact a batsman’s success at the highest level.
    """)

    st.markdown("---")
    st.write("### More trigger movement insights coming soon! Stay tuned. ⚡")
    
    if st.button("⬅️ Back to Home"):
        
        st.session_state.page = "home"
        st.rerun()



# Run the function when the script is executed

