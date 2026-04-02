import io
import pandas as pd
import streamlit as st


RAW_DATA = """Guests\tSEATS\tFamille
Sinna Maama\tCOACH\tJeyam
Gowri Maami\tCOACH\tJeyam
Keshini\tCOACH\tJeyam
Baba\tVan\tJeyam
Anojan\tVan\tJeyam
Palan Maha\tCOACH\tJeypalan
Ranji\tCOACH\tJeypalan
Babeeshan\tCOACH\tJeypalan
Mathusa\tCOACH\tJeypalan
Shagee\tCOACH\tJeypalan
Maama\tCOACH\tSriskandarajah
Maami\tSuren\tSriskandarajah
Pirakash\tPirakash\tSriskandarajah
Nithurshan\tCOACH\tSriskandarajah
Nevatha\tSuren\tSriskandarajah
Suren\tSuren\tSriskandarajah
Nylan\tSuren\tSriskandarajah
Jeyanthi\tCOACH\tSriskandarajah
Sritharan\tCOACH\tSritharan
Karthigan\tVan\tSritharan
Shayini\tKi2\tSritharan
Nea\tKi2\tSritharan
Divani\tKi2\tSritharan
Deenu\tKi2\tSritharan
Kiru\tKi2\tSritharan
Seelan\tCOACH\tJeyseelan
Tadja\tCOACH\tJeyseelan
Kasturi\tCOACH\tJeyseelan
Mathuri\tCOACH\tJeyseelan
Kabi\tCOACH\tJeyseelan
Nagules\tCOACH\tNagulesweran
Priya Nagules\tCOACH\tNagulesweran
Thagsan\tPirakash\tNagulesweran
Janushan\tPirakash\tNagulesweran
Paranthaman\tCOACH\tParanthaman
Theepan\tCOACH\tPirathipan
Jeyanthi\tCOACH\tPirathipan
Vibishan\tCOACH\tPirathipan
Mathaan\tCOACH\tMatanmohan
Mithilan\tPirakash\tMatanmohan
Tharon\tPirakash\tMatanmohan
Aruni\tCOACH\tMatanmohan
Femme Mathaan\tCOACH\tMatanmohan
Jeyanthi 3\tLivry\tSubodoran
Tharsana\tLivry\tSubodoran
Akaliaah\tLivry\tSubodoran
Sutha\tCOACH\tSuthajini
Kones\tCOACH\tSuthajini
Sneha\tCOACH\tVathani
Assai appa\tAASSAI\tTharumu
Assai Amma\tAASSAI\tTharumu
Assai Son\tAASSAI\tTharumu
Assai Son\tAASSAI\tTharumu
Assai Son\tAASSAI\tTharumu
Viji\tCOACH\tVijitha
Dilakshan\tCOACH\tVijitha
Sajeevan\tCOACH\tVijitha
Dinsy\tCOACH\tVijitha
Vannu\tCOACH\tSuthi
Suthi\tCOACH\tSuthi
Palan Kandasamy\tCOACH\tSuthi
Ranjana\tCOACH\tRanjana
Visakan\tVan\tGuna
Prathees\tVan\tGuna
Sathees\tCOACH\tSathees
Sathees 1\tCOACH\tSathees
Sathees 2\tCOACH\tSathees
Sathees 3\tCOACH\tSathees
Sathees 4\tCOACH\tSathees
Keerthan\tKeerthan\tKeerthan
Kayden\tKeerthan\tKeerthan
Dhyann\tKeerthan\tKeerthan
Jalaa\tLivry\tJalaa
Krishny\tLivry\tJalaa
Muhundan\tLivry\tJalaa
Velmuran\tLivry\tVelmurugan
Tevaki\tLivry\tVelmurugan
Papa de Keerthan\tKeerthan\tKeerthan
Periyamma de suren\tSuren\tSriskandarajah
Aunthy\tCOACH\tSivapalan
Clinton\tCOACH\tRancy
Sierra\tCOACH\tRancy
Vimala\tCOACH\tRancy
"""

def load_data():
    df = pd.read_csv(io.StringIO(RAW_DATA), sep="\t")
    df.columns = ["Guest", "Accommodation", "Family"]
    return df

def main():
    st.title("Passengers by Accommodation")

    df = load_data()

    # liste des accommodations
    accommodations = sorted(df["Accommodation"].unique())

    # sélection
    selected = st.selectbox("Choose accommodation", accommodations)

    # filtre
    filtered = df[df["Accommodation"] == selected]

    # affichage simple
    st.write(f"Passengers in {selected}:")
    for guest in filtered["Guest"]:
        st.write(f"- {guest}")

if __name__ == "__main__":
    main()
