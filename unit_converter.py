import streamlit as st

#Title of the app
st.title("🔃Unit Converter App")
# smaller heading below main heading 
st.markdown("### Convert Length, Weight and Temperature Instantly.🚀")
#welcome note
st.write("Welcome! Please select a category and enter a value to get the converted result in real-time.")
#to select conversion type by user from provided list
type_conversion= st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
#Defining units in dictionary
units={
    "Length": ["Meters", "Kilometers", "Miles"," Feet"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
}
# to pick input & output units by user
input_unit= st.selectbox("From",units [type_conversion])
output_unit= st.selectbox("To", units [type_conversion])
# to get user input
value= st.number_input("Enter Value: ", min_value= 0.0, format="%.2f")
# Defining fuction to perform conversion
def convert_units(value, input_unit, output_unit, type_conversion):
    if type_conversion == "Length":
        conversion_factors={
            "Meters": {"Kilometers":0.001, "Miles":0.000621371, "Feet":3.28084},
            "Kilometers":{"Meters": 1000, "Miles": 0.621371, "Feet": 3280.84},
            "Miles":{"Meters": 1609.43, "Kilometers":1.60934, "Feet":5280},
            "Feet":{"Meters": 0.3048, "Kilometers":0.0003048, "Miles": 0.000189394}
        }
    elif type_conversion == "Weight":
        conversion_factors={
            "Kilograms":{"Grams":1000, "Pounds":2.20462, "Ounces":35.274},
            "Grams":{"Kilograms":0.001, "Pounds": 0.00220462, "Ounces":0.035274},
            "Pounds":{"Kilograms":0.453592, "Grams":453.592, "Ounces":16},
            "Ounces":{"Kilograms":0.0283495, "Grams":28.3495, "Pounds":0.0625}
        }
    elif type_conversion == "Temperature":
        if input_unit == output_unit:
            return value
        elif input_unit == "Celsius" and output_unit == "Fahrenheit":
            return(value*9/5)+32
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            return value + 273.15
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            return(value - 32) * 5/9
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            return value - 273.15
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        
        else: "Invalid Conversion"

    return value * conversion_factors.get(input_unit, {}).get(output_unit, 1)

# Conversion Button
if st.button("Convert 🔁"):
    result = convert_units(value, input_unit, output_unit, type_conversion)

    if isinstance(result, str):  # If the function returns "Invalid conversion"
        st.error(result)
    else:
        st.success(f"Converted Value: {result:.2f} {output_unit}")