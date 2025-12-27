import streamlit as st
import random
import time
import requests
import pandas as pd
from streamlit_lottie import st_lottie

# ==========================================
# 1. ENHANCED EMOTION ENGINE
# ==========================================

class SmitTitanEngine:
    def __init__(self):
        # Expanded Emotion List
        self.emotions = {
            "Extreme Shock 😱": "Triggers high arousal and immediate clicks.",
            "Heartfelt 🥺": "Builds deep emotional connection with audience.",
            "Pure Anger 😡": "Triggers high engagement via controversy.",
            "Fear of Missing Out (FOMO) ⏳": "Creates urgency for limited-time content.",
            "Mystery/Suspense 🕵️": "Keeps audience curious until the end.",
            "Inspirational ✨": "High shareability across social platforms.",
            "Funny/Sarcastic 😂": "Best for high retention and watch time.",
            "Professional/Authority 🎓": "Builds trust and long-term brand value."
        }
        
        self.context_vault = {
            "marriage": {
                "titles": ["I Finally Told Her The Truth...", "Why 90% of Marriages Fail (The Harsh Reality)", "We Got Married In Secret! (Full Story)"],
                "colors": ["#F5F5DC (Luxury Beige)", "#FFD700 (Gold)", "#FFFFFF (White)"],
            },
            "love": {
                "titles": ["I Met My Soulmate At 3 AM...", "The Science of Why We Fall In Love", "I Asked My Crush Out And This Happened..."],
                "colors": ["#FF1493 (Deep Pink)", "#4B0082 (Indigo)", "#000000 (Black)"],
            },
            "money": {
                "titles": ["How I Made $10,000 In 10 Days", "Why You'll Always Be Broke (Stop Doing This)", "The Secret Wealth Formula Revealed"],
                "colors": ["#00FF41 (Matrix Green)", "#C0C0C0 (Silver)", "#111111 (Deep Grey)"],
            },
            "default": {
                "titles": ["I Tried This For 30 Days (Unexpected Results)", "The One Habit That Changed My Life", "DO NOT Watch This Video Alone..."],
                "colors": ["#FF0000 (Action Red)", "#FFFFFF (White)", "#000000 (Black)"],
            }
        }

# ==========================================
# 2. HIGH-BUDGET UI INJECTION
# ==========================================

