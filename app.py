import streamlit as st
from recommend import recommend_colleges

st.set_page_config(page_title="College Predictor", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #eef2f7;
}

/* Header */
.header {
    background-color: #002b5c;
    color: white;
    padding: 25px;
    border-radius: 8px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

/* Notice */
.notice {
    background-color: #d9edf7;
    color: black;
    padding: 15px;
    border-radius: 6px;
    margin-top: 15px;
    font-weight: 500;
}

/* Form box */
.form-box {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.15);
    margin-top: 20px;
}

/* Section Titles */
.section-title {
    color: black;
    font-size: 24px;
    font-weight: bold;
    margin-top: 40px;
}

/* Footer */
.footer {
    background-color: #002b5c;
    color: white;
    padding: 20px;
    text-align: center;
    margin-top: 60px;
    border-radius: 6px;
    font-size: 14px;
}

/* Button */
.stButton>button {
    background-color: #002b5c;
    color: white;
    font-weight: bold;
    height: 45px;
    border-radius: 6px;
    width: 100%;
}

.stButton>button:hover {
    background-color: #001a3d;
}

/* Input Labels */
label {
    color: #002b5c !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}

/* Input Borders */
div[data-baseweb="input"] > div {
    border: 2px solid #002b5c !important;
}

div[data-baseweb="select"] > div {
    border: 2px solid #002b5c !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='header'>🎓College Admission Predictor</div>", unsafe_allow_html=True)


st.markdown("""
<div class='notice'>
This portal predicts eligible engineering colleges based on your Entrance Rank,
Category (Caste), Gender, Budget and Preferred Location.
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>Enter Your Details</div>", unsafe_allow_html=True)
st.markdown("<div class='form-box'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    rank = st.number_input("Entrance Rank", min_value=1, step=1)
    category = st.selectbox(
        "Category",
        ["OC", "BC_A", "BC_B", "BC_C", "BC_D", "BC_E", "SC", "ST", "EWS"]
    )

with col2:
    budget = st.number_input("Annual Budget (₹)", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female"])
    location = st.text_input("Preferred Location (Optional)")

search = st.button("Predict Eligible Colleges")

st.markdown("</div>", unsafe_allow_html=True)

if search:
    results = recommend_colleges(rank, budget, location, category, gender)

    st.markdown("<div class='section-title'>Predicted Eligible Colleges</div>", unsafe_allow_html=True)

    if not results.empty:
        st.success("Colleges found based on your rank and category.")
        st.dataframe(results, use_container_width=True)
    else:
        st.error("No colleges found based on your criteria. Try adjusting rank, budget or location.")


st.markdown("<div class='section-title'>About Prediction System</div>", unsafe_allow_html=True)

st.markdown("""
<div style='color:black; font-size:16px; line-height:1.7;'>

This prediction system evaluates your entrance examination rank,
caste category, gender eligibility, tuition budget, and preferred location.

The algorithm compares your rank with official previous closing ranks
from engineering colleges and filters institutions where you meet
the eligibility criteria.

The results are generated using historical admission data
and are intended for guidance purposes only.

</div>
""", unsafe_allow_html=True)


st.markdown("<div class='section-title'>About Engineering</div>", unsafe_allow_html=True)

st.markdown("""
<div style='color:black; font-size:16px; line-height:1.7;'>

Engineering is the backbone of innovation and technological advancement.

It transforms theoretical knowledge into practical solutions —
from artificial intelligence and software systems
to civil infrastructure, renewable energy, and healthcare technology.

Your entrance rank is only the beginning of your journey.
Continuous learning, skill development, and perseverance
are what truly define a successful engineer.

The future belongs to innovators, creators, and problem solvers.
Start building yours today.

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class='footer'>
© 2026 All Rights Reserved by BlastBlazers Team
</div>
""", unsafe_allow_html=True)