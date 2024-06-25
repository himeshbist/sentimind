import streamlit as st
import random
import time

def show():
    st.markdown("""
    <style>
    .big-font {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .medium-font {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    .stButton>button {
        display: block;
        margin: 0 auto;
        background-color: #4CAF50;
        color: white;
        padding: 15px 30px;
        text-align: center;
        text-decoration: none;
        font-size: 18px;
        border-radius: 15px;
        border: none;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }
    .stText>div>input, .stRadio>div>label {
        display: block;
        margin: 10px auto;
    }
    .account-section {
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .profile-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
    }
    .account-details {
        margin-left: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Your Account</p>', unsafe_allow_html=True)

    # New Account / Login Section
    account_status = st.radio("Account Status", ("Existing User", "New User"), horizontal=True)

    if account_status == "New User":
        st.markdown('<p class="medium-font">Create New Account</p>', unsafe_allow_html=True)
        new_username = st.text_input("Choose a username")
        new_email = st.text_input("Enter your email")
        new_password = st.text_input("Choose a password", type="password")
        if st.button("Create Account"):
            # Handle account creation logic
            st.success("Account created successfully! Please log in.")
            time.sleep(2)
            st.experimental_rerun()

    else:
        # User profile section
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.image(r"C:\Users\Himesh\Downloads\profile-pic (9).png", width=150, use_column_width=True)
        
        with col2:
            if 'username' not in st.session_state:
                st.session_state.username = "Himesh Bist"
            if 'email' not in st.session_state:
                st.session_state.email = "himesh_2312res299@iitp.ac.in"
            
            st.markdown(f'<p class="medium-font">{st.session_state.username}</p>', unsafe_allow_html=True)
            st.write("Member since: July 12, 2024")
            st.write(f"Email: {st.session_state.email}")
            if st.button("Edit Profile"):
                st.session_state.edit_profile = True

        if 'edit_profile' in st.session_state and st.session_state.edit_profile:
            st.markdown('<p class="medium-font">Edit Profile</p>', unsafe_allow_html=True)
            new_username = st.text_input("New Username", value=st.session_state.username)
            new_email = st.text_input("New Email", value=st.session_state.email)
            if st.button("Save Changes"):
                st.session_state.username = new_username
                st.session_state.email = new_email
                st.session_state.edit_profile = False
                st.success("Profile updated successfully!")
                st.experimental_rerun()

        # Account statistics
        st.markdown('<p class="medium-font">Your Activity</p>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("Analyses Performed", f"{random.randint(50, 200)}")
        col2.metric("Accuracy Score", f"{random.randint(85, 99)}%")
        col3.metric("Favorite Category", "Technology")

        # Recent activity
        st.markdown('<p class="medium-font">Recent Activity</p>', unsafe_allow_html=True)
        recent_activities = [
            "Analyzed tweet about AI advancements",
            "Performed sentiment analysis on product review",
            "Analyzed social media post about climate change",
            "Sentiment check on customer feedback"
        ]
        for activity in recent_activities:
            st.write(f"• {activity}")

        # Account settings
        st.markdown('<p class="medium-font">Account Settings</p>', unsafe_allow_html=True)
        settings_expander = st.expander("Manage Your Settings")
        with settings_expander:
            st.checkbox("Receive email notifications")
            st.checkbox("Two-factor authentication", value=True)
            st.select_slider("Privacy Level", options=["Public", "Friends", "Private"])
            st.color_picker("Choose your theme color")

        # Subscription info (assuming a freemium model)
        st.markdown('<p class="medium-font">Subscription</p>', unsafe_allow_html=True)
        if 'current_plan' not in st.session_state:
            st.session_state.current_plan = "Free"
        st.info(f"Current Plan: {st.session_state.current_plan}")
        if st.session_state.current_plan == "Free":
            if st.button("Upgrade to Premium"):
                st.session_state.upgrade_premium = True

        if 'upgrade_premium' in st.session_state and st.session_state.upgrade_premium:
            st.markdown('<p class="medium-font">Upgrade to Premium</p>', unsafe_allow_html=True)
            st.write("Premium features:")
            st.write("• Unlimited sentiment analyses")
            st.write("• Advanced analytics")
            st.write("• Priority support")
            if st.button("Confirm Upgrade"):
                st.session_state.current_plan = "Premium"
                st.session_state.upgrade_premium = False
                st.success("Successfully upgraded to Premium!")
                st.experimental_rerun()

        # Help and Support
        st.markdown('<p class="medium-font">Help & Support</p>', unsafe_allow_html=True)
        if st.button("Contact Support"):
            st.session_state.contact_form = True
            st.experimental_rerun()

        # Danger Zone
        st.markdown('<p class="medium-font">Danger Zone</p>', unsafe_allow_html=True)
        danger_expander = st.expander("Account Management")
        with danger_expander:
            st.write("Be careful with these actions!")
            if st.button("Reset Account"):
                st.warning("This will reset your account. Are you sure?")
            if st.button("Delete Account"):
                st.error("This will permanently delete your account. This action cannot be undone.")

def main():
    show()

if __name__ == "__main__":
    main()