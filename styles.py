import streamlit as st

def apply_styles():
    st.markdown(
        """
        <style>
        body {
            background-color: #e6f2ff; /* Change the background color */
            font-family: Arial, sans-serif; /* Change the font */
        }
        .post-title {
            font-size: 24px;
            color: #333;
        }
        .post-content {
            font-size: 16px;
            color: #666;
        }
        .post-date {
            font-size: 14px;
            color: #999;
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
        """,
        unsafe_allow_html=True
    )