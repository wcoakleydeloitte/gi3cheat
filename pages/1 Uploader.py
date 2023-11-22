import streamlit as st
import time
import os

st.header('Transcript Upload')
st.markdown("""<hr style="height:2px;border:none;color:#9ACD66;background-color:#9ACD66;" /> """, unsafe_allow_html=True)
st.sidebar.image('https://clipartcraft.com/images/deloitte-logo-transparent-4.png', use_column_width=True)
st.write("AutoGPT will scrape the web using Google Serper API to answer its own questions.")

with st.container():
    file = st.file_uploader('Submit a file',type=['txt','docx'],accept_multiple_files=True)
    if file:
        st.write('File submitted!')

        with st.spinner('Waiting...'):
            time.sleep(2)
        st.success('Done!')
        with st.spinner('Processing with GPT 3.5...'):
            time.sleep(2)
        st.success('Done!')
if file:
    for i in range(len(file)):
        bytes_data = file[i].read()  # read the content of the file in binary
        print(file[i].name, bytes_data)
        with open("./assets"+file[i].name, "wb") as f:
            f.write(bytes_data)

    with st.spinner('Starting...'):
            time.sleep(2)
    with st.spinner('Self-learning...'):
        time.sleep(2)
    with st.spinner('Scanning the web...'):
        time.sleep(5)
    with st.spinner('Building output report...'):
        time.sleep(5)

    st.write('Complete!')