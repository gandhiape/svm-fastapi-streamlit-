import streamlit as st
import requests

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="💜",
    layout="wide"
)

# ================= CSS ==================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#2E1065,#5B21B6,#7C3AED);
}

.main-title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:white;
}

.sub-title{
    text-align:center;
    color:#E9D5FF;
    font-size:18px;
    margin-bottom:30px;
}

.block-container{
    padding-top:2rem;
}

[data-testid="stNumberInput"]{
    background-color:#F5F3FF;
    border-radius:12px;
    padding:5px;
}

.stButton>button{
    width:100%;
    background:#9333EA;
    color:white;
    border:none;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#7E22CE;
    color:white;
}

.result-card{
    background:white;
    padding:25px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 5px 20px rgba(0,0,0,.3);
}

</style>
""", unsafe_allow_html=True)

# ================= Header ==================
st.markdown("<div class='main-title'>💜 Breast Cancer Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Support Vector Machine (SVM)</div>", unsafe_allow_html=True)

# ================= Sidebar ==================
st.sidebar.title("📋 Information")

st.sidebar.info("""
Masukkan nilai dari **30 fitur**
kemudian tekan tombol **Predict**
untuk mengetahui hasil prediksi.
""")

# ================= Input ==================

st.subheader("Input Feature")

col1, col2, col3 = st.columns(3)

inputs = []

for i in range(30):

    if i % 3 == 0:
        with col1:
            value = st.number_input(f"Feature {i+1}", key=i)
    elif i % 3 == 1:
        with col2:
            value = st.number_input(f"Feature {i+1}", key=i)
    else:
        with col3:
            value = st.number_input(f"Feature {i+1}", key=i)

    inputs.append(value)

st.write("")

# ================= Predict ==================

if st.button("🔮 Predict"):

    url = "https://web-production-cf0ee.up.railway.app/predict"

    response = requests.post(
        url,
        json={
            "features": inputs
        }
    )

    hasil = response.json()

    st.markdown("---")

    st.markdown(f"""
    <div class="result-card">

# 🩺 Prediction Result

### <span style="color:#7E22CE;">{hasil['prediction']}</span>

Probability

# {hasil['probability']:.2%}

    </div>
    """, unsafe_allow_html=True)
