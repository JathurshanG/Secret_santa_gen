import io
from textwrap import dedent

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Liste des invités", page_icon="🪑", layout="wide")

RAW_DATA = dedent(
    """
    Guests\tSEATS\tFamille
    Sinna Maama\tCOACH\tJeyam
    Gowri Maami\tCOACH\tJeyam
    Keshini\tCOACH\tJeyam
    Palan Maha\tCOACH\tJeypalan
    Ranji\tCOACH\tJeypalan
    Babeeshan\tCOACH\tJeypalan
    Mathusa\tCOACH\tJeypalan
    Shagee\tCOACH\tJeypalan
    Maama\tCOACH\tSriskandarajah
    Pirakash\tPirakash\tSriskandarajah
    Nithurshan\tCOACH\tSriskandarajah
    Jeyanthi\tCOACH\tSriskandarajah
    Sritharan\tCOACH\tSritharan
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
    Sutha\tCOACH\tSuthajini
    Kones\tCOACH\tSuthajini
    Sneha\tCOACH\tVathani
    Viji\tCOACH\tVijitha
    Dilakshan\tCOACH\tVijitha
    Sajeevan\tCOACH\tVijitha
    Dinsy\tCOACH\tVijitha
    Vannu\tCOACH\tSuthi
    Suthi\tCOACH\tSuthi
    Palan Kandasamy\tCOACH\tSuthi
    Ranjana\tCOACH\tRanjana
    Sathees\tCOACH\tSathees
    Sathees 1\tCOACH\tSathees
    Sathees 2\tCOACH\tSathees
    Sathees 3\tCOACH\tSathees
    Sathees 4\tCOACH\tSathees
    Aunthy\tCOACH\tSivapalan
    Clinton\tCOACH\tRancy
    Sierra\tCOACH\tRancy
    Vimala\tCOACH\tRancy
    """
).strip()


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(RAW_DATA), sep="\t")
    df.columns = ["Guest", "Accommodation", "Family"]
    return df


def main() -> None:
    df = load_data()

    st.title("Filtre par accommodation")

    accommodations = sorted(df["Accommodation"].unique())
    selected_accommodation = st.selectbox("Choisir accommodation", accommodations)

    filtered = df[df["Accommodation"] == selected_accommodation]

    st.write(f"Nombre d'invités: {len(filtered)}")
    st.dataframe(filtered, use_container_width=True)


if __name__ == "__main__":
    main()
