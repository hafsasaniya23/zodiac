import streamlit as st
import pandas as pd
from PIL import Image

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#get the zodiac using the month and the day

def find_zodiac(month,day):
    if month== 'december':
        astro_sign= 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month== 'january':
        astro_sign= 'Capricorn' if (day < 20) else 'Aquarius'
    elif month== 'february':
        astro_sign= 'Aquarius' if (day < 19) else 'Pisces'
    elif month== 'march':
        astro_sign= 'Pisces' if (day < 21) else 'Aries'
    elif month== 'april':
        astro_sign= 'Aries' if (day < 20) else 'Taurus'
    elif month== 'may':
        astro_sign= 'Taurus' if (day < 21) else 'Gemini'
    elif month== 'june':
        astro_sign= 'Gemini' if (day < 21) else 'Cancer'
    elif month== 'july':
        astro_sign= 'Cancer' if (day < 23) else 'Leo'
    elif month== 'august':
        astro_sign= 'Leo' if (day < 23) else 'Virgo'
    elif month== 'september':
        astro_sign= 'Virgo ' if (day < 23) else 'Libra'
    elif month== 'october':
        astro_sign= 'Libra' if (day < 23) else 'Scorpio'
    elif month== 'november':
        astro_sign= 'Scorpio' if (day < 23) else 'Sagittarius'
    return astro_sign

def load_data(data):
    return pd.read_csv(data)
def  main():

    st.title("Zodiac Whispers")
    st.subheader("Where Stars Align with Your Personality")

    st.write("Welcome to Connecting Hearts with Cosmic Insights")
    menu= ["Home","Stellar Pinboard","Cosmic Constellation Collection"]
    choice = st.sidebar.selectbox("Menu",menu)
    df = load_data('C:/Users/DELL/Documents/class/3/zodiac_data.csv')

    if choice == "Home":
        st.subheader("Home")
        dob = st.date_input("Date of Birth")
        month_of_birth = st.selectbox("Month",month_list)
        day_of_birth = st.number_input("Date",min_value=1,max_value=31)
        if st.button("Predict"):
            st.write(dob)
            results = find_zodiac(month_of_birth.lower(),day_of_birth)
            st.success("Results")
            st.write("You are ::{}".format(results))
            zdf= df[df["horoscope"] == results.title()]
            #st.dataframe(zdf)
            st.write('Alias::{}'.format(zdf.iloc[0].aliasname))
            rcol1,rcol2,rcol3 = st.columns([2,1,1])
            with rcol1:
                st.info("Description")
                st.write(zdf.iloc[0].description)
            with rcol2:
                with st.expander("Positives "):
                    st.write(zdf.iloc[0].positives.split(','))
            with rcol3:
                with st.expander("Negatives "):
                    st.write(zdf.iloc[0].negatives.split(','))



    elif choice == "Stellar Pinboard":
        st.subheader("Explore the Mysteries of Your Zodiac")
        st.dataframe(df)

    else:
        st.subheader("Journey Through the Stars, Discover Yourself")
        image_paths = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg",
                   "image5.jpg", "image6.jpg", "image7.jpg", "image8.jpg",
                   "image9.jpg", "image10.jpg", "image11.jpg", "image12.jpg"]
        labels = ["Empathetic but indecisive", "Spontaneous but flighty", "Intense but secretive", "Perfectionist but self-critical",
              "Confident but dominating", "Passionate but uncommunicative", "Versatile but impatient", "Loyal but stubborn",
              "Whimsical but over-sensitive", "Philosophical but detached", "Goal-oriented but unforgiving", "Competitive but insecure"]
    
        num_images = len(image_paths)
        num_cols = 4  # Number of columns in the grid
        image_size = 200  # Size of each image in pixels

        col1, col2, col3, col4 = st.columns(num_cols)

        for i in range(num_images):
            if i % num_cols == 0:
                col = col1
            elif i % num_cols == 1:
                col = col2
            elif i % num_cols == 2:
                col = col3
            else:
                col = col4

            with col:
                image = Image.open(image_paths[i])
                st.image(image, caption=labels[i], width=image_size)

if  __name__ == '__main__':
    main()

