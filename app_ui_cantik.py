
import streamlit as st

st.set_page_config(page_title="Jual UC PUBG", page_icon="🔥", layout="centered")

# Gaya tajuk dan pengenalan
st.markdown("""
<style>
    .main {
        background-color: #f7f8fa;
    }
    .title {
        font-size: 36px;
        color: #ff4b4b;
        text-align: center;
    }
    .subtext {
        font-size: 18px;
        color: #333;
        text-align: center;
    }
</style>
<div class="title">🔥 Jual UC PUBG - Chatbot Tempahan</div>
<div class="subtext">Selamat datang! Tempah UC anda dengan mudah 💬</div>
<br>
""", unsafe_allow_html=True)

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

# Hantar butang
if st.button("🛒 Hantar Tempahan"):
    harga = pakej_uc[pakej_dipilih]
    st.success(f"✅ Tempahan diterima!\n\n**{nama}** telah menempah **{pakej_dipilih}** berharga **RM{harga:.2f}** untuk ID: `{id_pubg}`.")

    # Simpan maklumat ke dalam fail
    with open("rekod_pelanggan.txt", "a") as fail:
        fail.write(f"Nama: {nama}, Pakej: {pakej_dipilih}, Harga: RM{harga:.2f}, ID: {id_pubg}\n")

    st.balloons()
