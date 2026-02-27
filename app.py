import streamlit as st
from views.family import show_family

# --------------------------------------------------
# Session state init (TOUT EN HAUT)
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "nav_target" not in st.session_state:
    st.session_state.nav_target = None


# --------------------------------------------------
# Sync navigation request (AVANT widgets)
# --------------------------------------------------
if st.session_state.nav_target:
    st.session_state.page = st.session_state.nav_target
    st.session_state.nav_target = None


# --------------------------------------------------
# Home page
# --------------------------------------------------
def show_home():
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

    st.markdown("<br><br>", unsafe_allow_html=True)

    _, c2, _ = st.columns(3)
    with c2:
        if st.button("Register a family", use_container_width=True):
            st.session_state.nav_target = "Family registration"
            st.rerun()


# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="MAHA TRANSPORT",
    layout="wide"
)

# --------------------------------------------------
# Sidebar navigation (SOURCE UNIQUE)
# --------------------------------------------------
with st.sidebar:
    st.title("MAHA TRANSPORT")
    st.radio(
        "Navigation",
        ["Home", "Family registration", "Drivers", "Dashboard"],
        key="page"
    )

# --------------------------------------------------
# Page routing
# --------------------------------------------------
if st.session_state.page == "Home":
    show_home()

elif st.session_state.page == "Family registration":
    show_family()

else:
    st.title("🚧 Coming soon")
    st.info("This section is under construction.")
    