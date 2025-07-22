import os, requests, streamlit as st

CLASSIFIER_URL = os.getenv("CLASSIFIER_URL", "http://localhost:8000")

st.title("Creative Concierge (Mock)")

persona = st.selectbox(
    "Force persona (or pick auto)",
    ["auto", "photo_first", "vector_first", "general_creator"],
)

if st.button("Get recommendation"):
    if persona == "auto":
        resp = requests.post(
            f"{CLASSIFIER_URL}/classify",
            json={"user_id":"demo","path":"/","ts":0},
            timeout=5,
        )
        persona = resp.json()["persona"]

    st.success(f"Persona ➜ **{persona}**")
    HERO = {
        "photo_first":"Lightroom+Hero",
        "vector_first":"Illustrator+Hero",
        "general_creator":"Creative+Cloud+Hero"
    }.get(persona, "Creative+Cloud+Hero")
    st.image(f"https://placehold.co/600x300?text={HERO}")
