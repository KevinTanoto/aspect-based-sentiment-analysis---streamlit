## ABSA Indo-Election 2024

ABSA Indo-Election 2024 is a website application that shows a sentiment of each aspect in the sentence made using Python and Streamlit. The data is gatthered using Twitter API during the Indonesian presidential election 2023 - 2024. ABSA Indo-Election 2024 applies DeBERTa-v2 to predict the the aspect-based sentiment and compared it with machine learning model such as SVM, Naive Bayes, and Random Forest. In this web application. The application is divided into 4 pages, namely the home page, prediction page, dashboard page and contact page. The home page functions as an introduction, while the prediction page functions to predict the sentiment of a sentence through the selected category. The dashboard page has a function to visualize 3 data scraping results

## Installation
You need to install all required packages which are listed in the requirements.txt to run this web app.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the required package.

```
pip install -r requirements.txt
```

## Run Application on Local Environment
After installing all the required libraries, you can run this application on your local machine by running this command. Please make sure that you add streamlit command to your PATH environment variable.

```
streamlit run app.py
```
## Deployment link [HERE](https://aspect-based-sentiment-analysis---app-jmlbj33twbehchna9w9fqt.streamlit.app/)
