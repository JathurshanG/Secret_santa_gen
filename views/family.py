# Family.py
import os
import streamlit as st
from pymongo import MongoClient
from datetime import datetime, time


def show_family():

    # --------------------------------------------------
    # MongoDB connection
    # --------------------------------------------------
    MONGO_URI = os.getenv("MONGO_URI")

    if not MONGO_URI:
        st.error("MONGO_URI not found. Please set the environment variable.")
        st.stop()

    client = MongoClient(MONGO_URI)
    db = client["family_management"]
    collection = db["families"]

    # --------------------------------------------------
    # Page content
    # --------------------------------------------------
    st.markdown(
        "<h1 style='text-align:center;'>Family Registration</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="max-width:700px; margin:auto; text-align: justify;">
        <p>
        Register families arriving on site.  
        This information will be shared with drivers so they can assign
        themselves to a pickup and track completed trips in real time.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------
    # Family form
    # --------------------------------------------------
    with st.form("family_form"):

        st.subheader("Family information")
        family_name = st.text_input("Family name (Last name & First name)")
        number_of_people = st.number_input(
            "Number of people",
            min_value=1,
            step=1
        )

        st.divider()

        st.subheader("Arrival")
        col1, col2 = st.columns(2)
        with col1:
            arrival_date = st.date_input("Arrival date")
        with col2:
            arrival_time = st.time_input(
                "Arrival time (optional)",
                value=time(12, 0)
            )

        st.subheader("Departure")
        col3, col4 = st.columns(2)
        with col3:
            departure_date = st.date_input("Departure date")
        with col4:
            departure_time = st.time_input(
                "Departure time (optional)",
                value=time(12, 0)
            )

        st.divider()

        transport_mode = st.selectbox(
            "Mode of transport",
            ["Plane", "Boat", "Bus", "Car","Train" ,"Other"]
        )

        extra = st.text_input("Extra information (optional)")

        submit = st.form_submit_button("Save family")

    # --------------------------------------------------
    # Insert into MongoDB
    # --------------------------------------------------
    if submit:

        if not family_name:
            st.warning("Please enter the family name.")
            st.stop()

        arrival_datetime = datetime.combine(arrival_date, arrival_time)
        departure_datetime = datetime.combine(departure_date, departure_time)

        if departure_datetime < arrival_datetime:
            st.warning("Departure cannot be before arrival.")
            st.stop()

        collection.insert_one({
            "family_name": family_name,
            "number_of_people": number_of_people,
            "arrival_datetime": arrival_datetime,
            "departure_datetime": departure_datetime,
            "transport_mode": transport_mode,
            "extra": extra,
            "status": "waiting",
            "assigned_driver": None,
            "created_at": datetime.utcnow()
        })

        st.success("Family successfully registered ✅")