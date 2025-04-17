import streamlit as st

# conversion logic
def convert_units(value, category, from_unit, to_unit):
    if category == "Length":
        length_factors = {
            "meter": 1,
            "centimeter": 0.01,
        }
        try:
            result = value * \
                length_factors[from_unit] / length_factors[to_unit]
            return result
        except KeyError:
            return "invaild unit  selection for length."
    elif category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == to_unit:
            return value
        else:
            return "invaild temperature conversion."
    else:
        return "conversion not supported"

# ui title
st.title("Unit converter by Ali dost")

# category selection
category = st.selectbox("Select Category", ["Length", "Temperature"])

# unit base category
if category == "Length":
    units = ["meter", "centimeter"]
else:
    units = ["Celsius", "Fahrenheit"]

    # inputs
value = st.number_input("Enter value")
from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("To:", units)

# button
if st.button("Convert"):
    result = convert_units(value, category, from_unit, to_unit)
    if isinstance(result, (int, float)):
        st.success(f"Converted Value: {round(result, 2)} {to_unit}")
    else:
        st.error(result)
