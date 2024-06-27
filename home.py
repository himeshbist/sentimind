import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from textblob import TextBlob
from wordcloud import WordCloud
import pickle
import time
import logging
 
 
def load_model():
    model_path = "model/twitter_sentiment.pkl"
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
            logging.info("Model loaded successfully.")
            return model
    except (FileNotFoundError, pickle.UnpicklingError) as e:
        logging.error(f"Error loading model: {e}")
        st.error(f"Error loading model. Please check the file path and integrity.")
        return None 
    
model = load_model()

def analyze_text(model, text):
    if not model:
        st.error("Model is not available.")
        return None, None, None

    if not text.strip():
        st.warning("Input text is empty. Please enter valid text.")
        return None, None, None

    start_time = time.time()
    try:
        prediction = model.predict([text])[0]
    except Exception as e:
        st.error(f"Error during sentiment prediction: {str(e)}")
        return None, None, None
    end_time = time.time()

    sentiment_score = TextBlob(text).sentiment.polarity

    return prediction, round(end_time - start_time, 2), sentiment_score

def show():
    st.markdown("""
    <style>
    body {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        background-color: #2C2C2C;
        color: #FFFFFF;
        border-radius: 10px;
    }
    .stTextArea>div>div>textarea {
        background-color: #2C2C2C;
        color: #FFFFFF;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🔮 Sentiment Analysis Wizard")

    tab1, tab2 = st.tabs(["✨ Direct Input", "📁 Upload File"])

    with tab1:
        st.header("Analyze Text")
        with st.expander("How to Use"):
            st.write("1. Enter text in the input box below.")
            st.write("2. Click the 'Analyze Sentiment' button.")
            st.write("3. Read the sentiment prediction and the time taken for analysis.")

        tweet_input = st.text_area(
            "Text:",
            placeholder="Type your text here...",
            height=150,
            max_chars=5000,
            help="Enter a text to analyze its sentiment"
        )

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submit_button = st.button("🔍 Analyze Sentiment", help="Click to analyze the sentiment of the text")

        prediction_output = st.container()

        if submit_button:
            if tweet_input:
                try:
                    prediction, analysis_time, sentiment_score = analyze_text(model, tweet_input)
                    with prediction_output:
                        if prediction is not None:
                            st.write(f"**Prediction:** {prediction}")
                            st.write(f"**Time taken:** {analysis_time} seconds")
                            st.write(f"**Sentiment Score:** {sentiment_score}")
                          
                            # Add a cool word cloud
                            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(tweet_input)
                            fig, ax = plt.subplots()
                            ax.imshow(wordcloud, interpolation='bilinear')
                            ax.axis('off')
                            st.pyplot(fig)
                        else:
                            st.error("Error in sentiment analysis. Prediction is None.")
                except Exception as e:
                    st.error(f"Error in sentiment analysis: {str(e)}")
            else:
                st.error("Please enter a text!")

    with tab2:
        st.header("Upload a File")
        with st.expander("Instructions:"):
            st.write("1. Upload a `.txt` or `.csv` file containing one text entry per line.")
            st.write("2. The tool will analyze the sentiment of each entry.")

        uploaded_file = st.file_uploader("Choose a file", type=['txt', 'csv'])
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                    text_column = st.selectbox("Select the text column:", df.columns)
                    texts = df[text_column].tolist()
                else:
                    texts = uploaded_file.read().decode("utf-8").splitlines()

                predictions = []
                analysis_times = []
                sentiment_scores = []
                for text in texts:
                    prediction, analysis_time, sentiment_score = analyze_text(model, text)
                    predictions.append(prediction)
                    analysis_times.append(analysis_time)
                    sentiment_scores.append(sentiment_score)

                df = pd.DataFrame({"Text": texts, "Sentiment": predictions, "Sentiment Score": sentiment_scores})
                st.write(df)

                # Interactive Visualization
                fig = px.pie(df, names='Sentiment', title='Sentiment Distribution')
                st.plotly_chart(fig)

                st.write(f"**Average Time per Analysis:** {sum(analysis_times)/len(analysis_times):.2f} seconds")

                # Add a cool heatmap of sentiment over time
                if 'Timestamp' not in df.columns:
                    df['Timestamp'] = pd.date_range(start='1/1/2023', periods=len(df), freq='D')
                fig = px.density_heatmap(df, x='Timestamp', y='Sentiment Score', nbinsy=20, 
                                         title='Sentiment Heatmap Over Time')
                st.plotly_chart(fig)

            except Exception as e:
                st.error(f"An error occurred while processing the file: {e}")

if __name__ == "__main__":
    show()