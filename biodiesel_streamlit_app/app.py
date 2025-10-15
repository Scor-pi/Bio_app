import streamlit as st
import pandas as pd
import joblib

# ==============================
# ✅ Load model and encoder safely
# ==============================
MODEL_PATH = "model.pkl"
ENCODER_PATH = "biodiesel_streamlit_app/biodiesel_encoder.pkl"

try:
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
except Exception as e:
    st.error("❌ Model files not found or corrupted. Ensure 'model.pkl' and 'biodiesel_encoder.pkl' are in the same folder as this file.")
    st.stop()

# ==============================
# 🎨 Page Configuration
# ==============================
st.set_page_config(page_title="Biodiesel Type Prediction", page_icon="🧬", layout="centered")
st.title("🧬 Biodiesel Type Prediction")
st.write("Enter biodiesel parameters below to predict the biodiesel type.")

# ==============================
# 🧾 Input Fields
# ==============================
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        Acid_value = st.number_input("Acid value", min_value=0.0, step=0.1)
        CFPP = st.number_input("CFPP (°C)", min_value=0.0, step=0.1)
        Carbon_Residue = st.number_input("Carbon Residue (%)", min_value=0.0, step=0.1)
        Cetane_Number = st.number_input("Cetane Number", min_value=0.0, step=0.1)
        Cloud_Point = st.number_input("Cloud Point (°C)", min_value=0.0, step=0.1)
        Copper_strip_corr = st.number_input("Copper strip corr.", min_value=0.0, step=0.1)
        Density = st.number_input("Density (g/cm³)", min_value=0.0, step=0.1)
    with col2:
        Flash_Point = st.number_input("Flash Point (°C)", min_value=0.0, step=0.1)
        HV = st.number_input("Heating Value (MJ/kg)", min_value=0.0, step=0.1)
        Iodine_Value = st.number_input("Iodine Value", min_value=0.0, step=0.1)
        Pour_Point = st.number_input("Pour Point (°C)", min_value=0.0, step=0.1)
        Specific_gravity = st.number_input("Specific gravity", min_value=0.0, step=0.1)
        Sulphated_Ash = st.number_input("Sulphated Ash (%)", min_value=0.0, step=0.1)
        Sulphur_cont = st.number_input("Sulphur Content (ppm)", min_value=0.0, step=0.1)
        Viscosity = st.number_input("Viscosity (mm²/s)", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🔍 Predict Biodiesel Type")

# ==============================
# ⚙️ Prediction Logic
# ==============================
if submitted:
    input_data = pd.DataFrame([{
        'Acid value': Acid_value,
        'CFPP (0C)': CFPP,
        'Carbon Residue (%)': Carbon_Residue,
        'Cetane Number': Cetane_Number,
        'Cloud Point (0C)': Cloud_Point,
        'Copper strip corr.': Copper_strip_corr,
        'Density (g/cm3)': Density,
        'Flash Point (0C)': Flash_Point,
        'HV (MJ/kg)': HV,
        'Iodine Value': Iodine_Value,
        'Pour Point (0C)': Pour_Point,
        'Specific gravity': Specific_gravity,
        'Sulphated Ash (%)': Sulphated_Ash,
        'Sulphur cont (ppm)': Sulphur_cont,
        'Viscosity (mm2/S)': Viscosity
    }])

    try:
        pred_encoded = model.predict(input_data)[0]
        pred_label = encoder.inverse_transform([pred_encoded])[0]
        st.success(f"### 🧪 Predicted Biodiesel Type: **{pred_label}**")
        st.balloons()
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
