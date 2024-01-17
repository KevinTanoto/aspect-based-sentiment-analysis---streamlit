import streamlit as st
import streamlit.components.v1 as components

def renderPage():
    st.markdown("""
                <style>
                    .justify-text {
                        text-align: justify;
                    }
                </style>
                """, unsafe_allow_html=True)
    st.markdown("<h2 style=''>Analyzing The Popularity of Indonesia'S 2024 Presidential Candidates On Twitter Using Aspect Based Sentiment Analysis</h1>", unsafe_allow_html=True) 
    
    st.markdown("<hr style='border:2px solid #333'>", unsafe_allow_html=True)

    st.markdown("<p class='justify-text'>Di era komunikasi digital saat ini, platform media sosial telah menjadi saluran yang kuat untuk berdiskusi dan berekspresi publik.\
                Sebagai platform sosial media, Twitter berperan penting dalam membentuk dan menggambarkan sentimen masyarakat, khususnya terkait peristiwa politik. \
                Saat Indonesia bersiap menyambut pemilu presiden tahun 2024, memahami tren opini publik di Twitter penting untuk mendapatkan wawasan komprehensif mengenai sentimen pemilih.</p>", unsafe_allow_html=True)
    st.image("images/Foto Capres - Kompas.png", caption="Surat suara paslon capres-cawapres 2024 (dok. KPU)", use_column_width=True)

    c1, c2, c3 = st.columns(3)
    with st.container():
        c1.image("images/wordcloud anies imin copy.png", caption="Wordcloud Visi Misi Anies Baswedan", use_column_width=True)
        c2.image("images/wordcloud prabowo gibran copy.png", caption="Wordcloud Visi Misi Prabowo Subianto", use_column_width=True)
        c3.image("images/wordcloud ganjar mahmud copy.png", caption="Wordcloud Visi Misi Ganjar Mahmud", use_column_width=True)

    numbered_list_html = """
                        <h5>Tujuan dari penelitian ini: </h5>
                        <ol>
                            <li> Mengumpulkan dan memproses data Twitter terkait calon presiden 2024.</li>
                            <li> Menerapkan teknik Analisis Sentimen Berbasis Aspek untuk pemeriksaan mendetail atas sentimen yang diungkapkan di Twitter.</li>
                            <li> Mengidentifikasi dan mengkategorikan aspek-aspek kunci yang mempengaruhi sentimen masyarakat terhadap masing-masing kandidat.</li>
                            <li> Mengukur dan membandingkan skor sentimen keseluruhan untuk setiap kandidat berdasarkan aspek yang diidentifikasi.</li>
                            <li> Menarik kesimpulan yang bermakna dan memberikan wawasan yang dapat ditindaklanjuti bagi para ahli strategi politik dan pengambil keputusan.</li>
                        </ol>
                        """
    st.markdown(numbered_list_html, unsafe_allow_html=True)
