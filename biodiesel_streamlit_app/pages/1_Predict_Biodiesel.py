import streamlit as st
import pandas as pd
import joblib

# Load trained model and encoder
try:
    model = joblib.load("model.pkl")
    # Check if 'scaler' is needed based on your model training pipeline
    # scaler = joblib.load("scaler.pkl")
    encoder = joblib.load("biodiesel_encoder.pkl")
except FileNotFoundError:
    st.error("Model files not found. Please run the previous steps to save the model.")
    st.stop()

st.set_page_config(page_title="Predict Biodiesel", page_icon="🔍")

st.title("🔍 Predict Biodiesel Type")
st.markdown("Enter the parameters of the biodiesel sample to get a prediction.")

# Define input fields based on dataset features
# Make sure these match the features your model was trained on
def user_input_features():
    # You need to replace these with the actual feature names and appropriate ranges
    Acid_value = st.number_input("Acid value", value=0.5, step=0.1)
    CFPP = st.number_input("CFPP (°C)", value=0.3, step=0.1)
    Carbon_Residue = st.number_input("Carbon Residue (%)", value=0.4, step=0.1)
    Cetane_Number = st.number_input("Cetane Number", value=0.5, step=0.1)
    Cloud_Point = st.number_input("Cloud Point (°C)", value=0.4, step=0.1)
    Density = st.number_input("Density (g/cm³)", value=0.6, step=0.1)
    Flash_Point = st.number_input("Flash Point (°C)", value=0.5, step=0.1)
    HV = st.number_input("Heating Value (MJ/kg)", value=0.5, step=0.1)
    Iodine_Value = st.number_input("Iodine Value", value=0.5, step=0.1)
    Pour_Point = st.number_input("Pour Point (°C)", value=0.5, step=0.1)
    Specific_gravity = st.number_input("Specific Gravity", value=0.5, step=0.1)
    Sulphated_Ash = st.number_input("Sulphated Ash (%)", value=0.3, step=0.1)
    Sulphur_cont = st.number_input("Sulphur Content (ppm)", value=0.2, step=0.1)
    Viscosity = st.number_input("Viscosity (mm²/s)", value=0.4, step=0.1)
    Copper_strip_corr = st.number_input("Copper strip corr.", value=0.0, step=0.1)


    data = {
        'Acid value': Acid_value,
        'CFPP (0C)': CFPP,
        'Carbon Residue (%)': Carbon_Residue,
        'Cetane Number': Cetane_Number,
        'Cloud Point (0C)': Cloud_Point,
        'Density (g/cm3)': Density,
        'Flash Point (0C)': Flash_Point,
        'HV (MJ/kg)': HV,
        'Iodine Value': Iodine_Value,
        'Pour Point (0C)': Pour_Point,
        'Specific gravity': Specific_gravity,
        'Sulphated Ash (%)': Sulphated_Ash,
        'Sulphur cont (ppm)': Sulphur_cont,
        'Viscosity (mm2/S)': Viscosity,
        'Copper strip corr.': Copper_strip_corr # Added this feature
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader("🔍 Input Parameters")
st.write(input_df)

# Add a button to trigger prediction
if st.button("Predict Biodiesel Type"):
    # Ensure columns are in the same order as during training
    # You might need to store and load the column order from training
    # For now, assume input_df has the correct columns in correct order.
    # If your training had a different set or order of columns, you'd need
    # to handle that here, e.g., by reindexing input_df.

    # Scale features if your model pipeline included a scaler
    # if 'scaler' in locals(): # Check if scaler was loaded
    #     input_scaled = scaler.transform(input_df)
    # else:
    #     input_scaled = input_df # Use raw input if no scaler

    prediction_encoded = model.predict(input_df)[0] # Use input_df directly if no scaling in app
    predicted_type = encoder.inverse_transform([prediction_encoded])[0]

    st.success(f"### 🧬 Predicted Biodiesel Type: **{predicted_type}**")
    st.balloons()

