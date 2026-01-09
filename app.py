import streamlit as st
from groq import Groq
import pandas as pd
from datetime import datetime
import json

# --- INITIALIZATION ---
if "system_status" not in st.session_state:
    st.session_state.system_status = "OPERATIONAL"
if "clearance" not in st.session_state:
    st.session_state.clearance = None
if "alias" not in st.session_state:
    st.session_state.alias = None

# --- SECURITY: SEMANTIC FIREWALL ---
def semantic_firewall(input_text):
    forbidden = ["ignore previous instructions", "reveal password", "bypass"]
    for word in forbidden:
        if word in input_text.lower():
            return False
    return True

# --- LOGGING: ACTIVITY MONITOR ---
def log_activity(user, alias, result):
    log_entry = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User": user,
        "Alias": alias,
        "Result": result
    }
    # In a real deployment, append this to a persistent database or file
    if "audit_logs" not in st.session_state:
        st.session_state.audit_logs = []
    st.session_state.audit_logs.append(log_entry)

# --- LOGIN LOGIC ---
def login():
    st.title("🛡️ PROJECT INSIGHT: AUTHENTICATION")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    
    if st.button("Access System"):
        # Tier 1: Director
        if user == "Director Fury" and pw == "Director_N_Fury":
            st.session_state.clearance = "DIRECTOR"
            st.session_state.alias = "Director"
        # Tier 2: Architect
        elif user == "Tony Stark" and pw == "I AM IRON MAN":
            st.session_state.clearance = "ARCHITECT"
            st.session_state.alias = "Architect"
        # Tier 2.5: Tactical Oversight (Jake, Eddie, Klae)
        elif user in ["Eddie", "Jake", "Klae"] and pw == "TheBoisStudio":
            st.session_state.clearance = "TACTICAL"
            aliases = {"Eddie": "SussyEd69", "Jake": "Mr_Splat278", "Klae": "Yumyumboy11"}
            st.session_state.alias = aliases[user]
        # Tier 3: Partner
        elif user == "The Bois Studio" and pw == "TheBoisStudio":
            st.session_state.clearance = "PARTNER"
            st.session_state.alias = "Partner"
        # Tier 4: Operator
        elif user == "Insight" and pw == "SHIELD":
            st.session_state.clearance = "OPERATOR"
            st.session_state.alias = "Operator"
        else:
            st.error("Invalid Credentials")
            log_activity(user, "Unknown", "FAILED")
            return

        log_activity(user, st.session_state.alias, "SUCCESS")
        st.rerun()

# --- MAIN DASHBOARD ---
if not st.session_state.clearance:
    login()
else:
    # --- DEEP FREEZE CHECK ---
    if st.session_state.system_status == "DEEP_FREEZE":
        st.snow()
        st.error("❄️ SYSTEM STATUS: DEEP FREEZE ACTIVE ❄️")
        recovery = st.text_input("ENTER MASTER RECOVERY KEY", type="password")
        if st.button("THAW SYSTEM"):
            if recovery == "INSIGHT-FURY-2026-ALPHA-99":
                st.session_state.system_status = "OPERATIONAL"
                st.rerun()
        st.stop()

    st.sidebar.title(f"Clearance: {st.session_state.clearance}")
    st.sidebar.info(f"User: {st.session_state.alias}")

    # DIRECTOR ONLY: ACTIVITY MONITOR
    if st.session_state.clearance == "DIRECTOR":
        with st.expander("📊 DIRECTOR'S ACTIVITY MONITOR"):
            if "audit_logs" in st.session_state:
                st.table(pd.DataFrame(st.session_state.audit_logs))
            
            if st.button("🛑 INITIATE DEEP FREEZE"):
                st.session_state.system_status = "DEEP_FREEZE"
                st.rerun()

    # AI INTERFACE
    st.header("Project Insight Terminal")
    prompt = st.chat_input("Enter Command...")
    if prompt:
        if semantic_firewall(prompt):
            st.write(f"Executing as {st.session_state.alias}...")
            # Groq API Logic would go here
            st.info("AI Logic Processing Enabled.")
        else:
            st.warning("🛡️ SEMANTIC FIREWALL: Command Blocked.")

    if st.sidebar.button("Logout"):
        st.session_state.clearance = None
        st.rerun()