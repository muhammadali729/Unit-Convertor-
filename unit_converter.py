import streamlit as st

# Conversion factors for length units
length_conversion = {
    "Meter": 1,
    "Kilometer": 0.001,
    "Centimeter": 100,
    "Millimeter": 1000,
    "Micrometer": 1e6,
    "Nanometer": 1e9,
    "Mile": 0.000621371,
    "Yard": 1.09361,
    "Foot": 3.28084,
    "Inch": 39.3701,
    "Light Year": 1.057e-16
}

# Streamlit UI
st.title("Google-like Unit Converter 🔄")

# Select input and output units
from_unit = st.selectbox("Convert from:", length_conversion.keys())
to_unit = st.selectbox("Convert to:", length_conversion.keys())

# Input value
value = st.number_input("Enter value:", min_value=0.0, format="%.6f")

# Perform conversion
if from_unit and to_unit:
    converted_value = value * (length_conversion[to_unit] / length_conversion[from_unit])
    st.success(f"{value} {from_unit} = {converted_value:.6f} {to_unit}")
else:
    st.warning("Select different units for conversion!")

# Footer
st.markdown("---")
st.caption("🔹 Built with ❤️ using Streamlit")
