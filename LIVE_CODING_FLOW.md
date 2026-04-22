# Live Coding Flow (Bit by Bit)

Dokumen ini membantu pengajar menjelaskan kode secara bertahap agar peserta tidak kewalahan.

## Sesi 1 — Fondasi App (10-15 menit)

1. Buka `app.py`.
2. Jelaskan:
   - `setup_page()`
   - `apply_kemenkeu_theme()`
   - `st.navigation(...)`
3. Jalankan app dan tunjukkan perpindahan page.

Checkpoint peserta:
- Bisa menjalankan `streamlit run app.py`.
- Paham bahwa setiap page adalah fungsi `render()`.

---

## Sesi 2 — Widget Dasar (20-30 menit)

1. Buka `page/dasar_widget.py`.
2. Jelaskan urutan tab:
   - quick win
   - input
   - pilihan & aksi
   - layout
3. Peserta ubah minimal 1 widget per tab.

Checkpoint peserta:
- Bisa menjelaskan hubungan input → output di Streamlit.

---

## Sesi 3 — State, Form, Cache (25 menit)

1. Buka `page/state_form_cache.py`.
2. Jelaskan:
   - `st.session_state`
   - `st.form` + `form_submit_button`
   - `@st.cache_data` dari `services/dummy_data.py`

Checkpoint peserta:
- Bisa menambahkan 1 field pada form.
- Bisa melihat perbedaan waktu proses cache pertama vs kedua.

---

## Sesi 4 — Mini Project Dashboard (25 menit)

1. Buka `page/mini_project.py`.
2. Jelaskan filter sidebar, metric, chart, download.
3. Tantangan: tambah 1 metric atau 1 chart.

Checkpoint peserta:
- Dashboard berubah sesuai filter.

---

## Sesi 5 — Endpoint LLM (25 menit)

1. Buka `page/endpoint_llm.py`.
2. Mulai dari mode Dummy.
3. Lanjutkan ke mode Ollama / generic endpoint.
4. Jelaskan fallback/error handling singkat.

Checkpoint peserta:
- Bisa kirim prompt dan menerima respons.

---

## Sesi 6 — Deployment (15 menit)

1. Buka `page/deployment.py`.
2. Review checklist deploy.
3. Simulasikan setup secrets (`.streamlit/secrets.toml`).

Checkpoint peserta:
- Tahu langkah deploy dan titik troubleshooting utama.
