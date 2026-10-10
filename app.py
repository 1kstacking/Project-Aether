import streamlit as st
import json
import pandas as pd
import hashlib
import datetime
import random

# Enforce clean, modern responsive layout bounds
st.set_page_config(
    page_title="Project Aether: News & Alert Center", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🌌 PROJECT AETHER // TRANSMISSION CORE")
st.caption("Real-Time Automated Alert Layer • Immediate Event Notification Terminal")

# Initialize persistent memory state queues for tracking active alerts
if 'triggered_alerts' not in st.session_state:
    st.session_state.triggered_alerts = [
        {
            "Timestamp": datetime.datetime.now().strftime('%H:%M:%S'),
            "Type": "📡 INGESTION",
            "Message": "Global Aether communication channels verified. Webhook matrix standing by.",
            "Priority": "🟢 LOW"
        }
    ]

# Sidebar Administration Panel
st.sidebar.header("⚙️ Core Controls")
if st.sidebar.button("🧼 Reset Active Notification Buffer"):
    st.session_state.triggered_alerts = [
        {
            "Timestamp": datetime.datetime.now().strftime('%H:%M:%S'),
            "Type": "📡 INGESTION",
            "Message": "System event buffer purged. Node re-initialized.",
            "Priority": "🟢 LOW"
        }
    ]
    st.sidebar.success("Alert buffer cleared.")
    st.rerun()

# --- MODULE 1: AUTOMATED STREAM INGESTION ACTION GATE ---
st.header("⚡ Live Strategic Incident Generator")
st.write("Simulate or trigger incoming market transmissions to test instant system response limits:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚨 Inject Critical Volatility Event"):
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        st.session_state.triggered_alerts.insert(0, {
            "Timestamp": timestamp,
            "Type": "🔥 VOLATILITY",
            "Message": "CRITICAL RISK BREAK: Ticker symbol NVDA surged +12.4% over benchmark limits inside a sub-minute trading block!",
            "Priority": "🔴 CRITICAL"
        })
        st.rerun()

with col2:
    if st.button("📡 Inject System Gateway Warning"):
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        st.session_state.triggered_alerts.insert(0, {
            "Timestamp": timestamp,
            "Type": "⚠️ SYSTEM",
            "Message": "INGESTION DELAY: Secondary REST API endpoint gateway dropped packet connection handshake. Switching to fallback database.",
            "Priority": "🟡 WARNING"
        })
        st.rerun()

with col3:
    if st.button("📰 Ingest Institutional News Wire"):
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        st.session_state.triggered_alerts.insert(0, {
            "Timestamp": timestamp,
            "Type": "📰 WIRE",
            "Message": "NEWS FLASH: SEC announces revised framework criteria governing private alternative investment fund algorithmic portfolios.",
            "Priority": "🔵 INFO"
        })
        st.rerun()

# --- MODULE 2: HIGH-PRIORITY ACTION ALERTS SHOWCASE ---
st.header("🔔 Active System Notification Banners")

# Render flashing display states based on the most recent alert entry priority
if st.session_state.triggered_alerts:
    latest_event = st.session_state.triggered_alerts[0]
    
    if latest_event["Priority"] == "🔴 CRITICAL":
        st.error(f"‼️ **[{latest_event['Timestamp']}] {latest_event['Type']} DISRUPTION** — {latest_event['Message']}")
    elif latest_event["Priority"] == "🟡 WARNING":
        st.warning(f"⚠️ **[{latest_event['Timestamp']}] {latest_event['Type']} WARNING** — {latest_event['Message']}")
    elif latest_event["Priority"] == "🔵 INFO":
        st.info(f"📰 **[{latest_event['Timestamp']}] NEW WIRE ADVISORY** — {latest_event['Message']}")
    else:
        st.success(f"✅ **SYSTEM STATUS NORMAL:** {latest_event['Message']}")

# --- MODULE 3: STREAMING NEWS TICKER MATRIX LEDGER ---
st.header("📋 Continuous Ingested Transmission History Log")
st.write("Chronological ledger matrix tracking live alert packets processed without analytic bloat:")

# Convert state logs directly into a clean table structure
st.table(pd.DataFrame(st.session_state.triggered_alerts))
