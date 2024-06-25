import streamlit as st

def show(from_account=False):
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
        border: none;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Contact Support</p>', unsafe_allow_html=True)

    if from_account:
        if st.button("Back to Account"):
            st.session_state.contact_form = False
            st.experimental_rerun()

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.text_input("Subject")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        # Here you would typically handle sending the message
        # For now, we'll just show a success message
        st.success("Your message has been sent! We'll get back to you soon.")
        if from_account:
            st.session_state.contact_form = False
            st.experimental_rerun()

if __name__ == "__main__":
    show()