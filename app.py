import streamlit as st
from utils import get_top_abuse_ips

st.set_page_config(page_title="Cyber Threat Intelligence Dashboard", layout="centered")

st.title("🛡️ Cyber Threat Intelligence Dashboard")
st.header("AbuseIPDB IOCs (Top 10 High Confidence IPs)")

ips = get_top_abuse_ips()

if ips and isinstance(ips, list):
    st.code("\n".join(ips), language="text")
else:
    st.error("Failed to fetch IOCs. Please check your API key or internet connection.")
