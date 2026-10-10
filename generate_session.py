"""
Bikin STRING_SESSION Pyrogram untuk AKUN ASISTEN (akun user Telegram biasa).

Kenapa perlu? Akun BOT tidak bisa join voice chat — hanya akun user yang bisa.
Jadi bot musik ini butuh satu akun Telegram biasa ("asisten") yang akan
masuk ke voice chat grup dan memutar audionya.

⚠️  PENTING: pakai AKUN KEDUA, jangan nomor HP utamamu.
Session string ini = kunci login akun tersebut. Jangan disebar ke siapa pun.

Cara pakai (jalankan di komputermu sendiri, BUKAN di server):
    pip install pyrogram
    python generate_session.py

Nanti diminta: API_ID, API_HASH, nomor HP akun asisten, lalu kode OTP
yang dikirim Telegram ke akun itu. Kalau akunnya pakai 2FA, diminta password juga.
Hasilnya: satu baris panjang STRING_SESSION → paste ke env var STRING_SESSION.
"""
import asyncio

from pyrogram import Client


async def main():
    api_id = int(input("API_ID (dari my.telegram.org): ").strip())
    api_hash = input("API_HASH (dari my.telegram.org): ").strip()
    print("\nLogin sebagai AKUN ASISTEN (akun kedua, bukan nomor utamamu)...")
    async with Client("gen-session", api_id=api_id, api_hash=api_hash) as app:
        session = await app.export_session_string()
    print("\n✅ STRING_SESSION kamu (RAHASIA — jangan disebar!):\n")
    print(session)
    print("\nCopy baris di atas ke env var STRING_SESSION di Railway.")


if __name__ == "__main__":
    asyncio.run(main())
