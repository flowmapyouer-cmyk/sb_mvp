import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="세컨부스트 협업 대시보드", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=2200, scrolling=True)
