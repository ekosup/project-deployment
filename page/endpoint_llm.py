import time

import requests
import streamlit as st

from services.llm import call_generic_endpoint, dummy_llm_response
from ui.widgets import show_banner
from utils.ollama_client import OllamaError, DEFAULT_OLLAMA_HOST, generate_text, list_models


def render() -> None:
    show_banner(
        "Integrasi Endpoint Model / LLM",
        "Dari dummy mode, ke Ollama lokal, sampai generic REST endpoint.",
    )

    mode = st.radio(
        "Mode integrasi",
        ["Dummy (latihan peserta)", "Ollama (lokal)", "Generic REST endpoint"],
        horizontal=True,
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    _render_endpoint_config_panel()

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Tulis prompt... (contoh: berikan rekomendasi untuk meningkatkan SLA)")
    if not prompt:
        st.caption("Saran: mulai dari mode Dummy dulu, lalu lanjut ke Ollama atau endpoint API nyata.")
        return

    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Memproses respons model..."):
            try:
                if mode == "Dummy (latihan peserta)":
                    time.sleep(0.6)
                    answer = dummy_llm_response(prompt)
                elif mode == "Ollama (lokal)":
                    ollama_host = st.session_state.get("ollama_host", DEFAULT_OLLAMA_HOST)
                    model_options = list_models(ollama_host)
                    model = model_options[0] if model_options else "llama3.2"
                    answer = generate_text(prompt=prompt, model=model, host=ollama_host)
                else:
                    url = st.session_state.get("generic_endpoint_url", "")
                    if not url.strip():
                        raise ValueError("Isi URL endpoint terlebih dahulu di panel konfigurasi.")
                    api_key = st.session_state.get("generic_api_key", "")
                    timeout = int(st.session_state.get("generic_timeout", 45))
                    answer = call_generic_endpoint(url=url, prompt=prompt, api_key=api_key, timeout=timeout)
            except (OllamaError, requests.RequestException, ValueError) as exc:
                answer = f"Error integrasi endpoint: {exc}"

        st.markdown(answer)

    st.session_state.chat_history.append({"role": "assistant", "content": answer})


def _render_endpoint_config_panel() -> None:
    with st.expander("Panel konfigurasi endpoint", expanded=False):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Ollama Host", value=DEFAULT_OLLAMA_HOST, key="ollama_host")
            st.number_input("Generic timeout (detik)", min_value=5, max_value=180, value=45, key="generic_timeout")
        with c2:
            st.text_input(
                "Generic endpoint URL",
                placeholder="https://your-api.example.com/generate",
                key="generic_endpoint_url",
            )
            st.text_input(
                "API key (opsional, simpan di secrets/env untuk production)",
                type="password",
                key="generic_api_key",
            )

        st.code(
            """# .streamlit/secrets.toml
GENERIC_API_URL = "https://..."
GENERIC_API_KEY = "xxxx"

# akses di app
# st.secrets["GENERIC_API_KEY"]
""",
            language="toml",
        )
