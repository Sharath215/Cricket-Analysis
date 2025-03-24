import streamlit as st
import requests
import datetime
import time
import os
from PIL import Image
from werkzeug.utils import secure_filename

# ✅ Backend API URL (User Input)
NGROK_URL = st.text_input("Enter Backend URL:", "https://XXXXX.ngrok-free.app")

# ✅ Folder Setup
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Session State Management
if "processing_complete" not in st.session_state:
    st.session_state.processing_complete = False

if "uploaded_file_path" not in st.session_state:
    st.session_state.uploaded_file_path = None

if "score" not in st.session_state:
    st.session_state.score = None

def show_vk_input():
    st.markdown("<h2>📷 Virat Kohli - Shot Analysis</h2>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    shot_type = st.selectbox("Select Shot Type", ["Back Foot", "Front Foot"])
    section = st.selectbox("Select Section", ["IS", "T1", "T2", "PB", "PC"])
    years = list(range(2006, datetime.datetime.now().year + 1))
    year = st.selectbox("Select the Year", years[::-1])

    # ✅ Save File if Uploaded
    if uploaded_file:
        filename = secure_filename(uploaded_file.name)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        image = Image.open(uploaded_file)
        image = image.resize((640, 640))
        image.save(save_path)
        st.session_state.uploaded_file_path = save_path
        st.success(f"📂 Image stored at: `{save_path}`")

    # ✅ Upload & Start Processing
    if st.button("🛠️ Upload & Analyze", disabled=not st.session_state.uploaded_file_path):
        try:
            with st.spinner("🚀 Uploading image..."):
                with open(st.session_state.uploaded_file_path, "rb") as img_file:
                    files = {"file": img_file}
                    response = requests.post(f"{NGROK_URL}/upload", files=files, timeout=400)

            if response.status_code == 200:
                progress_bar = st.progress(0)
                status_text = st.empty()

                while True:
                    status_response = requests.get(f"{NGROK_URL}/status")
                    if status_response.status_code == 200:
                        progress_data = status_response.json()
                        status_text.text(f"🛠️ {progress_data['stage']}...")
                        progress_bar.progress(progress_data["progress"] / 100.0)

                        if progress_data["progress"] == 100:
                            result_response = requests.get(f"{NGROK_URL}/result")
                            if result_response.status_code == 200:
                                result = result_response.json()
                                st.session_state.score = result.get("score", "N/A")
                            else:
                                st.session_state.score = "Error fetching result"
                            break
                    time.sleep(3)  

                st.session_state.processing_complete = True
                st.success(f"✅ Processing Complete! Score: **{st.session_state.score}**")

            else:
                st.error("❌ Image processing failed!")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error: {str(e)}")

    # ✅ Get Final Result
    if st.button("🏆 Get Analysis Result", disabled=not st.session_state.processing_complete):
        st.session_state.page = "result"
        st.rerun()

    # ✅ Back to Home
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"
        st.rerun()
