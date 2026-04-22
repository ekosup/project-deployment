import streamlit as st


def show_banner(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="kemenkeu-banner">
            <h3 style="margin:0; color:white;">{title}</h3>
            <p style="margin:0.25rem 0 0 0; opacity:0.95;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
