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
    st.markdown("<h2 style=''>Investigating the Challenges of Aspect-Based Sentiment Analysis on Twitter During Indonesia's 2024 Presidential Election</h1>", unsafe_allow_html=True) 
    
    st.markdown("<hr style='border:2px solid #333'>", unsafe_allow_html=True)

    st.markdown("<p class='justify-text'>In today's era of digital communication, social media platforms have become powerful channels for discussion and public expression.\
                 As a social media platform, Twitter plays an important role in shaping and depicting public sentiment, especially regarding political events. \
                 As Indonesia prepares to welcome the 2024 presidential election, understanding public opinion trends on Twitter is important to gain comprehensive insight into voter sentiment.</p>", unsafe_allow_html=True)
    st.image("images/Foto Capres - Kompas.png", caption="Surat suara paslon capres-cawapres 2024 (dok. KPU)", use_column_width=True)

    c1, c2, c3 = st.columns(3)
    with st.container():
        c1.image("images/wordcloud anies imin copy.png", caption="Wordcloud Visi Misi Anies Baswedan", use_column_width=True)
        c2.image("images/wordcloud prabowo gibran copy.png", caption="Wordcloud Visi Misi Prabowo Subianto", use_column_width=True)
        c3.image("images/wordcloud ganjar mahmud copy.png", caption="Wordcloud Visi Misi Ganjar Mahmud", use_column_width=True)

    numbered_list_html = """
                        <h5>The aim of this research: </h5>
                        <ol>
                            <li>Collecting and processing Twitter data related to 2024 presidential candidates.</li>
                             <li>Applies Aspect-Based Sentiment Analysis techniques for a detailed examination of sentiment expressed on Twitter.</li>
                             <li>Identify and categorize key aspects that influence public sentiment towards each candidate.</li>
                             <li>Measure and compare the overall sentiment score for each candidate based on the identified aspects.</li>
                             <li>Draw meaningful conclusions and provide actionable insights for political strategists and decision makers.</li>
                        </ol>
                        """
    st.markdown(numbered_list_html, unsafe_allow_html=True)
