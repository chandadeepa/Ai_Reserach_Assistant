
import streamlit as st

st.title("AI Research Assistant")

topic = st.text_input("Enter Topic")

if st.button("Search"):

    if topic.lower() == "india":
        st.subheader("Research Summary")
        st.write("India is a country in South Asia. It is the seventh-largest country in the world.")

    elif topic.lower() == "python":
        st.subheader("Research Summary")
        st.write("Python is a popular programming language used for AI, web development, and data science.")

    elif topic.lower() == "machine learning":
        st.subheader("Research Summary")
        st.write("Machine Learning is a branch of Artificial Intelligence that allows computers to learn from data.")

    elif topic.lower() == "ai":
        st.subheader("Research Summary")
        st.write("Artificial Intelligence is the simulation of human intelligence by machines.")

    else:
        st.write("Topic not available")