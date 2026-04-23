from ui.widgets import banner
import streamlit as st
import pandas as pd


def make_upper(text: str) -> str:
    return text.upper()


def render() -> None:
    banner(
        "Modul Dasar dan Widget",
        "Building blocks untuk membuat aplikasi interaktif dengan Streamlit: teks, tombol, input, dan media.",
    )

    name = st.text_input(
        label='Nama',
        value=''
    )

    office_date = st.date_input(
        'Tanggal masuk kantor'
    )

    st.write(
        f"Nama saya __{make_upper(name)}__, saya pertama kali bekerja pada __{office_date}__"
    )

    show_data = st.button('Show data')
    hide_data = st.button('Hide data')

    def hide_data():
        show_data = False

    if show_data:
        df = pd.DataFrame({'a': [12,12,14], 'b':[1,2,3]})
        st.write(df)

    if hide_data:
        hide_data()

    bulan = st.multiselect(
        'Bulan',
        ['Jan', 'Feb', 'Mar']
    )

    st.write(bulan)

    st.divider()

    sample_data = st.file_uploader('Sample data')

    df_sample = pd.DataFrame()

    if sample_data:
        df_sample = pd.read_csv(sample_data)
        
        df_edited = st.data_editor(df_sample)
    
        st.download_button(
            "Unduh data (csv)",
            df_edited.to_csv(),
            'edited_data.csv',
        )

    st.divider()

    a, b, c = st.columns(3)

    with a:
        st.write("Ini kolom 1")

    with b:
        st.button(
            'Ini tombol 1',
            width='stretch'
        )
    
    with c:
        st.dataframe(df_sample)