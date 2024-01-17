import streamlit as st
import requests

# def getSentiments(userText, type):
#     sentiment_classifier = APC.SentimentClassifier("\Model-PyABSA\checkpoints")
#     if type == 'SentimentClassifier - Prabowo':
#         target_word = "prabowo"
#     elif type == 'SentimentClassifier - Ganjar':
#         target_word = "ganjar"
#     elif type == 'SentimentClassifier - Anies':
#         target_word = "anies"
#     replacement_start = "[B-ASP]"
#     replacement_end = "[E-ASP]"

#     result_text = []

#     for sent in [userText]:
#         if target_word in sent.lower():
#             modified_t = sent.replace(target_word, f"{replacement_start}{target_word}{replacement_end}")
#             result_text.append(modified_t)

#     text = sentiment_classifier.predict(
#                         text=result_text,
#                         save_result=True,
#                         print_result=True,
#                         ignore_error=True,
#                         )
#     sentiment = text[0]["sentiment"][0]
#     confidence = text[0]["confidence"][0]

#     return sentiment, confidence
    
        

def renderPage():
    st.title("Sentiment Analysis 😊😐😕😡")
    st.markdown("<hr style='border:2px solid #333'>", unsafe_allow_html=True)

    st.subheader("User Input Text Analysis")
    st.text("Analyzing text data given by the user and find sentiments within it.")
    st.text("")
    userText = st.text_input('User Input', placeholder='Input text HERE')
    st.text("")
    type = st.selectbox(
     'Type of model',
     ('SentimentClassifier - Prabowo', 'SentimentClassifier - Ganjar', 'SentimentClassifier - Anies'))
    st.text("")
    if st.button('Predict'):
        if(userText!="" and type!=None):
            st.text("")
            st.components.v1.html("""
                                <h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>
                                """, height=100)
            
            payload = {"userText": userText, "modelType": type}
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            result = response.json()
            
            st.success(f"Sentiment: {result['sentiment']} with {result['confidence']}.")
        else:
            st.warning("Please enter a sentence for sentiment analysis.")
    #         