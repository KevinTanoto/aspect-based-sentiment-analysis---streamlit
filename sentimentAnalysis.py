import streamlit as st
import requests
import pandas as pd
from pyabsa import AspectPolarityClassification as APC
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords

def read_file(file_path):

    with open(file_path, "r") as file:
        my_list = [line.strip() for line in file.readlines()]

    return my_list

def getSentiments(userText, key):
    sentiment_classifier = APC.SentimentClassifier("\Model-PyABSA\checkpoints")
    replacement_start = "[B-ASP]"
    replacement_end = "[E-ASP]"

    if key == 1:
        target_word1, target_word2 = "display", "navigation"
        target_word3, target_word4 = "design", "functions"

        for sent in [userText.lower()]:
            modified_t = sent.replace(target_word1, f"{replacement_start}{target_word1}{replacement_end}")
            modified_t = modified_t.replace(target_word2, f"{replacement_start}{target_word2}{replacement_end}")
            modified_t = modified_t.replace(target_word3, f"{replacement_start}{target_word3}{replacement_end}")
            modified_t = modified_t.replace(target_word4, f"{replacement_start}{target_word4}{replacement_end}")  
    elif key == 2:
        target_word1, target_word2 = "anies", "ganjar"

        for sent in [userText.lower()]:
            modified_t = sent.replace(target_word1, f"{replacement_start}{target_word1}{replacement_end}")
            modified_t = modified_t.replace(target_word2, f"{replacement_start}{target_word2}{replacement_end}")

    elif key == 3:
        target_word1, target_word2 = "delivery", "restaurant"
        for sent in [userText.lower()]:
            modified_t = sent.replace(target_word1, f"{replacement_start}{target_word1}{replacement_end}")
            modified_t = modified_t.replace(target_word2, f"{replacement_start}{target_word2}{replacement_end}")
    elif key == 4:
        modified_t = [userText]

        text = sentiment_classifier.predict(
                        text=modified_t,
                        save_result=False,
                        print_result=True,
                        ignore_error=True,
                        )
        
        sentiment = text[0]["sentiment"]
        confidence = text[0]["confidence"]
        aspect = text[0]['aspect']
        return sentiment, confidence,  aspect
        
    text = sentiment_classifier.predict(
                        text=modified_t,
                        save_result=False,
                        print_result=True,
                        ignore_error=True,
                        )
    
    sentiment = text["sentiment"]
    confidence = text["confidence"]
    aspect = text['aspect']

    return sentiment, confidence, aspect

def get_sentiment_ml(path, text):
    le = LabelEncoder()
    my_list = read_file("data/processed_tweets.txt")
    le.fit(["Positive", "Negative"])
    tfidfconverter = TfidfVectorizer(max_features=2000, min_df=5,stop_words=stopwords.words('english'), max_df=0.7,ngram_range=(1,3))
    tfidfconverter.fit_transform(my_list).toarray()

    model = pickle.load(open(path,'rb'))

    review_vector = tfidfconverter.transform([text]).toarray()
    pred_text = model.predict(review_vector)
    pred_text = le.inverse_transform(pred_text)
    
    return pred_text

def renderPage():
    st.title("Apect-Based Sentiment Analysis")
    st.markdown("<hr style='border:2px solid #333'>", unsafe_allow_html=True)

    st.subheader("User Input Aspect Based Sentiment Analysis")
    st.markdown("<p class='justify-text'>Sentiment Analysis Model for users seeking insights into public sentiments.\
                Users have the flexibility to select the model they want to analyze which is DeBERTa, RF, NB, and SVM</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='justify-text' style = 'font-weight: bold'>1. The display is sharp, but the navigation feels a bit off. The design is modern, but the functions can be confusing. Overall, it's a mixed bag.</p>", unsafe_allow_html=True)
    st.markdown("<p class='justify-text'>In this sentence there is a lot of use of ambiguous language, ambiguity in the language 'a bit off', 'could be confusing'. This will make it difficult to carry out sentiment \
                analysis. ABSA can identify one by one the aspects that appear in a sentence and provide sentiment for each sentence.</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='justify-text' style = 'font-weight: bold'>2. I dislike anies, that is why i choose ganjar.</p>", unsafe_allow_html=True)
    st.markdown("<p class='justify-text'>Standard sentiment analysis will have difficulty in carrying out sentiment accurately, the only solution for standard sentiment analysis is to separate\
                 sentences one by one. by training the ABSA model with data that annotates selected aspects, the ABSA model can identify aspects and provide sentiment towards specific aspects</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='justify-text' style = 'font-weight: bold'>3. Despite the long wait time for my food delivery, the restaurant's quality and taste make it worth it!</p>", unsafe_allow_html=True)
    st.markdown("<p class='justify-text'>This sentence is also confusing because long here is negative, but if for example the word 'long battery' then the word becomes positive. ABSA considers the context in which emotions\
                 are expressed. The consideration is that the emotions associated with a particular aspect may differ based on the way it is expressed.</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='justify-text' style = 'font-weight: bold'>4. I don't like it, it doesn't feel right.</p>", unsafe_allow_html=True)
    st.markdown("<p class='justify-text'>In this sentence most models can perform sentiment analysis well. The ABSA model cannot find aspects in sentences so it will perform global sentiment</p>", unsafe_allow_html=True)
    
    options = {"The display is sharp, but the navigation feels a bit off. The design is modern, but the functions can be confusing. Overall, it's a mixed bag.": 1,
                "I dislike anies, that is why i choose ganjar.": 2, 
                "Despite the long wait time for my food delivery, the restaurant's quality and taste make it worth it!": 3,
                "I don't like it, it doesn't feel right.": 4}
    st.text("")
    text = st.selectbox('Select Text to Predict', options.keys())
    
    key = options[text]
    
    model = st.radio(
    "Choose the model",
    ["DeBERTa", "Random Forest", "Naive Bayes","Support Vector Machine"])
    # captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

    if model == 'DeBERTa':
        st.write('You selected DeBERTa')
    if model == 'Random Forest':
        st.write('You selected Random Forest Model')
        path = "Classification Model/random_forest_sma.pkl"
    if model == 'Naive Bayes':
        st.write('You selected Naive Bayes Model')
        path = "Classification Model/naive_bayes_sma.pkl"
    if model == 'Support Vector Machine':
        st.write('You selected Support Vector Machine')
        path = "Classification Model/support_vector_machine_sma.pkl"

    st.text("")
    if st.button('Predict'):
        if model == 'DeBERTa':
            sentiment, confidence, aspect = getSentiments(text, key)
            # st.write(text)
            data_df = pd.DataFrame(
                {
                    "Sentiment": sentiment,
                    "Aspect": aspect,
                    "Confidence": confidence
                }
            )
            st.dataframe(data_df) 
            # st.success(f"Sentiment: {sentiment} {confidence} {aspect}")



            # result = getSentiments(text, key)
            # st.success(f"Sentiment: {result}")
        else:
            result = get_sentiment_ml(path,text)
            st.success(f"Sentiment: {result}")


        # if(userText!="" and type!=None):
        #     st.text("")
        #     st.components.v1.html("""
        #                         <h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>
        #                         """, height=100)
            
        #     payload = {"userText": userText, "modelType": type}
        #     response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        #     result = response.json()
            
        #     st.success(f"Sentiment: {result['sentiment']} with {result['confidence']}.")
        # else:
        #     st.warning("Please enter a sentence for sentiment analysis.")


       