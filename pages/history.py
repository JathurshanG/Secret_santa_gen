import os
import streamlit as st
import pandas as pd
from pymongo import MongoClient

# --------------------------------------------------
# MongoDB connection
# --------------------------------------------------
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    st.error("MONGO_URI not found.")
    st.stop()

client = MongoClient(MONGO_URI)
collection = client["family_management"]["families"]

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Convoy History",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align:center;'>📋 Convoy History</h1>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Search / Filter section
# --------------------------------------------------
st.subheader("🔍 Search & Filters")

col1, col2 = st.columns(2)

with col1:
    search_family = st.text_input(
        "Search by family name",
        placeholder="Smith – Ali"
    )

with col2:
    search_driver = st.selectbox(
        "Filter by driver",
        ["All", "Pirakash", "Keerthan", "Suren", "Dila", "Nevatha", "Nithur", "Nihi"]
    )

# --------------------------------------------------
# Load all convoys
# --------------------------------------------------
families = list(collection.find())

if not families:
    st.info("No convoys found.")
    st.stop()

df = pd.DataFrame({
    "Family": [f["family_name"] for f in families],
    "People": [f["number_of_people"] for f in families],
    "Arrival": [f["arrival_date"] for f in families],
    "Departure": [f.get("departure_date") or "" for f in families],
    "Transport": [f["transport_mode"] for f in families],
    "Extra": [f.get("extra") or "" for f in families],
    "Status": [f["status"] for f in families],
    "Driver": [f.get("assigned_driver") or "" for f in families],
})

# --------------------------------------------------
# Apply filters
# --------------------------------------------------
if search_family:
    df = df[df["Family"].str.contains(search_family, case=False, na=False)]

if search_driver != "All":
    df = df[df["Driver"] == search_driver]

# --------------------------------------------------
# Display table
# --------------------------------------------------
st.dataframe(
    df,
    use_container_width=True
)