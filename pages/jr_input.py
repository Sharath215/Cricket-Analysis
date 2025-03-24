import streamlit as st
import requests
import datetime
import os
from PIL import Image
import io

# ✅ Backend API URL
FLASK_URL = "http://127.0.0.1:5001"

# ✅ Folder Structure
UPLOAD_FOLDER = os.path.abspath(os.path.join("backend", "uploads"))
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure folder exists

# ✅ Session State Initialization
if "steps" not in st.session_state:
    st.session_state.steps = {
        "uploaded": False,
        "processed": False,
        "cropped": False,
        "pose_detected": False
    }

if "uploaded_file_path" not in st.session_state:
    st.session_state.uploaded_file_path = None

if "filepath" not in st.session_state:
    st.session_state.filepath = None

def show_vk_input():
    st.markdown("<h2>📷 Joe Root - Shot Analysis</h2>", unsafe_allow_html=True)

    # ✅ Upload Image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    # ✅ Select Shot Type
    shot_type = st.selectbox("Select Shot Type", ["Back Foot", "Front Foot"])

    # ✅ Select Section
    section = st.selectbox("Select Section", ["IS", "T1", "T2", "PB", "PC"])

    # ✅ Select Year
    years = list(range(2006, datetime.datetime.now().year + 1))
    year = st.selectbox("Select the Year", years[::-1])

    # ✅ Store File Path in Session
    if uploaded_file is not None:
        st.success("✅ Image uploaded successfully!")

        # ✅ Save Image
        save_path = os.path.abspath(os.path.join(UPLOAD_FOLDER, uploaded_file.name))
        image = Image.open(uploaded_file)
        image = image.resize((640, 640))  
        image.save(save_path)

        st.session_state.uploaded_file_path = save_path
        st.success(f"📂 Image stored at: `{save_path}`")

    # ✅ Step 1: Upload to Backend
    upload_disabled = not st.session_state.uploaded_file_path
    if st.button("🛠️ Upload Image to Backend", disabled=upload_disabled):
        if not st.session_state.uploaded_file_path:
            st.warning("⚠️ Please upload an image first!")
            return

        try:
            with st.spinner("🛠️ Uploading image..."):
                with open(st.session_state.uploaded_file_path, "rb") as img_file:
                    files = {"file": img_file}
                    response = requests.post(f"{FLASK_URL}/upload", files=files, timeout=60)

            if response.status_code == 200:
                st.session_state.filepath = response.json().get("filepath", "")
                if not st.session_state.filepath:
                    st.error("❌ No file path returned from backend!")
                    return

                st.session_state.steps["uploaded"] = True
                st.success("✅ Image uploaded successfully!")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Upload failed! Error: {str(e)}")

    # ✅ Step 2: Preprocess Image
    preprocess_disabled = not st.session_state.steps["uploaded"]
    if st.button("🔄 Preprocess Image", disabled=preprocess_disabled):
        try:
            with st.spinner("🔄 Preprocessing Image..."):
                response = requests.post(f"{FLASK_URL}/process_image", json={"filepath": st.session_state.filepath}, timeout=60)

            if response.status_code == 200:
                st.session_state.processed_image = response.content
                st.session_state.steps["processed"] = True
                st.success("✅ Image preprocessed successfully!")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Image Processing failed! Error: {str(e)}")

    # ✅ Step 3: Detect & Crop Batsman
    crop_disabled = not st.session_state.steps["processed"]
    if st.button("🏏 Detect & Crop Batsman", disabled=crop_disabled):
        
        try:
            with st.spinner("🏏 Detecting & Cropping Batsman..."):
                response = requests.post(f"{FLASK_URL}/detect_batsman", json={"filepath": st.session_state.filepath}, timeout=120)

            if response.status_code == 200:
                st.session_state.cropped_image = response.content
                st.session_state.steps["cropped"] = True
                st.success(f"🎯 Batsman detection and crop for {shot_type} ({section}, {year}) completed!")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Batsman detection failed! Error: {str(e)}")

    # ✅ Step 4: Detect Pose
    pose_disabled = not st.session_state.steps["cropped"]
    if st.button("📌 Detect Pose", disabled=pose_disabled):
        try:
            with st.spinner("📌 Detecting Pose..."):
                response = requests.post(f"{FLASK_URL}/detect_pose", json={"filepath": st.session_state.filepath}, timeout=120)

            if response.status_code == 200 and response.content:
                st.session_state.pose_image = response.content
                st.session_state.steps["pose_detected"] = True
                st.success("✅ Pose detection completed!")
            else:
                st.error(f"❌ Pose detection failed! No image received. Response: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Pose detection failed! Error: {str(e)}")

    # ✅ Step 5: Get Final Result
    get_result_disabled = not all(st.session_state.steps.values())
    
    if st.button("🏆 Get Analysis Result", disabled=get_result_disabled):
        st.session_state.page = "result"
          # ✅ Ensure query param updates
        st.rerun()

    # ✅ Display Buttons for Each Step
    if st.session_state.steps["uploaded"]:
        if st.button("📂 Show Uploaded Image"):
            st.image(st.session_state.uploaded_file_path, caption="📂 Uploaded Image", width=300)

    if st.session_state.steps["processed"]:
        if st.button("🎨 Show Processed Image"):
            st.image(Image.open(io.BytesIO(st.session_state.processed_image)), caption="🎨 Processed Image", width=300)

    if st.session_state.steps["cropped"]:
        if st.button("🏏 Show Cropped Batsman"):
            st.image(Image.open(io.BytesIO(st.session_state.cropped_image)), caption="🏏 Cropped Batsman", width=300)

    if st.session_state.steps["pose_detected"]:
        if st.button("📌 Show Pose Detection"):
            st.image(Image.open(io.BytesIO(st.session_state.pose_image)), caption="📌 Pose Detection", width=300)

    # ✅ Back to Home Button
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"
        st.rerun()
