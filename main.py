import streamlit as st
import os
import smtplib as smtp

email = "python.user.143@gmail.com"
password = "dqzr zdrj pwbx rifr"
reciever = "boycalledutkarsh@gmail.com"

sender = smtp.SMTP("smtp.gmail.com")
sender.starttls()
sender.login(email, password)

st.title("SparkRide Carwash Easy Bookings")
st.subheader("Book A Variety Of Car Washes and Get them in just a day")
st.write("*To book instant car washes (washes in under a hour), please call +91 1234567890")

st.subheader("Book a car wash the for a set day")
date = st.date_input("Day Of Carwash: ", format="dd/MM/yyyy")
time = st.time_input("Time Of Carwash: ")
parking = st.text_input("Enter Parking Lot Number: ")

st.subheader("Select Package")
selected = st.radio("Select a option to wash your car", ["Simple Microfiber Rub - ₹100", "Microfiber rub with water, soap - ₹200", "Hardcore scrub - ₹250"])

submit_button = st.button("Submit a booking")

if submit_button:
  sender.sendmail(email, reciever, f"NEW BOOKING ARRIVED \n\n Day: {date}, Time: {time}, Parking Lot Number: {parking} \n Mode: {selected}")
  st.empty()
  st.success("✅ Booking submitted! You may now close this tab.")
  st.stop()
