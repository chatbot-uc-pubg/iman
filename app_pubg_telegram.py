
import streamlit as st
import requests

st.set_page_config(page_title="Jual UC PUBG", page_icon="🔥", layout="centered")

# Fungsi hantar ke Telegram
def hantar_ke_telegram(nama, pakej, id_pubg, harga):
    mesej = f"🛒 Tempahan Baru!\nNama: {nama}\nID PUBG: {id_pubg}\nPakej: {pakej}\nHarga: RM{harga:.2f}"
    url = f"https://api.telegram.org/bot8070853770:AAFkCsS9lIMfaPVnmh_i2Eznu4EXvXuxwlA/sendMessage"
    data = {
        "chat_id": "920806705",
        "text": mesej
    }
    requests.post(url, data=data)

# Gaya tema PUBG
st.markdown("""
<style>
    .stApp {
        background-image: url('https://wallpaperaccess.com/full/1372679.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .title {
        font-size: 40px;
        color: #FFD700;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px #000;
    }
    .subtext {
        font-size: 20px;
        color: #fff;
        text-align: center;
        margin-bottom: 30px;
    }
    .stTextInput > div > label {
        color: #fff;
    }
</style>
<div class="title">🔥 PUBG UC Order Bot</div>
<div class="subtext">Tempah UC PUBG anda dengan mudah dan pantas!</div>
""", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/5/5e/PUBG-Logo.svg", width=200)

# Senarai pakej
pakej_uc = {
    "60 UC": 4.50,
    "325 UC": 20.00,
    "660 UC": 38.00,
    "1800 UC": 100.00,
    "3850 UC": 190.00
}

# Form input
st.markdown("### 📝 Isi Maklumat Anda")
nama = st.text_input("🧑 Nama Anda")
id_pubg = st.text_input("🎮 ID PUBG Anda")
pakej_dipilih = st.selectbox("📦 Pilih Pakej UC", list(pakej_uc.keys()))

# Butang hantar
if st.button("🛒 Hantar Tempahan"):
    harga = pakej_uc[pakej_dipilih]
    st.success(f"✅ Tempahan diterima!\n\n**{nama}** telah menempah **{pakej_dipilih}** berharga **RM{harga:.2f}** untuk ID: `{id_pubg}`.")
    with open("rekod_pelanggan.txt", "a") as fail:
        fail.write(f"Nama: {nama}, Pakej: {pakej_dipilih}, Harga: RM{harga:.2f}, ID: {id_pubg}\n")
    hantar_ke_telegram(nama, pakej_dipilih, id_pubg, harga)
    st.balloons()
