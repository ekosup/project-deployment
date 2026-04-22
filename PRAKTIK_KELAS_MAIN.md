# Praktik Kelas (untuk branch `main`)

Dokumen ini dipakai sebagai panduan resmi peserta saat branch `main` dipublikasikan.
Materi di-derive dari branch pengembangan Codespaces (`feat/codespaces-ready`) dan disederhanakan untuk praktik kelas.

---

## Tujuan Praktik

Setelah praktik, peserta diharapkan dapat:
1. Menjalankan aplikasi Streamlit modular.
2. Memahami alur `ui` + `services` + `page`.
3. Mengubah widget dan state sederhana.
4. Menghubungkan app ke mode endpoint dummy/LLM.
5. Menyiapkan hasil kerja untuk dinilai.

---

## Aturan Kerja Peserta

- **Jangan commit langsung ke repo utama**.
- Setiap peserta wajib kerja di **repo fork masing-masing**.
- Gunakan branch kerja dengan format:
  - `lab-1-nama`
  - `lab-2-nama`
  - `final-nama`

Contoh:
- `lab-1-andi`
- `final-siti`

---

## Alur Cepat Peserta

1. Fork repo dari trainer.
2. Buka fork di Codespaces.
3. Jalankan aplikasi:
   ```bash
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```
4. Kerjakan latihan sesuai modul.
5. Commit perubahan di branch sendiri.
6. Submit hasil (pilih salah satu):
   - Link branch di fork, atau
   - Pull Request ke repo trainer (jika diminta).

---

## Struktur yang Perlu Dipahami Peserta

```text
app.py              # entry point + navigation
core/theme.py       # setup tema dan style global
ui/widgets.py       # komponen UI reusable (banner)
services/           # logic data dan integrasi endpoint
page/               # modul halaman (function-based render)
utils/              # helper eksternal endpoint Ollama
```

---

## Modul Latihan yang Dikerjakan

1. **Dasar & Widget**
   - Ubah minimal 3 widget dan jelaskan dampaknya.
2. **State/Form/Cache**
   - Tambah 1 field form dan simpan ke `session_state`.
3. **Mini Project**
   - Tambah 1 filter baru di sidebar.
4. **Endpoint LLM**
   - Uji mode Dummy, lalu coba mode endpoint nyata (jika tersedia).
5. **Deployment**
   - Simulasikan checklist deployment + konfigurasi secrets.

---

## Format Submit

Saat submit, sertakan:
- Nama peserta
- Link fork + branch
- Ringkasan perubahan (3–5 poin)
- Screenshot halaman utama app yang sudah dimodifikasi

Template ringkasan:

```text
Nama:
Branch:
Perubahan:
1)
2)
3)
Kendala:
```

---

## Penutup

Jika semua modul selesai, lanjutkan ke tantangan akhir: integrasikan satu endpoint nyata dan tambahkan 1 visualisasi baru pada mini project.
