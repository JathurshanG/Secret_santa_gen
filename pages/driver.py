import os
import streamlit as st
import pandas as pd
from pymongo import MongoClient
from bson import ObjectId

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
    page_title="Driver Dashboard",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align:center;'>🚗 Driver Dashboard</h1>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Allowed drivers (LIMITED LIST)
# --------------------------------------------------
DRIVERS = [
    "Pirakash",
    "Keerthan",
    "Suren",
    "Dila",
    "Nevatha",
    "Nithur",
    "Nihi"
]

driver_name = st.selectbox(
    "Select your name",
    [""] + DRIVERS
)

if not driver_name:
    st.info("Please select your name to see available convoys.")
    st.stop()

# --------------------------------------------------
# Load ONLY available convoys
# --------------------------------------------------
families = list(collection.find({"status": "waiting"}))

if not families:
    st.success("No available convoys 🎉")
    st.stop()

# --------------------------------------------------
# Build DataFrame
# --------------------------------------------------
df = pd.DataFrame({
    "ID": [str(f["_id"]) for f in families],
    "Family": [f["family_name"] for f in families],
    "People": [f["number_of_people"] for f in families],
    "Arrival": [f["arrival_date"] for f in families],
    "Departure": [f.get("departure_date") or "" for f in families],
    "Transport": [f["transport_mode"] for f in families],
    "Extra": [f.get("extra") or "" for f in families],
    "Take": [False for _ in families]
})

# --------------------------------------------------
# Display table with tick
# --------------------------------------------------
edited_df = st.data_editor(
    df,
    use_container_width=True,
    hide_index=True,
    disabled=[
        "Family",
        "People",
        "Arrival",
        "Departure",
        "Transport",
        "Extra"
    ]
)

# --------------------------------------------------
# Process assignment
# --------------------------------------------------
for i, row in edited_df.iterrows():

    if row["Take"]:
        result = collection.update_one(
            {
                "_id": ObjectId(row["ID"]),
                "status": "waiting"   # sécurité anti-doublon
            },
            {
                "$set": {
                    "assigned_driver": driver_name,
                    "status": "assigned"
                }
            }
        )

        if result.modified_count == 1:
            st.success(
                f"Convoy '{row['Family']}' assigned to {driver_name} ✅"
            )
        else:
            st.warning(
                f"Convoy '{row['Family']}' was already taken."
            )

        st.rerun()