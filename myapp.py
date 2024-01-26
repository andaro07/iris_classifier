import streamlit as st
import pickle

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url(" https://unsplash.com/photos/dqBIJOBJjkk/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8N3x8aXJpcyUyMGZsb3dlciUyMGRhcmt8ZW58MHx8fHwxNzA2MjgzMDgwfDA&force=true");
background-size: cover;
}


"""

st.markdown(page_bg_img, unsafe_allow_html=True)


from pred_page import show_page

show_page()