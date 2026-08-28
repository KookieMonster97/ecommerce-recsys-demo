import streamlit as st
import json

st.set_page_config(page_title="E-commerce Recommender Demo", layout="wide")

with open("sample_recommendations.json") as f:
    recommendations = json.load(f)

with open("sample_history.json") as f:
    history = json.load(f)

st.title("Shopping Cart E-commerce Recommendation System")
st.caption("Built with HDFS -> Hive -> R -> Spark (ALS Collaborative Filtering)")

st.divider()

user_ids = list(recommendations.keys())
selected_user = st.selectbox("Select a User ID to see their recommendations:", user_ids)

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"User {selected_user}'s History")
    user_history = history.get(selected_user, [])
    if user_history:
        for item in user_history[:15]:
            st.write(f"Item **{item['itemid']}** -- {item['event']}")
    else:
        st.write("No history found for this user.")

with col2:
    st.subheader(f"Recommended for User {selected_user}")
    user_recs = recommendations.get(selected_user, [])
    for rec in user_recs:
        st.write(f"Item **{rec['itemid']}** -- confidence score: {rec['score']}")

st.divider()
st.caption(f"Demo built on {len(user_ids)} sample users from a 2.76M-event RetailRocket e-commerce dataset")
