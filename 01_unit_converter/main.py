import streamlit as st

# Conversion Functions
def convert_km_to_miles(km):
    return round(km * 0.621371, 4)

def convert_miles_to_km(miles):
    return round(miles * 1.60934, 4)

def convert_kg_to_pounds(kg):
    return round(kg * 2.20462, 4)

def convert_pounds_to_kg(pounds):
    return round(pounds * 0.453592, 4)

def convert_celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 4)

def convert_fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 4)

def convert_cm_to_inch(cm):
    return round(cm * 0.393701, 4)

def convert_inch_to_cm(inch):
    return round(inch * 2.54, 4)

def convert_kilogram_to_gram(kilogram):
    return round(kilogram * 1000, 4)

def convert_gram_to_kilogram(gram):
    return round(gram * 0.001, 4)

def convert_m_to_yards(m):
    return round(m * 1.09361, 4)

def convert_yards_to_m(yards):
    return round(yards * 0.9144, 4)

# Page Configuration
st.set_page_config(page_title="Unit Converter")
st.title("Unit Converter")
st.write("Welcome! Easily convert units below.")

# Conversion Category
conversion_type = st.selectbox(
    "Select a category:",
    ["Length", "Weight", "Temperature", "Distance"],
    key="conversion_type"
)

# Input Value
val_num = st.number_input("Enter value to convert:", value=0.0, step=0.1)

# Length Conversion
if conversion_type == "Length":
    length_conversion = st.selectbox("Select conversion:", [
        "Kilometers to Miles",
        "Miles to Kilometers",
        "Centimeters to Inches",
        "Inches to Centimeters"
    ])
    if length_conversion == "Kilometers to Miles":
        st.success(f"{val_num} Kilometers = {convert_km_to_miles(val_num)} Miles")
    elif length_conversion == "Miles to Kilometers":
        st.success(f"{val_num} Miles = {convert_miles_to_km(val_num)} Kilometers")
    elif length_conversion == "Centimeters to Inches":
        st.success(f"{val_num} Centimeters = {convert_cm_to_inch(val_num)} Inches")
    elif length_conversion == "Inches to Centimeters":
        st.success(f"{val_num} Inches = {convert_inch_to_cm(val_num)} Centimeters")

# Weight Conversion
elif conversion_type == "Weight":
    weight_conversion = st.selectbox("Select conversion:", [
        "Kilograms to Pounds",
        "Pounds to Kilograms",
        "Kilograms to Grams",
        "Grams to Kilograms"
    ])
    if weight_conversion == "Kilograms to Pounds":
        st.success(f"{val_num} Kilograms = {convert_kg_to_pounds(val_num)} Pounds")
    elif weight_conversion == "Pounds to Kilograms":
        st.success(f"{val_num} Pounds = {convert_pounds_to_kg(val_num)} Kilograms")
    elif weight_conversion == "Kilograms to Grams":
        st.success(f"{val_num} Kilograms = {convert_kilogram_to_gram(val_num)} Grams")
    elif weight_conversion == "Grams to Kilograms":
        st.success(f"{val_num} Grams = {convert_gram_to_kilogram(val_num)} Kilograms")

# Temperature Conversion
elif conversion_type == "Temperature":
    temperature_conversion = st.selectbox("Select conversion:", [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ])
    if temperature_conversion == "Celsius to Fahrenheit":
        st.success(f"{val_num}°C = {convert_celsius_to_fahrenheit(val_num)}°F")
    elif temperature_conversion == "Fahrenheit to Celsius":
        st.success(f"{val_num}°F = {convert_fahrenheit_to_celsius(val_num)}°C")

# Distance Conversion
elif conversion_type == "Distance":
    distance_conversion = st.selectbox("Select conversion:", [
        "Meters to Yards",
        "Yards to Meters"
    ])
    if distance_conversion == "Meters to Yards":
        st.success(f"{val_num} Meters = {convert_m_to_yards(val_num)} Yards")
    elif distance_conversion == "Yards to Meters":
        st.success(f"{val_num} Yards = {convert_yards_to_m(val_num)} Meters")
