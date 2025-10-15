import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AI Biodiesel Analyzer",
    page_icon="🌿",
    layout="wide"
)

st.sidebar.title("🌱 Navigation")
st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/1_Predict_Biodiesel.py", label="🔍 Predict Biodiesel")

st.markdown('''
    <style>
        .main {
            background-color: #F7F9FB;
        }
        h1, h2, h3 {
            color: #00695C;
        }
        .intro {
            font-size: 18px;
            line-height: 1.6;
        }
        .logo {
            text-align: center;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }
    </style>
''', unsafe_allow_html=True)

st.title("🌿 AI-Powered Biodiesel Prediction System")
st.subheader("Developed by MOHAMMED | Intelligent Fuel Analysis Platform")

st.markdown('''
<div class="intro">
Welcome to the **AI Biodiesel Analyzer** — a machine learning powered system that predicts the <b>type of biodiesel fuel</b> based on measured fuel parameters such as <b>viscosity, density, flash point, and heating value</b>.

This system was built using advanced supervised learning algorithms and optimized preprocessing techniques to enhance predictive accuracy and reliability.

**Key Features:**
- 🔍 Predicts biodiesel type with high accuracy
- ⚙️ Uses scaling, encoding, and intelligent feature selection
- 🧪 Interactive web interface built with Streamlit
- ☁️ Deployable on Render, Streamlit Community Cloud, or other platforms.
</div>

## How to Use:

1.  **Input Parameters:** Use the sidebar to enter the physicochemical properties of the biodiesel sample you want to analyze.
2.  **Predict:** Click the "Predict Biodiesel Type" button.
3.  **Result:** The app will display the predicted biodiesel type based on the trained AI model.

---

''', unsafe_allow_html=True)

st.markdown('<div class="footer">© 2025 ABU. All rights reserved.</div>', unsafe_allow_html=True)

# Add an image (optional)
# try:
#     image = Image.open('path/to/your/logo.png') # Replace with your image path
#     st.image(image, width=200)
# except FileNotFoundError:
#     st.warning("Logo image not found. Please update the path.")

