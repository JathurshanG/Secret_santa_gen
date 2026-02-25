import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# MongoDB Atlas (Streamlit Cloud Secret)
client = MongoClient(st.secrets["MONGO_URI"])
db = client["family_management"]
collection = db["families"]

st.title("🚐 Family Pickup Management – MVP")

# -----------------------------
# 1) FAMILY REGISTRATION
# -----------------------------
st.header("➕ Register a Family")

with st.form("family_form"):
    last_name = st.text_input("Last name")
    first_name = st.text_input("First name")
    number_of_people = st.number_input("Number of people", min_value=1, step=1)
    arrival_date = st.date_input("Arrival date")
    origin_country = st.text_input("Country of origin")
    transport_mode = st.selectbox(
        "Mode of transport",
        ["Plane", "Boat", "Bus", "Car", "Other"]
    )
    submit_family = st.form_submit_button("Save family")

if submit_family:
    collection.insert_one({
        "last_name": last_name,
        "first_name": first_name,
        "number_of_people": number_of_people,
        "arrival_date": str(arrival_date),
        "origin_country": origin_country,
        "transport_mode": transport_mode,
        "status": "waiting",
        "assigned_driver": None,
        "created_at": datetime.utcnow()
    })
    st.success("Family registered and waiting 🚦")

# -----------------------------
# 2) DRIVER AREA
# -----------------------------
st.divider()
st.header("🚗 Driver Area")

driver_name = st.text_input("Driver name")

if driver_name:
    st.subheader("🕒 Families waiting for pickup")

    waiting_families = list(collection.find({"status": "waiting"}))

    if not waiting_families:
        st.info("No families waiting")

    for fam in waiting_families:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(
                f"👨‍👩‍👧 {fam['last_name']} "
                f"({fam['number_of_people']} people) "
                f"| Arrival: {fam['arrival_date']}"
            )
        with col2:
            if st.button("Assign", key=str(fam["_id"])):
                collection.update_one(
                    {"_id": fam["_id"]},
                    {"$set": {
                        "status": "assigned",
                        "assigned_driver": driver_name
                    }}
                )
                st.rerun()

    st.subheader("📋 My assigned families")

    my_families = list(
        collection.find({
            "assigned_driver": driver_name,
            "status": "assigned"
        })
    )

    for fam in my_families:
        if st.button(
            f"Picked up {fam['last_name']}",
            key=f"pickup_{fam['_id']}"
        ):
            collection.update_one(
                {"_id": fam["_id"]},
                {"$set": {"status": "picked_up"}}
            )
            st.success("Family picked up ✅")
            st.rerun()