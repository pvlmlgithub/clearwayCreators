import streamlit as st
from backend2 import \
    get_weather_description
from datetime import datetime

st.title("Weather Forecast for the next days")

place = st.text_input("Place:")
date = st.date_input("Select a date:")
option = st.selectbox("Select data to use", ("Weather", "Sky"))
st.subheader(f"{option} for {date} in {place}")

if place:
    try:
        target_date = datetime.combine(date, datetime.min.time())

        filtered_data = get_weather_description(place, target_date)

        if option == "Weather":
            st.write(f"Weather Description: {filtered_data}")

        elif option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }

            if filtered_data in images:
                st.image(images[filtered_data], width=115)
            else:
                st.write(f"No image available for {filtered_data}")

    except KeyError:
        st.write("The place does not exist.")
    except Exception as e:
        st.write(f"An error occurred: {e}")
