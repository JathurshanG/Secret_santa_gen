import streamlit as st

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="MAHA TRANSPORT",
    layout="wide"
)

# --------------------------------------------------
# Hide Streamlit sidebar ONLY
# (on garde le header interne pour stabilité)
# --------------------------------------------------
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Custom top bar (visual only)
# --------------------------------------------------


# --------------------------------------------------
# REAL navigation (Streamlit buttons)
# --------------------------------------------------
nav1, nav2, nav3,nav4 = st.columns(4)

with nav1:
    st.markdown(
    """
    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:16px 32px;
        border-bottom:1px solid #eee;
        margin-bottom:32px;
    ">
        <div style="font-size:22px; font-weight:700;">
            MAHA TRANSPORT
        </div>
    </div>
    """,
    unsafe_allow_html=True
)   

# --------------------------------------------------
# Home content
# --------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>Family Pickup Management</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="max-width:700px; margin:auto; text-align: justify;">
        <p>
        This application helps manage family pickups.
        Families are registered in advance, and drivers can assign
        themselves to available convoys and track completed ones
        in real time.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Call-to-action buttons
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Family Registration", use_container_width=True):
        st.switch_page("pages/family.py")

with c2:
    if st.button("Driver Dashboard", use_container_width=True):
        st.switch_page("pages/driver.py")

with c3:
    if st.button("See Details", use_container_width=True):
        st.switch_page("pages/history.py")