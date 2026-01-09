import streamlit as st
import pandas as pd
from datetime import datetime

# --- SYSTEM CONFIGURATION ---
st.set_page_config(page_title="INSIGHT // SENTINEL HUD", layout="wide", initial_sidebar_state="collapsed")

# SENTINEL HUD STYLING (The "Circle x Security Bot" Blend)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
    /* Card Styling */
    .st-emotion-cache-12w0qpk { background: rgba(22, 27, 34, 0.8); border: 1px solid #30363d; border-radius: 12px; padding: 20px; }
    /* Button Styling */
    .stButton>button { 
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%); 
        color: white; border: none; border-radius: 6px; font-weight: 600;
        transition: transform 0.1s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px rgba(46, 160, 67, 0.4); }
    /* Header Styling */
    .threat-bar { background: #161b22; border-left: 5px solid #238636; padding: 10px 20px; border-radius: 4px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- UNIFIED LOGIN ---
if "clearance" not in st.session_state:
    st.markdown("<h1 style='text-align: center; color: #5865F2;'>PROJECT INSIGHT // LOGIN</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        user = st.text_input("Username")
        pw = st.text_input("Access Key", type="password")
        if st.button("AUTHENTICATE"):
            if user == "Director Fury" and pw == "Director_N_Fury":
                st.session_state.clearance, st.session_state.alias = "DIRECTOR", "FURY"
            elif user in ["Eddie", "Jake", "Klae"] and pw == st.secrets["TA_PASS"]:
                st.session_state.clearance = "TACTICAL"
                aliases = {"Eddie": "SussyEd69", "Jake": "Mr_Splat278", "Klae": "Yumyumboy11"}
                st.session_state.alias = aliases[user]
            st.rerun()

# --- THE SENTINEL HUD ---
if "clearance" in st.session_state:
    # 1. THREAT LEVEL BAR
    st.markdown(f"""
        <div class='threat-bar'>
            <span style='color: #8b949e;'>SYSTEM_STATUS:</span> 
            <span style='color: #3fb950; font-weight: bold;'>● OPTIMAL</span>
            <span style='float: right; color: #8b949e;'>Clearance: {st.session_state.clearance} // User: {st.session_state.alias}</span>
        </div>
    """, unsafe_allow_html=True)

    # 2. METRICS (Circle Influence)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("NETWORK NODES", "12 Active", "Stable")
    m2.metric("API LATENCY", "14ms", "-2ms")
    m3.metric("BOT UPTIME", "99.98%")
    m4.metric("COMMANDS/MIN", "142")

    st.write("")

    # 3. MODULE GRID (Dyno Influence)
    col_main, col_logs = st.columns([3, 1])

    with col_main:
        st.subheader("🛠️ SYSTEM MODULES")
        tab1, tab2, tab3 = st.tabs(["🛡️ SECURITY", "🤖 AI_OPERATIONS", "📊 ANALYTICS"])
        
        with tab1:
            c1, c2 = st.columns(2)
            with c1:
                st.info("**ANTI-NUKE PROTOCOLS**")
                st.button("Enable Beast Mode")
                st.button("Cycle Permission Keys")
            with c2:
                st.info("**RAID PROTECTION**")
                st.button("Lock Server Channels")
                st.button("Initiate Captcha Sweep")

        with tab2:
            st.write("Link external AI workflows here.")
            st.button("Sync Llama-3 Registry")

    with col_logs:
        st.subheader("📜 ACTIVITY")
        st.code("13:45 - Eddie logged in\n13:46 - Scan Initiated\n13:50 - Firewall Updated", language="bash")

    if st.sidebar.button("Logout"):
        st.session_state.clearance = None
        st.rerun()
