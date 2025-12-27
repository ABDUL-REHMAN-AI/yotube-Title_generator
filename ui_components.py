import streamlit as st

def inject_design():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #0f0f0f;
    }

    .main {
        background: linear-gradient(180deg, #1a1a1a 0%, #000000 100%);
    }

    /* Gradient Text */
    .hero-title {
        background: linear-gradient(90deg, #ff0000, #ff8000, #ff0080);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        margin-top: 20px;
        transition: 0.3s ease;
    }
    
    .glass-card:hover {
        border: 1px solid rgba(255, 0, 0, 0.5);
    }

    /* Premium Button */
    .stButton>button {
        background: linear-gradient(90deg, #FF0000 0%, #CC0000 100%);
        color: white;
        border-radius: 50px;
        padding: 1.5rem 3rem;
        font-size: 1.2rem;
        font-weight: bold;
        border: none;
        width: 100%;
        transition: 0.4s all ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 0, 0, 0.4);
    }

    /* YT Preview */
    .yt-box {
        background: #1e1e1e;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)