import streamlit as st
from views.family import show_family

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
    st.title("🚐 MAHA TRANSPORT")
    page = st.radio(
        "Navigation",
        ["Home", "Family registration", "Drivers", "Dashboard"]
    )

# --------------------------------------------------
# Page routing
# --------------------------------------------------
if page == "Home":
    show_home()

elif page == "Family registration":
    show_family()

else:
    st.title("🚧 Coming soon")
    st.info("This section is under construction.")
    st.components.v1.html("""
            div class="tenor-gif-embed" data-postid="9395077867143719278" data-share-method="host" data-aspect-ratio="0.763889" data-width="100%"><a href="https://tenor.com/view/vip-dhanush-bye-vip-dhanush-tata-vip-tata-vip-bye-dhanush-tata-gif-9395077867143719278">Vip Dhanush Bye Vip Dhanush Tata GIF</a>from <a href="https://tenor.com/search/vip+dhanush+bye-gifs">Vip Dhanush Bye GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
            """)