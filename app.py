import streamlit as st

st.set_page_config(
    page_title="Family Pickup App",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align: center;'>Family Pickup Management</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="max-width: 700px; margin: auto; text-align: justify;">
        <p>
        This application helps manage family pickups.
        Families are registered in advance, and drivers can assign themselves
        to a pickup and track what has already been done in real time.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
col1, col2,col3 = st.columns(3)

with col1:
    if st.button("Family Registration", use_container_width=True):
        st.switch_page("pages/family.py")

with col2:
    if st.button("Driver Dashboard", use_container_width=True):
        st.switch_page("pages/driver.py")

with col3:
    if st.button("See Details", use_container_width=True):
        st.switch_page("pages/history.py")
