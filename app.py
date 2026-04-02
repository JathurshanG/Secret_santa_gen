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

    # nettoyage minimum
    df["Guest"] = df["Guest"].str.strip()
    df["Accommodation"] = df["Accommodation"].str.strip()
    df["Family"] = df["Family"].str.strip()

    return df


def main():
    st.set_page_config(page_title="Accommodation Filter", layout="centered")

    df = load_data()

    st.title("Accommodation Filter")

    # filtre
    accommodations = sorted(df["Accommodation"].unique())
    selected = st.radio("Select accommodation", accommodations)

    filtered = df[df["Accommodation"] == selected]

    # affichage
    st.write(f"Guests: {len(filtered)}")
    st.dataframe(filtered, use_container_width=True)

    # stats
    st.subheader("Distribution")
    st.bar_chart(df["Accommodation"].value_counts())

    # debug data (important)
    st.subheader("⚠️ Data issues")

    duplicates = df[df.duplicated("Guest", keep=False)]
    if not duplicates.empty:
        st.write("Duplicate names:")
        st.dataframe(duplicates)

    weird_values = df[
        df["Accommodation"].str.lower().isin(df["Guest"].str.lower())
    ]

    if not weird_values.empty:
        st.write("⚠️ Accommodation looks like a person name:")
        st.dataframe(weird_values)


if __name__ == "__main__":
    main()
