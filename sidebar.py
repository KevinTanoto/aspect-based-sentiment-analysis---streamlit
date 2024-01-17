from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu

def show():
    with st.sidebar:
        st.markdown("""
                    # Applications
                    """, unsafe_allow_html = False)
        selected = option_menu(
            menu_title = "Main Menu",
            options = ["Home", "Dashboard", "Sentiment Analysis" , "Contact"], 
            icons = ["house", "bar-chart", "card-text", "person-rolodex"],
            menu_icon="cast",
            default_index = 0,
        )
        return selected