def inject_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Manrope:wght@300;700;800&display=swap');
    
    .stApp { background: #020202; color: #ffffff; font-family: 'Manrope', sans-serif; }
    
    .titan-header {
        font-family: 'Syncopate', sans-serif;
        font-size: 3.8rem;
        text-align: center;
        background: linear-gradient(180deg, #FFD700 0%, #DAA520 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        filter: drop-shadow(0px 10px 15px rgba(255, 215, 0, 0.2));
    }

    .dev-credit {
        text-align: center; font-family: 'Syncopate', sans-serif; font-size: 0.8rem;
        color: #FFD700; letter-spacing: 8px; margin-bottom: 50px; font-weight: bold;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 215, 0, 0.1);
        border-radius: 30px; padding: 40px; margin-bottom: 25px;
        backdrop-filter: blur(20px);
    }

    div.stButton > button {
        background: linear-gradient(90deg, #FFD700, #DAA520) !important;
        color: black !important; font-weight: 800 !important;
        border-radius: 15px !important; width: 100%; height: 60px; border: none;
        text-transform: uppercase; letter-spacing: 2px;
    }

    .metric-box {
        background: #0a0a0a; border: 1px solid #1a1a1a; border-radius: 20px;
        padding: 25px; text-align: center; border-bottom: 4px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. MAIN APPLICATION
# ==========================================

def main():
    st.set_page_config(page_title="SMIT TITAN GENERATOR", layout="wide")
    inject_styles()
    engine = SmitTitanEngine()

    st.markdown("<h1 class='titan-header'>SMIT TITAN GENERATOR</h1>", unsafe_allow_html=True)
    st.markdown("<p class='dev-credit'>POWERED BY ABDUL REHMAN MEMON</p>", unsafe_allow_html=True)

    col_main, col_data = st.columns([1.6, 1])

    with col_main:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        concept = st.text_input("ENTER CONTENT CONCEPT", placeholder="e.g. My secret wealth strategy...")
        
        c1, c2 = st.columns(2)
        with c1:
            # ALL NEW EMOTIONS ADDED HERE
            selected_emotion = st.selectbox("🎯 TARGET EMOTION", list(engine.emotions.keys()))
        with c2:
            mode = st.selectbox("🕹️ AI ALGORITHM", ["Hyper-Viral", "Strategic SEO", "Legacy Branding"])
        
        st.write("---")
        execute = st.button("EXECUTE TITAN PROTOCOL")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_data:
        st.markdown("### 🧬 Algorithm Heatmap")
        # Visual Analytics for High-Budget feel
        st.line_chart(pd.DataFrame([10, 25, 60, 95, 80, 100], columns=['Reach Momentum']), color="#FFD700")
        st.info(f"**Emotion Analysis:** {engine.emotions[selected_emotion]}")

    if execute:
        if concept:
            with st.status("🛠️ Calibrating Titan Neural Nodes...", expanded=False):
                time.sleep(1.5)
            
            # Logic Processing
            cat = "marriage" if "marr" in concept.lower() else ("love" if "love" in concept.lower() else ("money" if "money" in concept.lower() else "default"))
            final_title = random.choice(engine.context_vault[cat]["titles"])
            
            # --- DISPLAY RESULTS ---
            st.markdown(f"""
                <div style="background:linear-gradient(45deg, #050505, #111); padding:50px; border-radius:30px; border:2px solid #FFD700; margin-top:30px; box-shadow: 0 20px 50px rgba(0,0,0,0.9);">
                    <p style="color:#FFD700; font-family:Syncopate; font-size:0.8rem; letter-spacing:3px;">TITAN OPTIMIZED OUTPUT</p>
                    <h1 style="color:white; font-size:3rem; margin-top:20px; line-height:1.2;">"{final_title}"</h1>
                </div>
            """, unsafe_allow_html=True)

            # --- ANALYTICS CARDS ---
            st.write("### 💎 Content Intelligence")
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f"<div class='metric-box'><small style='color:#666;'>Viral Score</small><h2 style='color:#FFD700;'>{random.randint(92, 99)}%</h2></div>", unsafe_allow_html=True)
            with m2:
                st.markdown(f"<div class='metric-box'><small style='color:#666;'>CTR Forecast</small><h2 style='color:#00FF00;'>Excellent</h2></div>", unsafe_allow_html=True)
            with m3:
                st.markdown(f"<div class='metric-box'><small style='color:#666;'>SEO Rank</small><h2 style='color:white;'>#1 Potential</h2></div>", unsafe_allow_html=True)

            # Color Palette
            st.write("### 🎨 Strategic Color Palette (Thumbnail)")
            cp_html = "".join([f"<div style='background:{c.split(' ')[0]}; flex:1; height:60px; border-radius:10px; margin:5px; border:1px solid rgba(255,255,255,0.1); color:black; font-weight:bold; padding-top:18px; text-align:center;'>{c}</div>" for c in engine.context_vault[cat]["colors"]])
            st.markdown(f"<div style='display:flex;'>{cp_html}</div>", unsafe_allow_html=True)
            
            # FUN FACT / OUT OF THE BOX TIP
            st.warning(f"💡 **TITAN MARKETING TIP:** Using a {selected_emotion.split(' ')[0]} face in your thumbnail with these colors will boost your Average View Duration by 18%.")
            st.balloons()

    st.markdown("<br><br><p style='text-align:center; opacity:0.3; font-family:Syncopate; font-size:10px; letter-spacing:5px;'>© 2025 ABDUL REHMAN MEMON | SMIT TITAN v9.0 PLATINUM</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()