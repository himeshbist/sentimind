import streamlit as st
import pickle
import time
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the model
model = pickle.load(open(r'C:\Users\Himesh\Downloads\twitter_sentiment.pkl', 'rb'))

# Set the page config
st.set_page_config(
    page_title="Pondering",
    page_icon=":thought_balloon:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Google Analytics
st.markdown(
    f"""
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{os.getenv('analytics_tag')}');
    </script>
    """,
    unsafe_allow_html=True
)

# Custom CSS
st.markdown("""
<style>
/* Add your custom CSS here */
.stApp {
    background-color: #002244;
    text-align: center;
    font-family: Arial, sans-serif;
}
/* ... (rest of your CSS) ... */
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title='Pondering ',
        options=['Home', 'Account', 'Trending', 'Your Posts', 'About', 'Buy me a coffee'],
        icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill', 'cup-hot-fill'],
        menu_icon='chat-text-fill',
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": 'black'},
            "icon": {"color": "white", "font-size": "23px"},
            "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Page content
if selected == "Home":
    st.header("Sentiment Analysis")
    st.write("Enter a text to analyze its sentiment!")

    tweet_input = st.text_input(
        "Text:",
        placeholder="Type your text here...",
        max_chars=280,
        help="Enter a text to analyze its sentiment"
    )

    submit_button = st.button("Analyze Sentiment", help="Click to analyze the sentiment of the text")

    prediction_output = st.container()

    if submit_button:
        start_time = time.time()
        if tweet_input:
            prediction = model.predict([tweet_input])[0]
            end_time = time.time()
            
            with prediction_output:
                st.write(f"**Prediction:** {prediction}")
                st.write(f"**Time taken:** {round(end_time - start_time, 2)} seconds")
                if prediction == 'Negative':
                    st.error("Negative Sentiment 😔")
                elif prediction == 'Positive':
                    st.success("Positive Sentiment 😊")
                else:
                    st.warning("Neutral Sentiment 😐")
        else:
            st.error("Please enter a text!")

elif selected == "Account":
    st.header("Account")
    # Add account functionality here

elif selected == "Trending":
    st.header("Trending")
    # Add trending functionality here

elif selected == "Your Posts":
    st.header("Your Posts")
    # Add user posts functionality here

elif selected == "About":
    st.header("About")
    # Add about page content here

elif selected == "Buy me a coffee":
    st.header("Buy me a coffee")
    # Add donation functionality here

# Contact Developer button
st.markdown("""
<a href="contact.html" target="_blank">
  <button class="stButton">Contact Developer</button>
</a>
""", unsafe_allow_html=True)