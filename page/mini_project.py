import plotly.express as px
import streamlit as st

from core.theme import KEMENKEU_BLUE, KEMENKEU_GOLD
from services.dummy_data import generate_dummy_kpi_data
from ui.widgets import show_banner


def render() -> None:
    show_banner(
        "Mini Project: Dashboard Layanan (Dummy Data)",
        "Contoh struktur project yang siap dipakai sebagai latihan capstone.",
    )

    data = generate_dummy_kpi_data()

    st.sidebar.subheader("Filter Dashboard")
    unit_filter = st.sidebar.multiselect("Unit", sorted(data["unit"].unique()), default=sorted(data["unit"].unique()))
    layanan_filter = st.sidebar.multiselect(
        "Layanan",
        sorted(data["layanan"].unique()),
        default=sorted(data["layanan"].unique())[:3],
    )

    filtered = data[(data["unit"].isin(unit_filter)) & (data["layanan"].isin(layanan_filter))]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Permohonan", f"{filtered['jumlah_permohonan'].sum():,}")
    c2.metric("Avg Success", f"{filtered['success_rate'].mean():.1%}")
    c3.metric("Avg SLA", f"{filtered['rata_menit'].mean():.1f} menit")
    c4.metric("Avg Kepuasan", f"{filtered['skor_kepuasan'].mean():.2f}/5")

    left, right = st.columns([1.2, 1])
    with left:
        fig_tren = px.area(
            filtered.groupby("tanggal", as_index=False)["jumlah_permohonan"].sum(),
            x="tanggal",
            y="jumlah_permohonan",
            title="Tren Permohonan Harian",
            color_discrete_sequence=[KEMENKEU_BLUE],
        )
        st.plotly_chart(fig_tren, use_container_width=True)

    with right:
        fig_unit = px.bar(
            filtered.groupby("unit", as_index=False)["jumlah_permohonan"].sum(),
            x="unit",
            y="jumlah_permohonan",
            title="Kontribusi per Unit",
            color_discrete_sequence=[KEMENKEU_GOLD],
        )
        st.plotly_chart(fig_unit, use_container_width=True)

    with st.expander("Lihat data detail"):
        st.dataframe(filtered, use_container_width=True)
        st.download_button(
            "Download CSV hasil filter",
            data=filtered.to_csv(index=False).encode("utf-8"),
            file_name="dashboard_layanan_dummy.csv",
            mime="text/csv",
        )
