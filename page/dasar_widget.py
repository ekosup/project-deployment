import plotly.express as px
import streamlit as st

from services.dummy_data import generate_dummy_kpi_data
from ui.widgets import show_banner


def render() -> None:
    show_banner(
        "Modul Dasar dan Widget Penting",
        "Peserta belajar 1 per 1 widget, lalu langsung praktik dengan mini-lab.",
    )

    data = generate_dummy_kpi_data()
    tab_quick, tab_input, tab_opsi, tab_layout = st.tabs(
        ["Quick Win", "Input", "Pilihan & Aksi", "Layout"]
    )

    with tab_quick:
        st.subheader("Quick Win: 20 baris jadi dashboard")
        st.dataframe(data.head(10), use_container_width=True)
        fig = px.line(
            data.groupby("tanggal", as_index=False)["jumlah_permohonan"].sum(),
            x="tanggal",
            y="jumlah_permohonan",
            markers=True,
            title="Jumlah Permohonan Harian (Dummy)",
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab_input:
        st.subheader("Widget input dasar")
        nama_kelas = st.text_input("Nama peserta", value="Peserta A")
        target_proyek = st.text_area("Target proyek setelah pelatihan", value="Dashboard monitoring layanan")
        jumlah_tim = st.number_input("Jumlah anggota tim", min_value=1, max_value=30, value=5)
        st.success(f"Halo {nama_kelas}! Target: {target_proyek}. Tim: {jumlah_tim} orang.")

    with tab_opsi:
        st.subheader("Widget pilihan + aksi")
        unit = st.selectbox("Pilih unit", ["DJP", "DJBC", "DJPb", "DJKN", "BPPK", "Itjen"])
        layanan = st.multiselect(
            "Pilih layanan prioritas",
            ["SPT Tahunan", "NPWP", "Billing", "Lelang", "Perbendaharaan", "Konsultasi"],
            default=["SPT Tahunan", "Billing"],
        )
        rentang = st.slider("Target SLA (menit)", min_value=5, max_value=120, value=(20, 60))
        setuju = st.checkbox("Saya paham konsep rerun Streamlit")

        if st.button("Generate ringkasan", type="primary"):
            st.write(
                {
                    "unit": unit,
                    "layanan_prioritas": layanan,
                    "sla_menit": rentang,
                    "siap_lanjut": setuju,
                }
            )

    with tab_layout:
        st.subheader("Layout: columns, expander, sidebar")
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown("#### Area Utama")
            st.line_chart(data.groupby("tanggal")["success_rate"].mean())
        with c2:
            st.markdown("#### Ringkasan")
            st.metric("Rata success rate", f"{data['success_rate'].mean():.1%}")
            st.metric("Rata kepuasan", f"{data['skor_kepuasan'].mean():.2f}")

        with st.expander("Panduan peserta"):
            st.write(
                "Coba ubah satu widget setiap kali (misalnya slider atau selectbox), "
                "lalu amati perubahan output agar alur interaktif Streamlit lebih mudah dipahami."
            )
