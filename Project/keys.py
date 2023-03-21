import streamlit as st


def main():
# GİRİŞ UYGULAMASI
    st.title("Kullanıcı Girişi")
    
    menu = ["Ana Sayfa", "Giriş Yap"]
    choice = st.sidebar.selectbox("Menü", menu)

    if choice == "Ana Sayfa":
        st.subheader("Ana Sayfa")

    elif choice == "Giriş Yap":
        st.subheader("Giriş Sayfası")
        

        username = st.sidebar.text_input("Kullanıcı Adı")
        password = st.sidebar.text_input("Şifre", type= 'password')
        #Altına bir buton ekleyelim kenar çubuğuna 
        if st.sidebar.button("Giriş Yap"):
            if password == 'Değerlidir':
                st.success("Olarak Giriş Yapıldı {}" .format(username))

        
            else:
                st.warning("Kullanıcı Adı/ Şifre Hatalı!")




    
