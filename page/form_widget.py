from ui.widgets import banner
import pandas as pd
import streamlit as st

from services import (
    DEFAULT_MESSAGE_API_BASE_URL,
    MessageService,
    MessageServiceError,
)


def render() -> None:
    banner(
        "Form Widget",
        "Demo form untuk mengirim dan mengambil data dari endpoint say-hello.",
    )

    service = MessageService(
        base_url='https://training.ekos.my.id',
        api_key='AUytx9bbpnpPTjfQtVfmp2FUpSSaAJs1UGZgUQp0IG8',
        timeout=30
    )

    st.write(service.get_messages())

    with st.form('form_submit_message'):
        name = st.text_input('Name')
        message = st.text_input('Message')
        submit = st.form_submit_button('Kirim pesan')

    if not submit:
        return

    try:
        response = service.post_message(nama=name, message=message)
    except MessageServiceError as err:
        st.error(f"Gagal kirim message: {err}")
        return
    
    

        