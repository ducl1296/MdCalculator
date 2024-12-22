import streamlit as st

st.set_page_config(
    page_title="🩺 MdCalculator",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("🩺 MdCalculator")

st.page_link("pages/BalanceHidrico.py", label="Balance Hidrico", icon="🚰")

