import streamlit as st

from ui.widgets import show_banner


def render() -> None:
    show_banner(
        "Pelatihan Project Deployment dengan Streamlit",
        "Alur belajar: Dasar → Widget → State/Form/Cache → Integrasi Endpoint → Deployment",
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Durasi Setup", "< 10 menit")
    with col2:
        st.metric("Baris kode app awal", "± 20")
    with col3:
        st.metric("Target", "App online + AI")

    st.markdown("### Kenapa Streamlit efektif untuk unit Analis Data?")
    st.markdown(
        """
        - Cepat membuat dashboard internal berbasis data.
        - Mudah untuk prototyping use-case analitik dan AI.
        - Bisa dihubungkan ke model endpoint lokal maupun cloud.
        - Deployment bisa bertahap: local, cloud sederhana, sampai container.
        """
    )

    st.markdown("### Peta Modul Pelatihan")
    st.info(
        "1) Streamlit Dasar  •  2) Widget Penting  •  3) State/Form/Cache  •  "
        "4) Dashboard Dummy  •  5) Endpoint LLM  •  6) Deployment"
    )
