
import streamlit as st
from model_utils import get_hr_score

st.set_page_config(page_title="HR Prediction Model", layout="centered")

st.title("💣 HR Prediction Model v3.0 (Simplified)")

st.markdown("This tool estimates a hitter’s HR probability using core power stats and pitcher tendencies.")

with st.form("hr_form"):
    batter_name = st.text_input("🔤 Batter Name")

    st.markdown("### 🧨 Hitter Power")
    barrel_rate = st.slider("Barrel Rate (%)", 0.0, 30.0, 10.0)
    exit_velocity = st.slider("Exit Velocity (mph)", 70.0, 120.0, 91.0)
    xSLG = st.slider("Expected Slugging (xSLG)", 0.300, 0.800, 0.650, step=0.050)
    st.markdown("_xSLG Guide: 0.300 = light hitter, 0.500 = solid, 0.650+ = elite power_")
    sweet_spot = st.slider("Sweet Spot Contact (%)", 0.0, 60.0, 35.0)

    st.markdown("### ⚾ Pitcher HR Risk")
    hr9 = st.slider("HRs Allowed per 9 IP", 0.0, 3.0, 1.2)

    # Fixed values for removed sliders
    park_factor = 0
    wind_boost = 0
    temp_boost = 0
    hard_hit_pct = 35
    fatigue = 5
    rpi = 0.5

    submitted = st.form_submit_button("📊 Calculate HR Probability")
    if submitted:
        score, sleeper = get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                                      hr9, hard_hit_pct, fatigue,
                                      park_factor, wind_boost, temp_boost)
        st.subheader(f"🔢 HR Score: {score:.1f} / 100")
        if sleeper:
            st.markdown("🧨 **Sleeper Tag: This batter has sneaky upside!**")
