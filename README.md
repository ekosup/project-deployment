# Streamlit Kelas Praktik (Example Branch)

Repo ini adalah versi **contoh lengkap** untuk demo pengajar.
Isinya sudah menampilkan alur materi, dummy data, mini dashboard, dan integrasi endpoint dasar.

## Alur Belajar Bit by Bit

1. `app.py` → pahami cara `st.navigation` bekerja.
2. `core/theme.py` → lihat setup tema Kemenkeu.
3. `ui/widgets.py` → kenali komponen UI reusable (`show_banner`).
4. `page/dasar_widget.py` → widget inti Streamlit.
5. `page/state_form_cache.py` → session state, form, cache.
6. `page/mini_project.py` → mini dashboard end-to-end.
7. `page/endpoint_llm.py` → integrasi endpoint model/LLM.
8. `page/deployment.py` → checklist deploy.

---

## Struktur Project

```text
.
├── app.py
├── core/
│   └── theme.py
├── ui/
│   └── widgets.py
├── services/
│   ├── dummy_data.py
│   └── llm.py
├── page/
│   ├── beranda.py
│   ├── dasar_widget.py
│   ├── state_form_cache.py
│   ├── mini_project.py
│   ├── endpoint_llm.py
│   └── deployment.py
├── utils/
│   └── ollama_client.py
├── data/
│   └── .gitkeep
└── .streamlit/
    ├── config.toml
    └── secrets.example.toml
```

---

## Menjalankan Lokal

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Akses: `http://localhost:8501`

---

## Menjalankan di Codespaces

1. Buka repo fork peserta di Codespaces.
2. Tunggu dependency selesai terpasang.
3. Jalankan:
   ```bash
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```
4. Buka port `8501`.

---

## Secrets (Opsional untuk endpoint privat)

```bash
cp .streamlit/secrets.example.toml .streamlit/secrets.toml
```

Lalu isi API URL/API key sesuai kebutuhan.

---

## Catatan

- Main branch ini sengaja dibuat sederhana untuk praktik.
- Versi fitur lanjutan dapat dikembangkan di branch terpisah.
