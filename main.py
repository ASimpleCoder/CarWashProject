email = "python.user.143@gmail.com"
password = "dqzr zdrj pwbx rifr"
reciever = "boycalledutkarsh@gmail.com"

import streamlit as st
import smtplib as smtp
import datetime

st.title("SparkRide Carwash Easy Bookings")
st.subheader("Book A Variety Of Car Washes and Get them in just a day")
st.write("*To book instant car washes (washes in under a hour), please call +91 1234567890")

st.subheader("Book a car wash for a set day")
date = st.date_input("Day Of Carwash:", datetime.date.today())
time = st.time_input("Time Of Carwash:")
parking = st.text_input("Enter Parking Lot Number:")

st.subheader("Select Package")
selected = st.radio("Select a option to wash your car", [
    "Simple Microfiber Rub - ₹100",
    "Microfiber rub with water, soap - ₹200",
    "Hardcore scrub - ₹250"
])

if st.button("Submit a booking"):
    try:
        with smtp.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(email, password)

            message = f"""Subject: New SparkRide Booking

NEW BOOKING ARRIVED

Day: {date}
Time: {time}
Parking Lot Number: {parking}
Package: {selected}
"""

            server.sendmail(email, receiver, message.encode('utf-8'))

        st.success("✅ Booking submitted! You may now close this tab.")
    except Exception as e:
        st.error(f"Booking failed: {e}")
