import streamlit as st
from googletrans import Translator
from textblob import TextBlob

def main():
    st.title("Translator and Sentiment Analysis App")
    st.write("Built with Streamlit and Python")

    activities = ["Translator", "Sentiment Analysis"]
    choice = st.sidebar.selectbox("Select activity", activities)

    if choice == "Translator":
        from_text = st.text_input("Enter a sentence:")
        from_code = st.text_input("Enter a language code:")
        if st.button("Translate"):
            try:
                translator = Translator()
                translated_text = translator.translate(from_text, dest=from_code).text
                st.success(translated_text)
            except Exception as e:
                st.error("Translation Error: Please check your input and language code.")

    elif choice == "Sentiment Analysis":
        from_sent = st.text_input("Enter a sentence:")
        if st.button("Analyze"):
            br = TextBlob(from_sent)
            sentiment = br.sentiment.polarity
            if sentiment > 0:
                st.success("Positive Sentiment")
            elif sentiment == 0:
                st.info("Neutral Sentiment")
            else:
                st.error("Negative Sentiment")

if __name__ == "__main__":
    main()
