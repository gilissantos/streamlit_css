import streamlit as st

st.set_page_config(page_title="Streamlit com CSS3", page_icon="css3.png")

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


st.title("Título", anchor="titulo")

st.header("subtítulo", anchor="subtitulo")

st.write("Você pode personalizar a estilização das suas aplicações do streamlit com CSS.")

st.button("botão com formatação css")

