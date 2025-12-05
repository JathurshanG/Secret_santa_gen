import streamlit as st
import time
from pymongo import MongoClient

st.set_page_config(page_title="Ton Tirage 🎁", page_icon="🎄")

# ---------------------------------------------------------
# 1️⃣ Vérification de la session utilisateur
# ---------------------------------------------------------
if "user" not in st.session_state:
    st.error("⚠️ Tu dois te connecter d'abord.")
    st.switch_page("app.py")
    st.stop()

user = st.session_state["user"]


# ---------------------------------------------------------
# 2️⃣ Connexion MongoDB (cache pour vitesse ⚡)
# ---------------------------------------------------------
@st.cache_resource
def get_db():
    client = MongoClient(st.secrets["MONGO_URI"])
    return client["secret_santa"]

db = get_db()
draws = db["draws"]


# ---------------------------------------------------------
# 3️⃣ TIMER DE DÉCONNEXION (30 secondes)
# ---------------------------------------------------------
if "login_time" not in st.session_state:
    st.session_state.login_time = time.time()

elapsed = time.time() - st.session_state.login_time

if elapsed > 30:
    st.session_state.clear()
    st.switch_page("app.py")
    st.stop()

remaining = int(30 - elapsed)
st.info(f"⏳ Cette page expirera dans {remaining} secondes.")


# ---------------------------------------------------------
# 4️⃣ INFOS DE L'ÉVÉNEMENT 🎄
# ---------------------------------------------------------
DATE = "Samedi 23 Décembre 2025"
LIEU = """ 32 Av Gambetta,
           Livry-Gargan
       """
HEURE = "19h30"
BUDGET = "50€"

st.markdown(
    f"""
    <div style="padding:15px; border-radius:10px; background-color:#e8f5e9; border:1px solid #c8e6c9; margin-bottom:20px;">
        <h2 style="text-align:center;">🎄 Secret Santa 2025 🎁</h2>
        <p style="text-align:center; font-size:18px;">
            <b>📅 Date :</b> {DATE}<br>
            <b>📍 Lieu :</b> {LIEU}<br>
            <b>🕒 Heure :</b> {HEURE}<br>
            <b>💸 Budget :</b> {BUDGET}<br><br>
            Prépare ton cadeau et garde ton tirage secret 🤫✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# 5️⃣ Récupération du tirage depuis MongoDB
# ---------------------------------------------------------
if "receiver" not in st.session_state:
    doc = draws.find_one({"giver": user})
    if not doc:
        st.error("❌ Aucun tirage trouvé pour toi.")
        st.stop()
    st.session_state.receiver = doc["receiver"]

receiver = st.session_state.receiver


# ---------------------------------------------------------
# 6️⃣ AFFICHAGE DU TIRAGE
# ---------------------------------------------------------
st.markdown(
    f"""
    <h1 style="text-align:center;">🎁 Ton Tirage, {user} ✨</h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    f"""
    <div style='text-align:center; font-size:26px;'>
        🎁 <b>Tu offres un cadeau à :</b><br><br>
        <span style='font-size:40px;'>✨ {receiver} ✨</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.success("🤫 Garde ton tirage secret !")


# ---------------------------------------------------------
# 7️⃣ Bouton Déconnexion
# ---------------------------------------------------------
if st.button("Se déconnecter"):
    st.session_state.clear()
    st.switch_page("app.py")
