import streamlit as st
import pandas as pd
from PIL import Image

def show():
    st.title("Your Posts")
    st.image(r"C:\Users\Himesh\Downloads\Designer (2).png", width=100)  # Replace with the correct image path

    # Display a list of user's posts with some styling
    posts = [
        {"title": "Post 1", "content": "This is a positive post about the weather. It's sunny and beautiful outside!"},
        {"title": "Post 2", "content": "I'm so frustrated with this slow internet connection. It's driving me crazy!"},
        {"title": "Post 3", "content": "This movie was amazing! I highly recommend it to everyone."},
    ]

    for post in posts:
        with st.container():
            st.subheader(post["title"])
            st.write(post["content"])

    # Add options to create, edit, or delete posts with images
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Create New Post", key="create_post_btn"):
            st.write("Create New Post functionality to be implemented.")
        st.image(r"C:\Users\Himesh\Downloads\Designer (4).png", width=30)  # Replace with the correct image path

    with col2:
        if st.button("Edit Post", key="edit_post_btn"):
            st.write("Edit Post functionality to be implemented.")
        st.image(r"C:\Users\Himesh\Downloads\Designer (3).png", width=30)  # Replace with the correct image path

    with col3:
        if st.button("Delete Post", key="delete_post_btn"):
            st.write("Delete Post functionality to be implemented.")
        st.image(r"C:\Users\Himesh\Downloads\Designer (5).png", width=30)  # Replace with the correct image path

    # Display Sentiment Analysis Results with images
    st.markdown("---")
    st.header("Sentiment Analysis Results")
    st.image(r"C:\Users\Himesh\Downloads\Designer (6).png", width=100)  # Replace with the correct image path

    sentiment_data = {
        "Post Title": ["Post 1", "Post 2", "Post 3"],
        "Sentiment": ["Positive", "Negative", "Positive"]
    }

    df = pd.DataFrame(sentiment_data)
    st.dataframe(df.style.set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#0a308a'), ('color', 'white')]
    }]))

    # Add more information with styling and images
    st.write("**What is Sentiment Analysis?**")
    st.write("Sentiment analysis is a technique used to determine the emotional tone of text data.")
    st.image(r"C:\Users\Himesh\Downloads\Designer (7).png", width=200)  # Replace with the correct image path

    st.write("**Benefits of Sentiment Analysis:**")
    st.write("- **Gain insights into customer opinions:** Analyze customer reviews and social media posts.")
    st.write("- **Improve marketing strategies:** Identify trends and preferences.")
    st.write("- **Monitor brand reputation:** Track sentiment across different platforms.")

    st.write("**How Sentiment Analysis is Used on This Website:**")
    st.write("We use sentiment analysis to analyze your posts and provide insights into the overall sentiment.")
    st.image(r"C:\Users\Himesh\Downloads\Designer (8).png", width=200)  # Replace with the correct image path

# Run the Streamlit app
if __name__ == "__main__":
    show()