import os
import streamlit as st
from pymongo import MongoClient
from datetime import datetime

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
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Family Registration",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align:center;'> Family Registration</h1>",
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

    family_name = st.text_input("Family name (Last name & First name)")
    number_of_people = st.number_input("Number of people", min_value=1)

    arrival_date = st.date_input("Arrival date")

    departure_date = st.date_input("Departure date", key="dep_
    
    import streamlit as st

transport_mode = st.selectbox(
    "Mode of transport",
    ["Plane", "Boat", "Bus", "Car", "Other"]
)

extra = None
if transport_mode == "Plane":
    extra = st.text_input(
        "Extra information (required)",
        placeholder="e.g. Terminal 2E – Paris Charles de Gaulle (CDG)"
    )

if st.button("Submit"):
    if transport_mode == "Plane" and not extra:
        st.error("Extra information is required when transport mode is Plane.")
    else:
        st.success("Form submitted successfully!")
        st.write("Transport:", transport_mode)
        st.write("Extra:", extra)
    # ✅ OBLIGATOIRE
    
    submit = st.form_submit_button("Save family")
# --------------------------------------------------
# Insert into MongoDB
# --------------------------------------------------
if submit:

    if not family_name:
        st.warning("Please enter the family name.")
    else:
        collection.insert_one({
            "family_name": family_name,
            "number_of_people": number_of_people,
            "arrival_date": str(arrival_date),
            "departure_date": str(departure_date) if departure_date else None,
            "transport_mode": transport_mode,
            "extra": extra,
            "status": "waiting",
            "assigned_driver": None,
            "created_at": datetime.utcnow()
        })

        st.success("Family successfully registered ✅")