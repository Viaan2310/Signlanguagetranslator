import streamlit as st
import time
import random
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="SignLingo",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .stApp {
        background-color: #fdfbf7;
    }
    .main-header {
        font-family: 'Playfair Display', serif;
        color: #1f2937;
        text-align: center;
    }
    .stButton>button {
        background-color: #0d9488;
        color: white;
        border-radius: 9999px;
        border: none;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #0f766e;
    }
    .transcript-box {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e5e7eb;
        height: 400px;
        overflow-y: auto;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- Mock Data ---
MOCK_TRANSLATIONS = [
  "Hello, how are you doing today?",
  "It's really nice to meet you.",
  "Could you please help me find the nearest hospital?",
  "I am looking for the library, is it close by?",
  "I have been practicing sign language for a few months.",
  "Thank you so much for your assistance.",
  "What time does the train leave?",
  "I hope you have a wonderful day ahead.",
  "My name is Sarah, what is yours?",
  "Can we meet again tomorrow?",
  "I need to buy some water.",
  "This technology is fascinating.",
  "Please speak a bit slower.",
]

# --- Session State ---
if 'translations' not in st.session_state:
    st.session_state.translations = []
if 'is_scanning' not in st.session_state:
    st.session_state.is_scanning = False

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2060/2060238.png", width=50)
    st.title("SignLingo")
    st.markdown("Real-time sign language translation powered by AI.")
    
    st.markdown("---")
    
    target_language = st.selectbox(
        "Translate to:",
        ["English", "Spanish", "French", "German", "Japanese"]
    )
    
    st.markdown("### Features")
    st.markdown("- 📹 **Real-time Detection**")
    st.markdown("- 🗣️ **Multi-Language**")
    st.markdown("- 🌐 **Universal Access**")
    
    st.markdown("---")
    if st.button("Clear History"):
        st.session_state.translations = []

# --- Main Content ---
st.markdown("<h1 class='main-header'>Bridging silence with <span style='color:#0d9488; font-style:italic;'>understanding.</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280; margin-bottom: 40px;'>Instant, AI-powered sign language translation directly in your browser.</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📹 Camera Input")
    # Streamlit's camera input captures a static image, but works for the UI demo
    camera_image = st.camera_input("Show sign language gestures")
    
    # Simulation Logic
    if camera_image:
        st.session_state.is_scanning = True
        # Simulate processing delay
        with st.spinner("Analyzing gestures..."):
            time.sleep(1.5)
            new_translation = random.choice(MOCK_TRANSLATIONS)
            st.session_state.translations.append(new_translation)
            st.success("Translation successful!")
    
    if not camera_image:
        st.info("Please allow camera access and take a photo to simulate translation.")

with col2:
    st.subheader("💬 Live Transcript")
    
    # Display translations
    transcript_container = st.container()
    with transcript_container:
        if not st.session_state.translations:
            st.markdown("""
                <div class='transcript-box' style='display:flex; align-items:center; justify-content:center; flex-direction:column; opacity:0.5;'>
                    <h3>Waiting for input...</h3>
                    <p>Translations will appear here</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div class='transcript-box'>", unsafe_allow_html=True)
            for i, text in enumerate(reversed(st.session_state.translations)):
                confidence = round(random.uniform(95.0, 99.9), 2)
                st.markdown(f"""
                <div style='margin-bottom: 15px; border-bottom: 1px solid #f3f4f6; padding-bottom: 10px;'>
                    <div style='display:flex; align-items:center; gap:10px;'>
                        <span style='background:#e0f2fe; color:#0284c7; padding:2px 8px; border-radius:12px; font-size:0.8em; font-weight:bold;'>#{len(st.session_state.translations) - i}</span>
                        <span style='font-size: 1.1em; color: #111827;'>{text}</span>
                    </div>
                    <div style='font-size: 0.8em; color: #9ca3af; margin-left: 40px; margin-top: 4px;'>
                        Confidence: {confidence}% • Model: ASL-v2.4
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<center style='color:#9ca3af; font-size:0.8em;'>© 2024 SignLingo Inc. Built with Streamlit.</center>", unsafe_allow_html=True)
