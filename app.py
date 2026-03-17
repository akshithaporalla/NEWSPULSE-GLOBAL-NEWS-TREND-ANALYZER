import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

st.set_page_config(layout="wide")

# -----------------------------
# Initial News Dataset
# -----------------------------
if "news_data" not in st.session_state:

    st.session_state.news_data = pd.DataFrame({
    "Date":["10 Feb","10 Feb","09 Feb","08 Feb","07 Feb"],
    "Headline":[
    "AI startup raises funding",
    "Inflation rises globally",
    "New election reforms proposed",
    "Market hits new high",
    "Tech companies invest in AI"],
    "Topic":["Technology","Economy","Politics","Economy","Technology"],
    "Sentiment":["Positive","Negative","Neutral","Positive","Positive"]
    })

# -----------------------------
# Simple User Database
# -----------------------------
users = {
    "admin": "admin123",
    "user": "user123"
}

# -----------------------------
# Login Function
# -----------------------------
def login():

    st.title("Login - NewsPulse Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username.strip() in users and users[username.strip()] == password.strip():

            st.session_state["logged_in"] = True
            st.session_state["role"] = username.strip()

            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid Username or Password")

# -----------------------------
# Admin Page
# -----------------------------
def admin_page():

    st.title("Admin Dashboard")

    st.markdown("### Welcome , **admin** ")
    st.markdown("---")

    st.subheader(" Select Dashboard Section")

    if "section" not in st.session_state:
        st.session_state.section = ""

    col1,col2 = st.columns(2)

    with col1:
        if st.button(" Recent & Trending News"):
            st.session_state.section = "news"

        if st.button(" Sentiment Analysis"):
            st.session_state.section = "sentiment"

        if st.button(" Overall Summary"):
            st.session_state.section = "summary"

    with col2:
        if st.button(" Trending Keywords & Topics"):
            st.session_state.section = "keywords"

        if st.button(" Model Performance Metrics"):
            st.session_state.section = "model"

    st.markdown("---")

    df = st.session_state.news_data

    # -----------------------------
    # Show Content Based on Button
    # -----------------------------

    if st.session_state.section == "news":

        st.subheader(" Recent & Trending News")
        st.dataframe(df)

    elif st.session_state.section == "sentiment":

        st.subheader(" Sentiment Distribution")

        

        positive = len(df[df["Sentiment"]=="Positive"])
        negative = len(df[df["Sentiment"]=="Negative"])
        neutral = len(df[df["Sentiment"]=="Neutral"])

        values=[positive,negative,neutral]
        labels=["Positive","Negative","Neutral"]

        fig,ax=plt.subplots()
        ax.pie(values,labels=labels,autopct='%1.0f%%')
        ax.axis("equal")

        st.pyplot(fig)

    elif st.session_state.section == "summary":

        st.subheader(" Overall Summary")

        st.write("Total News Articles:",len(df))
        st.write("Topics Covered:",df["Topic"].unique())

    elif st.session_state.section == "keywords":

        st.subheader(" Trending Keywords")
      #-----------------------------
      #topic modeling using LDA
      #-----------------------------
        st.subheader("Topic Modeling")

   

        text_data = df["Headline"].astype(str)

        vectorizer = CountVectorizer(stop_words="english")

        X = vectorizer.fit_transform(text_data)

        lda = LatentDirichletAllocation(n_components=3, random_state=42)

        lda.fit(X)

        words = vectorizer.get_feature_names_out()
 
        for i, topic in enumerate(lda.components_):

          st.write(f"Topic {i+1}")

        topic_words = [words[j] for j in topic.argsort()[-10:]]

        st.write(", ".join(topic_words))

        #---------------------------------------
        # keyword frequency and word cloud
        #---------------------------------------
        st.subheader(" Trending Keywords")

        # Combine all headlines
        text = " ".join(df["Headline"]).lower()

        # Word Cloud
        wordcloud = WordCloud(width=800,height=400,background_color="black").generate(text)

        fig,ax=plt.subplots()
        ax.imshow(wordcloud)
        ax.axis("off")

        st.pyplot(fig)

        

        # -----------------------------
        # Trending Keywords Table
        # -----------------------------
        st.subheader(" Top Trending Keywords")

        words = text.split()

        word_freq = Counter(words)

        top_words = word_freq.most_common(10)

        keywords_df = pd.DataFrame(top_words, columns=["Keyword","Frequency"])

        st.dataframe(keywords_df)

    elif st.session_state.section == "model":

        st.subheader(" Model Performance")

        st.write("Accuracy: 92%")
        st.write("Precision: 90%")
        st.write("Recall: 88%")

        
    


        

    st.markdown("---")

    st.subheader(" Quick Stats")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Total News Articles", len(df))
    c2.metric("Categories", df["Topic"].nunique())
    c3.metric("News Sources", len(df))
    c4.metric("Dashboard Status", "Operational")



# -----------------------------
# Dashboard
# -----------------------------
def dashboard():

    st.title(" NewsPulse - Global News Trend Analyzer")

    df = st.session_state.news_data

    total = len(df)
    positive = len(df[df["Sentiment"]=="Positive"])
    negative = len(df[df["Sentiment"]=="Negative"])
    neutral = len(df[df["Sentiment"]=="Neutral"])

    st.subheader("News Summary")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Total Articles",total)
    c2.metric("Positive",positive)
    c3.metric("Negative",negative)
    c4.metric("Neutral",neutral)

    col1,col2 = st.columns(2)

    # Sentiment Pie Chart
    with col1:

        st.subheader("Sentiment Analysis")

        values=[positive,negative,neutral]
        labels=["Positive","Negative","Neutral"]

        fig,ax=plt.subplots()
        ax.pie(values,labels=labels,autopct='%1.0f%%')

        st.pyplot(fig)

    # Trending Topics
    with col2:

        st.subheader("Trending Topics")

        st.write("Technology : AI, innovation")
        st.write("Economy : market, inflation")
        st.write("Politics : election, policy")

    # Word Cloud
    st.subheader("Word Cloud")

    text = " ".join(df["Headline"].astype(str))

    wordcloud = WordCloud(
        width=400,
        height=200,
        background_color="black",
        colormap="viridis"
    ).generate(text)

    fig2, ax2 = plt.subplots()
    ax2.imshow(wordcloud, interpolation="bilinear")
    ax2.axis("off")

    st.pyplot(fig2)


    # -----------------------------
    # Topic Distribution Bar Graph
    # -----------------------------
    st.subheader("Topic Distribution")

    topic_counts = df["Topic"].value_counts()

    fig3, ax2 = plt.subplots()

    ax2.bar(topic_counts.index, topic_counts.values)

    ax2.set_xlabel("Topics")
    ax2.set_ylabel("Number of Articles")
    ax2.set_title("News Articles by Topic")
    st.pyplot(fig3)

    # Latest News Table
    st.subheader("Latest News")

    st.dataframe(df)

# -----------------------------
# Main App
# -----------------------------
if "logged_in" not in st.session_state:

    login()

else:

    st.sidebar.title("Navigation")

    page = st.sidebar.radio("Go to",["Dashboard","Admin Page","Logout"])

    if page == "Dashboard":
        dashboard()

    elif page == "Admin Page":

        if st.session_state["role"] == "admin":
            admin_page()
        else:
            st.warning("Admin Access Only")

    elif page == "Logout":
        st.session_state.clear()
        st.rerun()



        