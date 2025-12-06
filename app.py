import streamlit as st
import hashlib
from pymongo import MongoClient

st.set_page_config(page_title="Secret Santa 🎄", page_icon="🎁")


# -----------------------------
# CACHE MONGO
# -----------------------------
@st.cache_resource
def get_db():
    client = MongoClient(st.secrets["MONGO_URI"])
    return client["secret_santa"]

db = get_db()
users = db["users"]

# -----------------------------
# PASSWORD CHECK
# -----------------------------
def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def check_login(name, pwd):
    hashed = hash_password(pwd)
    return users.find_one({"name": name, "password_hash": hashed}) is not None


import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
/* Supprime la sidebar */
section[data-testid="stSidebar"] {
    display: none;
}

/* Supprime le bouton pour ouvrir la sidebar */
button[kind="header"] {
    display: none;
}

/* Supprime le menu ☰ */
#MainMenu {
    visibility: hidden;
}

/* Supprime le footer "Made with Streamlit" */
footer {
    visibility: hidden;
}

/* Supprime le header */
header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# UI LOGIN
# -----------------------------
st.title("🎄 Secret Santa  🎁",text_alignment='center')
# Liste des prénoms autorisés
PRENOMS = [
    "Danusa", "Rathusan", "Tevisha",
    "Nevatha", "Nithurshan", "Suren",
    "Nihithan", "Diluxmi", "Keerthan",
    "Jathurshan"
]
st.markdown("""### ###""")
name = st.selectbox("Sélectionne ton prénom :", PRENOMS)

pwd = st.text_input("Mot de passe", type="password")

if st.button("Connexion"):
    if check_login(name, pwd):
        st.session_state["user"] = name
        st.switch_page("pages/tirage.py")

    else:
        st.error("❌ Mauvais mot de passe ou prénom.")
