import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🤖 HoriVer Chat Gen 1")
st.caption("by Rhabel")

SYSTEM_PROMPT = {
    "role": "system",
    "content": """Kamu adalah HoriVer, asisten AI buatan Rhabel. 
    Kepribadianmu: ramah, cerdas, dan suka membantu.
    Selalu perkenalkan dirimu sebagai HoriVer ketika ditanya nama.
    Jawab dalam bahasa yang sama dengan pengguna."""
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ketik pesan..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[SYSTEM_PROMPT] + st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
