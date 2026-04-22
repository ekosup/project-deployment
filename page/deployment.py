import streamlit as st

from ui.widgets import show_banner


def render() -> None:
    show_banner(
        "Modul Deployment",
        "Dari local ke cloud dengan checklist yang jelas dan mudah diikuti peserta.",
    )

    st.markdown("### Checklist minimal project")
    st.code(
        """.
├── app.py
├── page/
├── services/
├── ui/
├── core/
├── data/
├── requirements.txt / pyproject.toml
└── .streamlit/
    └── secrets.toml  # jangan commit ke git
"""
    )

    st.markdown("### Opsi 1 (cepat): Streamlit Community Cloud")
    st.markdown(
        "1. Push repo ke GitHub.\n"
        "2. Buat app di Streamlit Cloud.\n"
        "3. Set secret dari dashboard cloud.\n"
        "4. Deploy dan uji endpoint."
    )

    st.markdown("### Opsi 2 (production mindset): Docker")
    st.code(
        """# Dockerfile ringkas
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -U pip && pip install .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
""",
        language="dockerfile",
    )

    st.info(
        "Jika deployment gagal, cek kembali dependency, versi Python, dan konfigurasi secrets. "
        "Lakukan perbaikan bertahap lalu deploy ulang."
    )
