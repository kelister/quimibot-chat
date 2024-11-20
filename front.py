import streamlit as st
import pandas as pd
from chatbot import predict_class, get_response, intents

st.title("👨‍🔬Quimibot")


if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("¡Hola! Soy Quimibot, tu asistente para todo lo relacionado con la química. ¿En qué puedo ayudarte hoy?")

    st.session_state.messages.append({"role": "assistant", "content": "¡Hola! Soy Quimibot, tu asistente para todo lo relacionado con la química. ¿En qué puedo ayudarte hoy?"})
    st.session_state.first_message = False

if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    insts = predict_class(prompt)
    res = get_response(insts, intents)

    with st.chat_message("assistant"):
        st.markdown(res)

    st.session_state.messages.append({"role": "assistant", "content": res})