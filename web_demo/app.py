import streamlit as st, requests, random

st.title("Creative Concierge (Mock)")

persona = st.selectbox("Force persona", ["auto","photo_first","vector_first","general_creator"])

if st.button("Get recommendation"):
    if persona == "auto":
        resp = requests.post("http://localhost:8000/classify",
                             json={"user_id":"demo","path":"/","ts":0})
        persona = resp.json()["persona"]
    st.success(f"Persona ➜ {persona}")
    st.image(f"https://placehold.co/600x300?text={persona}")
