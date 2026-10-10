# 🎵 Bot Musik Voice Chat Telegram — v3

> **Catatan v3:** pakai `pytgcalls==3.0.0.dev24` (versi dev) karena `tgcalls`
> versi stabil cuma punya wheel sampai Python 3.10, sedangkan hosting modern
> (termasuk botkeep) cuma sediain Python 3.11+. API v3 beda total: lagu
> **di-download dulu** baru diputar dari file lokal (bukan streaming URL).
> Repo v2 (stabil, Python ≤3.10) tetap ada di `riffbois/music-bot`.

Bot buat muter lagu di voice chat grup Telegram. Search pakai **YouTube Data API resmi**, download via yt-dlp.

## Kenapa butuh akun asisten?

Akun **bot** Telegram tidak bisa join voice chat — hanya akun **user** biasa yang bisa.
Jadi bot ini jalan dengan 2 akun:

| Akun | Peran |
|------|-------|
| **Bot** (`BOT_TOKEN` dari @BotFather) | Terima perintah `/play` dll dari user |
| **Asisten** (akun user biasa, `STRING_SESSION`) | Join voice chat & muter audionya |

⚠️ Pakai **akun Telegram kedua** untuk asisten, jangan nomor HP utamamu.

## Yang kamu butuhin

1. **API ID & API Hash** — buka my.telegram.org → login → API development tools → bikin app → copy
2. **Bot token** — chat @BotFather di Telegram → /newbot → copy tokennya
3. **Akun asisten** — akun Telegram kedua (nomor HP berbeda)
4. **STRING_SESSION** — string session akun asisten, cara bikinnya:
   ```bash
   pip install pyrogram
   python generate_session.py
   ```
   Ikuti panduannya (login pakai nomor HP akun asisten + kode OTP).
   Hasilnya satu baris panjang → simpan sebagai env var `STRING_SESSION`.
   (Jalankan di komputermu sendiri, bukan di server.)
5. **YouTube API Key** (opsional tapi disarankan) — console.cloud.google.com → bikin project → enable "YouTube Data API v3" → Credentials → Create API key. Kalau kosong, bot fallback ke search yt-dlp biasa.

## Deploy ke Railway

1. Push folder ini ke GitHub
2. Buka railway.app → **New Project** → **Deploy from GitHub** → pilih repo
3. Railway otomatis deteksi `nixpacks.toml` (Python 3.11 + ffmpeg)
4. Buka tab **Variables**, tambahin:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `STRING_SESSION`
   - `YOUTUBE_API_KEY` (opsional)
5. Deploy otomatis jalan!

> 💰 Biaya: Railway kasih **kredit trial $5 sekali pakai** (±30 hari) buat akun baru.
> Bot musik jalan terus 24/7 makan sekitar **$5–10/bulan**. Setelah kredit trial habis,
> bot butuh plan berbayar biar tetap nyala. Pantau pemakaian di dashboard Railway.

## Cara pakai di grup

1. Tambahin **bot** ke grup
2. Tambahin **akun asisten** ke grup juga, jadikan **admin** (butuh izin kelola voice chat)
3. Buka voice chat di grup
4. Kirim `/play shape of you`
5. Enjoy! 🎶

## Perintah

| Perintah | Fungsi |
|----------|--------|
| `/play <judul>` | Putar lagu (search via YouTube API) |
| `/skip` | Lewati lagu |
| `/stop` | Berhenti & keluar |
| `/pause` | Jeda |
| `/resume` | Lanjut |
| `/queue` | Lihat antrean |

## Cara kerja search

1. Bot cari judul via **YouTube Data API** (resmi, akurat, ada kuota 10.000 unit/hari gratis)
2. Kalau API key kosong/error → fallback ke search yt-dlp biasa
3. Audio di-stream langsung dari YouTube (nggak disimpan)

## Troubleshooting

- **"Gagal join voice chat"** → pastikan voice chat sudah dibuka, akun asisten sudah join grup, dan asisten jadi admin / punya izin voice chat.
- **Error 403 / "sign in to confirm you're not a bot" dari YouTube** → YouTube kadang memblokir IP datacenter (Railway/Render/VPS). Ini masalah umum bot musik di cloud. Opsi: coba lagi nanti, pakai proxy residential untuk traffic YouTube, atau pindah host yang IP-nya tidak diblokir.
- **Bot tidak merespons perintah** → cek log Railway, pastikan semua env var terisi benar.

## Alternatif deploy

- **Render**: `render.yaml` sudah diset sebagai Background Worker (butuh plan berbayar, mulai ~$7/bulan — free tier Render mematikan service yang idle)
- **Heroku**: pakai `Procfile` yang udah ada (Heroku sudah tidak ada free tier)
- **VPS**: install Python 3.11 + ffmpeg, jalanin pakai tmux/systemd (paling murah untuk 24/7, ~$4–6/bulan)
