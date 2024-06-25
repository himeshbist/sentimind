import streamlit as st
import random
from datetime import datetime, timedelta

def generate_random_post():
    topics = ["AI", "Climate Change", "Space Exploration", "Quantum Computing", "Renewable Energy"]
    sentiments = ["Positive", "Negative", "Neutral"]
    return {
        "topic": random.choice(topics),
        "sentiment": random.choice(sentiments),
        "likes": random.randint(100, 10000),
        "comments": random.randint(10, 1000),
        "time": datetime.now() - timedelta(hours=random.randint(1, 24))
    }

def show():
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .post-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .topic {
        color: #1e88e5;
        font-size: 20px;
        font-weight: bold;
    }
    .sentiment {
        font-size: 16px;
        font-weight: bold;
    }
    .sentiment-positive {
        color: #4caf50;
    }
    .sentiment-negative {
        color: #f44336;
    }
    .sentiment-neutral {
        color: #ff9800;
    }
    .engagement {
        color: #616161;
        font-size: 14px;
    }
    .stButton>button {
        background-color: #1e88e5;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1565c0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Trending Topics</p>', unsafe_allow_html=True)

    # Initialize session state for posts if not exists
    if 'posts' not in st.session_state:
        st.session_state.posts = [generate_random_post() for _ in range(5)]

    # Button to refresh trending topics
    if st.button("Refresh Trending Topics"):
        st.session_state.posts = [generate_random_post() for _ in range(5)]
        st.success("Trending topics refreshed!")

    # Display posts
    for i, post in enumerate(st.session_state.posts):
        with st.container():
            st.markdown(f"""
            <div class="post-box">
                <p class="topic">{post['topic']}</p>
                <p class="sentiment sentiment-{post['sentiment'].lower()}">{post['sentiment']} Sentiment</p>
                <p class="engagement">❤️ {post['likes']} Likes | 💬 {post['comments']} Comments</p>
                <p class="engagement">🕒 {post['time'].strftime('%I:%M %p')}</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            
            if col1.button(f"👍 Like", key=f"like_{i}"):
                st.session_state.posts[i]['likes'] += 1
                st.success(f"You liked the post about {post['topic']}!")
                st.experimental_rerun()
            
            if col2.button(f"💬 Comment", key=f"comment_{i}"):
                st.session_state[f"commenting_{i}"] = True

            if col3.button(f"📊 Analyze", key=f"analyze_{i}"):
                st.info(f"Detailed sentiment analysis for '{post['topic']}' will be shown here.")

        # Comment section
        if st.session_state.get(f"commenting_{i}", False):
            comment = st.text_area("Write your comment:", key=f"comment_text_{i}")
            if st.button("Post Comment", key=f"post_comment_{i}"):
                st.session_state.posts[i]['comments'] += 1
                st.success("Your comment has been posted!")
                st.session_state[f"commenting_{i}"] = False
                st.experimental_rerun()

    # Filter and sort options
    st.sidebar.markdown("## Filter and Sort")
    filter_sentiment = st.sidebar.multiselect("Filter by Sentiment", ["Positive", "Negative", "Neutral"])
    sort_by = st.sidebar.selectbox("Sort by", ["Most Liked", "Most Commented", "Most Recent"])

    if st.sidebar.button("Apply Filters"):
        filtered_posts = [post for post in st.session_state.posts if post['sentiment'] in filter_sentiment]
        if sort_by == "Most Liked":
            filtered_posts.sort(key=lambda x: x['likes'], reverse=True)
        elif sort_by == "Most Commented":
            filtered_posts.sort(key=lambda x: x['comments'], reverse=True)
        else:  # Most Recent
            filtered_posts.sort(key=lambda x: x['time'], reverse=True)
        st.session_state.posts = filtered_posts
        st.success("Filters applied successfully!")
        st.experimental_rerun()

if __name__ == "__main__":
    show()