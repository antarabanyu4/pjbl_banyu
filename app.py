import streamlit as st

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon="🔥",)

with st.sidebar:
    col1, col2, col3 = st.columns((1,2,1))
    with col2:
        st.image("mtk.png")
    st.title("Bangun Datar")

    pilihan = st.selectbox(
        "Pilih Bangun Datar",
        ("Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Trapesium",))
    st.caption("Dibuat Dengan 💘 Oleh **Antara Banyu**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi =st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            #st.success(f"Luas Persegi Adalah {luas: .2f} Dan Keliling Persegi Adalah {keliling: .2f}")
            col1, col2= st.columns((2,2))
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()
           
    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas Persegi Panjang Adalah {luas: .2f} Dan Keliling Persegi Panjang Adalah {keliling: .2f}")
            st.balloons()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jari_jari = st.number_input("Masukkan Jari-Jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            st.success(f"Luas Lingkaran Adalah {luas: .2f} Dan Keliling Lingkaran Adalah {keliling: .2f}")
            st.balloons()

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` dan `keliling` segitiga")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi1 = st.number_input("Masukkan Sisi 1")
        sisi2 = st.number_input("Masukkan Sisi 2")
        sisi3 = st.number_input("Masukkan Sisi 3")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            st.success(f"Luas Segitiga Adalah {luas: .2f} Dan Keliling Segitiga Adalah {keliling: .2f}")
            st.balloons()

    case "Trapesium":
        st.title("Trapesium")
        st.markdown("Menghitung `luas` dan `keliling` trapesium")
        alas1 = st.number_input("Masukkan Alas 1")
        alas2 = st.number_input("Masukkan Alas 2")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi1 = st.number_input("Masukkan Sisi 1")
        sisi2 = st.number_input("Masukkan Sisi 2")
        sisi3 = st.number_input("Masukkan Sisi 3")
        sisi4 = st.number_input("Masukkan Sisi 4")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * (alas1 + alas2) * tinggi
            keliling = sisi1 + sisi2 + sisi3 + sisi4
            st.success(f"Luas Trapesium Adalah {luas: .2f} Dan Keliling Trapesium Adalah {keliling: .2f}")
            st.balloons()

    case _:
        st.error("Terjadi Kesalahan")
