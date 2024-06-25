import streamlit as st
from PIL import Image

def show():
    # Custom CSS to style the page
    st.markdown("""
    <style>
        .big-font {
            font-family: 'Open Sans', sans-serif;
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
        }
        .medium-font {
            font-family: 'Roboto', sans-serif;
            font-size: 24px;
            font-weight: bold;
            color: #34495e;
        }
        .highlight {
            background: linear-gradient(to right, #f1c40f, #e67e22);
            padding: 30px;
            border-radius: 10px;
            color: #fff;
        }
        .team-member {
            background-color: #f8f8f8;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .team-member:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .team-member img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 10px;
        }
        .team-member h3 {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .team-member p {
            font-size: 14px;
            color: #666;
        }
        
        .social-links {
            text-align: center;
            margin-top: 30px;
        }

        .social-links a {
            margin: 0 15px;  /* Space between icons */
            font-size: 30px; /* Adjust icon size as needed */
            color: #333;     /* Default icon color */
            transition: color 0.3s ease; /* Smooth color transition on hover */
        }

        .social-links a:hover {
            color: #f1c40f; /* Change color on hover */
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<p class="big-font">About SentiMind: Your Emotion Intelligence Partner</p>', unsafe_allow_html=True)

    # Subheader
    st.markdown('<p class="medium-font">Unlocking the Power of Words, One Sentiment at a Time</p>', unsafe_allow_html=True)

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="highlight">
        SentiMind is your gateway to understanding the emotions behind every word. Our cutting-edge sentiment analysis tool harnesses the power of artificial intelligence to decode the hidden sentiments in text, giving you unprecedented insights into human emotions.
        
        Whether you're a business looking to understand customer feedback, a researcher analyzing social media trends, or an individual curious about the emotional tone of your writing, SentiMind is here to illuminate the path.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        image = Image.open(r"C:\Users\Himesh\Downloads\Designer.png")
        st.image(image, caption='Decoding Emotions', use_column_width=True)

    # Features section
    st.markdown('<p class="medium-font">🚀 Key Features</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
        - 🎯 **Precise Sentiment Analysis**: Accurately categorize text as positive, negative, or neutral.
        - 📊 **Detailed Analytics**: Get in-depth insights with our comprehensive sentiment reports.
        - ⚡ **Real-time Processing**: Analyze text on-the-fly for immediate results.
        """)

    with col2:
        st.write("""
        - 🌐 **Multi-language Support**: Analyze sentiments across multiple languages.
        - 🔒 **Privacy-focused**: Your data security is our top priority.
        - 🔧 **Customizable**: Tailor the analysis to your specific needs.
        """)

    # How it works section
    st.markdown('<p class="medium-font">🧠 How It Works</p>', unsafe_allow_html=True)
    st.write("""
    1. **Input**: Paste your text or upload a document.
    2. **Analysis**: Our AI processes the content, identifying emotional cues.
    3. **Results**: Receive a detailed breakdown of sentiments and emotions.
    4. **Insights**: Use our visualizations to understand the emotional landscape of your text.
    """)

    # Call to action
    st.markdown('<p class="medium-font">Ready to Decode Emotions?</p>', unsafe_allow_html=True)
    
    # Button to Navigate to "home.py"
    if st.button('Try SentiMind Now!'):
        st.experimental_rerun()  # Rerun the app


    # Team display section
    col1, col2, col3, col4, col5 = st.columns(5)
    team_images = [r"C:\Users\Himesh\Downloads\profile-pic (4).png",r"C:\Users\Himesh\Downloads\profile-pic (7).png", r"C:\Users\Himesh\Downloads\profile-pic (6).png", r"C:\Users\Himesh\Downloads\profile-pic (5).png", r"C:\Users\Himesh\Downloads\profile-pic (8).png"]
    team_names = ["Himesh Bist", "Tariq", "Meraj", "Badal", "Hirdesh"]
   
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            image = Image.open(team_images[i])
            st.image(image, width=120)
            st.write(f"**{team_names[i]}**")
            

    st.write("""
    Our diverse team is united by a passion for bridging the gap between language and emotion. 
    Together, we've created SentiMind - a tool that's not just technologically advanced, 
    but also intuitive and impactful for our users.
    """)
     # Social links at the bottom
    st.markdown('<div class="social-links">', unsafe_allow_html=True)
    st.markdown('<a href="https://www.instagram.com/your_instagram/" target="_blank"><i class="fab fa-instagram"></i></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/your_github/" target="_blank"><i class="fab fa-github"></i></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://wa.me/your_whatsapp_number" target="_blank"><i class="fab fa-whatsapp"></i></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    show()