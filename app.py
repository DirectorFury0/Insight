import streamlit as st
import pandas as pd
from datetime import datetime

# --- SYSTEM CONFIGURATION ---
st.set_page_config(page_title="INSIGHT // UNIFIED HUD", layout="wide", initial_sidebar_state="collapsed")

# Cyber-Grid Unified Aesthetic
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #00ffcc; font-family: 'Share Tech Mono', monospace; }
    .stButton>button { width: 100%; border: 1px solid #00ffcc; background-color: #161b22; color: #00ffcc; height: 3em; font-weight: bold; }
    .stButton>button:hover { background-color: #00ffcc; color: #0b0e14; box-shadow: 0 0 20px #00ffcc; }
    div[data-testid="stMetricValue"] { color: #00ffcc !important; font-family: 'Share Tech Mono'; }
    .status-box { border: 1px solid #00ffcc; padding: 20px; border-radius: 10px; background: rgba(0, 255, 204, 0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- UNIFIED AUTHENTICATION ---
if "clearance" not in st.session_state:
    st.title("🛰️ PROJECT INSIGHT // NODE_ACCESS")
    with st.container():
        col1, col2 = st.columns(2)
        with col1: user = st.text_input("IDENT_ID")
        with col2: pw = st.text_input("ACCESS_KEY", type="password")
        
        if st.button("ESTABLISH UPLINK"):
            # Shared Access Logic
            if user == "Director Fury" and pw == "Director_N_Fury":
                st.session_state.clearance, st.session_state.alias = "DIRECTOR", "FURY"
            elif user == "Tony Stark" and pw == "I AM IRON MAN":
                st.session_state.clearance, st.session_state.alias = "ARCHITECT", "STARK"
            elif user in ["Eddie", "Jake", "Klae"] and pw == st.secrets["TA_PASS"]:
                st.session_state.clearance = "TACTICAL"
                aliases = {"Eddie": "SussyEd69", "Jake": "Mr_Splat278", "Klae": "Yumyumboy11"}
                st.session_state.alias = aliases[user]
            else:
                st.error("UPLINK_FAILED // INVALID_IDENT")
                st.stop()
            st.rerun()

# --- UNIFIED HUD INTERFACE ---
if "clearance" in st.session_state:
    # SYSTEM HEADER
    st.title(f"// SYSTEM_HUD: {st.session_state.alias} // LEVEL: {st.session_state.clearance}")
    
    # HUD METRICS GRID
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("CORE_TEMP", "32°C", "STABLE")
    with m2: st.metric("ENCRYPTION", "AES-512", "ACTIVE")
    with m3: st.metric("UPLINK_SPEED", "1.2 GB/S")
    with m4: st.metric("THREAT_SCAN", "0 FOUND")
    
    st.write("---")

    # THE COMMAND MATRIX (Same Layout for Everyone)
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("### 📡 DATA_OPS")
        if st.button("RUN REGISTRY SCAN"):
            st.code("SCANNING... ALL 2026 NODES ONLINE")
        if st.button("PULL INTEL REPORT"):
            st.code("GENERATING INTEL SUMMARY...")

    with col_b:
        st.markdown("### 🛡️ SEC_OPS")
        if st.button("ENFORCE FIREWALL"):
            st.success("FIREWALL RE-INITIALIZED")
        if st.button("CLEAN CACHE"):
            st.warning("SYSTEM CACHE PURGED")

    with col_c:
        st.markdown("### 👥 TEAM_OPS")
        if st.button("LOCATE TEAM NODES"):
            st.write("CONNECTED: SussyEd69, Mr_Splat278, Yumyumboy11")
        if st.button("PING ALL HANDS"):
            st.info("BROADCAST SENT TO TACTICAL TEAM")

    # --- PERMISSION-BASED OVERRIDE (Hidden unless Director/Architect) ---
    if st.session_state.clearance in ["DIRECTOR", "ARCHITECT"]:
        st.write("---")
        st.markdown("### ⚠️ COMMAND_OVERRIDE")
        ov1, ov2 = st.columns(2)
        with ov1:
            if st.button("❄️ INITIATE DEEP FREEZE"):
                st.session_state.system_status = "DEEP_FREEZE"
                st.rerun()
        with ov2:
            if st.button("🛠️ EDIT REGISTRY"):
                st.write("ENTERING REGISTRY EDIT MODE...")

    if st.sidebar.button("TERMINATE_SESSION"):
        st.session_state.clearance = None
        st.rerun()
