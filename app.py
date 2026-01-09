import streamlit as st
import pandas as pd
from datetime import datetime

# PAGE CONFIG
st.set_page_config(
    page_title="SENTINEL // COMMAND HUD",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
#  🔥 GLOBAL UI THEME — HOLOGRAPHIC NEO-GLASS SHELL
# ============================================================
st.markdown("""
<style>
/* ---------------- BACKGROUND ---------------- */
.main {
    background: radial-gradient(circle at 20% 20%, #0f172a, #020617 70%);
    color: #cdd6f4 !important;
    font-family: 'Inter', sans-serif;
}

/* ---------------- NEO-GLASS PANELS ---------------- */
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 0 25px rgba(0, 150, 255, 0.08);
    border-radius: 16px;
    padding: 20px;
    backdrop-filter: blur(12px);
}

/* ---------------- BUTTONS ---------------- */
.stButton>button {
    background: linear-gradient(135deg, #3b82f6, #0ea5e9);
    border: none;
    color: white;
    padding: 0.6rem 1.1rem;
    border-radius: 8px;
    font-weight: 600;
    transition: 0.15s ease;
}

.stButton>button:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 0 15px rgba(14, 165, 233, 0.5);
}

/* ---------------- LOGIN CARD ---------------- */
.login-box {
    background: rgba(255, 255, 255, 0.04);
    padding: 40px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(15px);
    box-shadow: 0 0 30px rgba(59, 130, 246, 0.25);
}

/* ---------------- HEADER ---------------- */
.holo-header {
    padding: 14px 22px;
    border-left: 6px solid #3b82f6;
    background: rgba(255,255,255,0.04);
    border-radius: 6px;
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
}

/* METRICS CLEANER LOOK */
[data-testid="stMetricValue"] {
    color: #38bdf8 !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# 🔐 LOGIN INTERFACE
# ============================================================

if "clearance" not in st.session_state:

    st.markdown("<h1 style='text-align:center; color:#3b82f6;'>SENTINEL ACCESS PORTAL</h1>", unsafe_allow_html=True)
    st.write("")

    c1, c2, c3 = st.columns([1, 2, 1])

    with c2:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        user = st.text_input("👤 IDENTIFICATION")
        pw = st.text_input("🔑 ACCESS KEY", type="password")

        if st.button("INITIATE AUTH SEQUENCE"):
            if user == "Director Fury" and pw == "Director_N_Fury":
                st.session_state.clearance = "DIRECTOR"
                st.session_state.alias = "FURY"
            elif user in ["Eddie", "Jake", "Klae"] and pw == st.secrets["TA_PASS"]:
                st.session_state.clearance = "TACTICAL"
                aliases = {"Eddie": "SussyEd69", "Jake": "Mr_Splat278", "Klae": "Yumyumboy11"}
                st.session_state.alias = aliases[user]
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# 🛰️ MAIN SENTINEL HUD
# ============================================================

else:
    # HOLO HEADER
    st.markdown(f"""
        <div class='holo-header'>
            <span style='color:#94a3b8;'>SYSTEM STATUS:</span>
            <span style='color:#16a34a; font-weight:bold;'>● ONLINE</span>
            <span style='float:right; color:#a1a1aa;'>Clearance: {st.session_state.clearance} // Agent: {st.session_state.alias}</span>
        </div>
    """, unsafe_allow_html=True)

    # METRICS
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("NETWORK LOAD", "12 nodes", "Stable")
    m2.metric("API LATENCY", "14ms", "-2ms")
    m3.metric("BOT UPTIME", "99.98%")
    m4.metric("CMD/MIN", "142")

    st.write("")

    # GRID LAYOUT
    col_main, col_logs = st.columns([3, 1])

    # LEFT: MODULES
    with col_main:
        st.subheader("🧩 SYSTEM MODULE GRID")

        tab1, tab2, tab3 = st.tabs(["🛡 SECURITY", "🤖 AI OPS", "📊 ANALYTICS"])

        # SECURITY MODULE
        with tab1:
            c1, c2 = st.columns(2)

            with c1:
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                st.subheader("ANTI-NUKE PROTOCOL")
                st.button("Activate Beast Mode")
                st.button("Rotate Permission Keys")
                st.markdown("</div>", unsafe_allow_html=True)

            with c2:
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                st.subheader("RAID SHIELD")
                st.button("Lock Server Channels")
                st.button("Begin Captcha Sweep")
                st.markdown("</div>", unsafe_allow_html=True)

        # AI OPS
        with tab2:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("AI WORKFLOW SYNC")
            st.write("Link external AI clusters or bot frameworks.")
            st.button("Sync Llama-3 Registry")
            st.markdown("</div>", unsafe_allow_html=True)

        # ANALYTICS
        with tab3:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.write("Future analytics modules will display here.")
            st.markdown("</div>", unsafe_allow_html=True)

    # RIGHT: LOG PANEL
    with col_logs:
        st.subheader("📜 SYSTEM ACTIVITY")
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.code("13:45 - Eddie logged in\n13:46 - Scan Initiated\n13:50 - Firewall Updated")
        st.markdown("</div>", unsafe_allow_html=True)

    # LOGOUT
    if st.sidebar.button("Log Out"):
        st.session_state.clearance = None
        st.rerun()
