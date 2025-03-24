import streamlit as st
import requests
from PIL import Image

NGROK_URL = "https://XXXXX.ngrok-free.app"# Replace with your actual NGROK URL

st.set_page_config(page_title="Analysis Result", page_icon="🏏")
st.title("🏏 Analysis Result")

# Load the uploaded image from the 'uploads/' folder
if "uploaded_image_path" in st.session_state:
    image_path = st.session_state.uploaded_image_path  # Get stored image path
    image = Image.open(image_path)
    st.image(image, caption="Uploaded Image", use_column_width=True)
else:
    st.warning("⚠ No image found. Please upload an image first.")

# Fetch & display result
result_response = requests.get(f"{NGROK_URL}/result")

if result_response.status_code == 200:
    result = result_response.json()
    st.session_state.score = result.get("score", "N/A")
else:
    st.session_state.score = "Error fetching result"

st.success(f"🏆 **Score:** {st.session_state.score}")

# Button to go back
if st.button("🔄 Analyze Another Image"):
    st.switch_page("upload.py")  # Redirect to the upload page
