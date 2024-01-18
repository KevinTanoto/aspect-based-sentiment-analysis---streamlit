import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pre_processing

def process_dataframe(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df = df.sort_values(by='created_at' , ascending=False)
    df = df.set_index('created_at')
    df_sample = resample(df)
    count_positive, count_neutral, count_negative= label_count(df)
    top_pos, top_neg = top_tweet(df)
    daily_counts_df = daily_counts(df)
    return df, df_sample, count_positive, count_neutral, count_negative , top_pos, top_neg, daily_counts_df

def generate_wc(text):
    wordcloud = WordCloud(width=1600, height=800, max_font_size=200, background_color=None)
    wordcloud.generate(text)
    return wordcloud

def resample(df):
    df_sample = df.resample('2D').mean()
    return df_sample

def daily_counts(df):
    daily_counts_df = df.resample('D').size().rename('daily_count')
    return daily_counts_df

def label_count(df):
    count_positive = df['label'].value_counts().get(1, 0)
    count_neutral = df['label'].value_counts().get(0, 0)
    count_negative = df['label'].value_counts().get(-1, 0)
    return count_positive, count_neutral, count_negative

def top_tweet(df):
    sorted_df = df.sort_values(by='favorite_count', ascending=False)
    top_5data_pos = sorted_df[sorted_df['label'] == 1].head(5)[['full_text', 'username']]
    top_5data_neg = sorted_df[sorted_df['label'] == -1].head(5)[['full_text', 'username']]

    top_5data_pos.index = top_5data_pos.index.strftime('%d-%m-%y')
    top_5data_neg.index = top_5data_neg.index.strftime('%d-%m-%y')

    top_5data_pos = top_5data_pos.rename(columns={'full_text': 'Tweet', 'username': 'Username'})
    top_5data_neg = top_5data_neg.rename(columns={'full_text': 'Tweet', 'username': 'Username'})
    
    return top_5data_pos, top_5data_neg


def renderPage():
    st.title("Dashboard")
    candidate_type = st.selectbox(
     'Calon presiden',
     ('Prabowo Subianto', 'Ganjar Pranowo', 'Anies Baswedan'))

    if candidate_type == "Prabowo Subianto":

        df_prabowo = pd.read_csv("data/prabowo_1-dec-2023__5-jan-2024.csv")
        df, df_sample, pos, neu, neg,  top_pos, top_neg, daily_counts_df = process_dataframe(df_prabowo)
        wc = pre_processing.wc_format(df)
        total_data = len(df_prabowo)
        pie = "images/aniessentiment pyABSA.png"
 
    elif candidate_type == "Ganjar Pranowo":

        df_ganjar = pd.read_csv("data/ganjar_1-dec-2023__5-jan-2024.csv")
        df, df_sample, pos, neu, neg, top_pos, top_neg, daily_counts_df = process_dataframe(df_ganjar)
        wc = pre_processing.wc_format(df)
        total_data = len(df_ganjar)
        pie = "images/ganjar sentiment pyABSA.png"

    elif candidate_type == "Anies Baswedan":

        df_anies = pd.read_csv("data/anies_1-dec-2023__5-jan-2024.csv")
        df, df_sample, pos, neu, neg,  top_pos, top_neg, daily_counts_df = process_dataframe(df_anies)
        wc = pre_processing.wc_format(df)
        total_data = len(df_anies)
        pie = "images/prabowo sentiment pyABSA.png"

    total_data_text_box = f"""
                            <div style="
                                display:flex;
                                justify-content: center;
                                margin: 15px;
                            ">
                                <div style="
                                    padding: 10px;
                                    border: 2px solid #333;
                                    border-radius: 5px;
                                    display:flex;
                                    flex-direction:column;
                                    text-align: center;
                                    align-items: center;
                                ">
                                    <div style="
                                        font-weight: bold;
                                    ">
                                        Total Data
                                    </div>
                                    <div style="
                                        color: deepskyblue;
                                        font-weight: bold;
                                    ">
                                        {total_data}
                                    </div>
                                </div>
                            </div>
                            """

    st.markdown(total_data_text_box, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with st.container():
        c1.write("<p style='text-align: center; font-size: 20px; font-weight: bold;'>Time Series of The Sentiment</p>", unsafe_allow_html=True)
        c1.line_chart(df_sample, y="score")
        c2.write("<p style='text-align: center; font-size: 20px; font-weight: bold;'>Daily Mention</p>", unsafe_allow_html=True)
        c2.area_chart(daily_counts_df, y=["daily_count"])
        
    c3, c4 = st.columns(2)
    with st.container():
        # fig1, ax1 = plt.subplots(figsize=(7, 4))
        c3.write(f"<p style='text-align: center; font-size: 20px; font-weight: bold;'>{candidate_type} Sentiment</p>", unsafe_allow_html=True)
        c3.image(pie)
        # ax1.pie([pos, neu, neg], labels=['Positive','Neutral','Negative'], autopct='%1.1f%%', startangle=90, colors = ['green', 'orange', 'red'])
        # ax1.axis('equal')
        # c3.pyplot(fig1)

        c4.write("<p style='text-align: center; font-size: 20px; font-weight: bold;'>Wordcloud</p>", unsafe_allow_html=True)
        wordcloud = WordCloud(width=1400, height=900, max_font_size=200, background_color="white", max_words = 100, scale=1.5)
        wordcloud.generate(wc)
        c4.image(wordcloud.to_array())

    c5, c6 = st.columns(2)
    with st.container():
        c5.write("<p style='text-align: center; font-size: 20px; font-weight: bold;'>Top 5 Positive Tweet</p>", unsafe_allow_html=True)
        c5.dataframe(top_pos)
        c6.write("<p style='text-align: center; font-size: 20px; font-weight: bold;'>Top 5 Negative Tweet</p>", unsafe_allow_html=True)
        c6.dataframe(top_neg)