import time
from datetime import date, timedelta

import streamlit as st

from services.dummy_data import generate_dummy_kpi_data, slow_aggregate
from ui.widgets import show_banner


def render() -> None:
    show_banner(
        "State, Form, dan Cache",
        "Fondasi agar app stabil, cepat, dan tidak membingungkan saat interaksi meningkat.",
    )

    if "klik_counter" not in st.session_state:
        st.session_state.klik_counter = 0

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Session State")
        if st.button("Tambah counter"):
            st.session_state.klik_counter += 1
        st.write(f"Counter saat ini: **{st.session_state.klik_counter}**")

    with col2:
        st.subheader("Form submit")
        with st.form("form_rencana_proyek"):
            nama = st.text_input("Nama proyek", value="monitoring-layanan-kemenkeu")
            target_user = st.selectbox("Target user", ["Analis", "Pejabat", "Pelaksana", "Publik Internal"])
            deadline = st.date_input("Target rilis", value=date.today() + timedelta(days=21))
            submit = st.form_submit_button("Simpan rencana")
        if submit:
            st.success(f"Rencana tersimpan: {nama} untuk {target_user}, target {deadline}.")

    st.subheader("Cache data")
    data = generate_dummy_kpi_data()
    group_by = st.radio("Agregasi berdasarkan", ["unit", "layanan"], horizontal=True)

    t0 = time.time()
    agg = slow_aggregate(data, group_by)
    duration = time.time() - t0

    st.caption(f"Waktu proses: {duration:.2f}s (pemanggilan kedua akan jauh lebih cepat karena cache).")
    st.dataframe(agg, use_container_width=True)
