import streamlit as st
import sidebar
import home
import sentimentAnalysis
import contact
import dashboard
import nltkmodule

st.set_page_config(layout="wide")
page = sidebar.show()

if page=="Home":
    home.renderPage()
elif page=="Dashboard":
    dashboard.renderPage()
elif page=="Sentiment Analysis":
    sentimentAnalysis.renderPage()
elif page=="Contact":
    contact.renderPage()
