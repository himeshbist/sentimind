import streamlit as st
from streamlit_option_menu import option_menu
import os

from dotenv import load_dotenv

# Import all your page modules
import home, account, trending, about
from styles import apply_styles

# Import the contact module
import contact

# Import the your_posts module
import your_posts

# Load environment variables
load_dotenv()

# Set the page config
st.set_page_config(
    page_title="Sentimind",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
apply_styles()

# Google Analytics
st.markdown(
    f"""
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={os.getenv('ANALYTICS_TAG')}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{os.getenv('ANALYTICS_TAG')}');
    </script>
    
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title='Sentimind',
        options=['Home', 'Account', 'Trending', 'Your Posts', 'About', 'Contact'],
        icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill', 'envelope-fill'],
        menu_icon='chat-text-fill',
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": 'black'},
            "icon": {"color": "white", "font-size": "23px"},
            "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Initialize session state for contact form
if 'contact_form' not in st.session_state:
    st.session_state.contact_form = False

# Page content
if selected == "Home":
    home.show()
elif selected == "Account":
    if st.session_state.contact_form:
        contact.show()
    else:
        account.show()
elif selected == "Trending":
    trending.show()
elif selected == "Your Posts":
    your_posts.show()
elif selected == "About":
    about.show()
elif selected == "Contact":
    contact.show()