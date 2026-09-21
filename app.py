import streamlit as st

st.set_page_config(
    page_title="Friends Reunion - Batch 2002",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own chrome (menu, footer, header, padding) and stretch
# the embedded invitation to fill the entire browser window instead of
# sitting inside a small boxed iframe.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
        iframe {
            position: fixed !important;
            top: 0; left: 0;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.iframe(html_content, height="stretch")
