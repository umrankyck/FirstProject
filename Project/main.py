import streamlit as st
import pandas as pd



page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
background-color: #A547DE;
opacity: 0.8;
background-image:  linear-gradient(135deg, #a547de 25%, transparent 25%), linear-gradient(225deg, #a547de 25%, transparent 25%), linear-gradient(45deg, #a547de 25%, transparent 25%), linear-gradient(315deg, #a547de 25%, #A547DE 25%);
background-position:  10px 0, 10px 0, 0 0, 0 0;
background-size: 20px 20px;
background-repeat: repeat;
}
</style>
"""
 

 
 
 
 
st.markdown(page_bg_img, unsafe_allow_html=True)  #html izin verir

st.title("Sayfama Hoşgeldiniz :tada: ")
st.markdown("---")

st.subheader('Hangi kelimeyi aramak istersiniz?')
option = st.selectbox(
    'Seçim yapınız...',('Seçiniz','Başarı', 'Özgüven', 'Stres', 'Obsesif'))

st.write('Kelime:', option)

if option == 'Başarı':
    st.write('Başarı - Bir işi istenilen bir biçimde bitirmek.')

if option == 'Özgüven' :
    st.write('Öz güven, kişinin kendi değeri hakkındaki subjektif değerlendirmesi ve kişinin kendi özelliklerinin ne ölçüde olumlu ya da olumsuz olduğu hakkındaki yorumudur. Öz güven hem kişinin kendisine ilişkin düşünceleri, hem bu düşüncelerin yol açtığı duyguları, hem de bu duygu ve düşüncelerin ifadesi olan davranışları içerir.')

if option == 'Stres' :
    st.write('Stres; vücutta belirli biyolojik, fiziksel ve bilişsel reaksiyonların gelişimini tetikleyen, kişiyi anlık olarak bir tehditle veya mücadele gerektirecek bir sorunla karşı karşıya bırakan koşullarda ortaya çıkan durumu ifade eder.')

if option == 'Obsesif' :
    st.write('Takıntılı düşünce ve dürtüler anlamına gelen obsesyon ile yineleyici zihinsel eylemler ve davranışlar anlamına gelen kompulsiyon davranışları bir araya gelerek hastalığı oluşturur. Obsesyon, yani kişinin zihninde uzaklaştıramadığı fikir, düşünce ve dürtüler, kişinin isteği dışında gelişir.')


