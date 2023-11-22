import streamlit as st
from streamlit_lottie import st_lottie
import os
from PIL import Image
import requests



dir = os.path.dirname(os.path.abspath(__file__))
static = os.path.join(dir,'assets')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# with open(os.path.join(static,'st.css')) as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# print('loaded styling')
# st.sidebar.image(os.path.join(static,'635b055453d8bb5a7852461d_Deloitte-Logo.png'), use_column_width=True)
# st.sidebar.image('https://logos-marques.com/wp-content/uploads/2020/12/Deloitte-logo.png', use_column_width=True)
st.sidebar.image('https://clipartcraft.com/images/deloitte-logo-transparent-4.png', use_column_width=True)
st.title('Welcome to the GI3 demo')
st.markdown("""<hr style="height:2px;border:none;color:#9ACD66;background-color:#9ACD66;" /> """, unsafe_allow_html=True)
st.write()
st.write("Please click **uploader** on the sidebar to proceed.")
st.write("---")
st.write("""The release of new Gi3 legislation in August 2023 created a surge in demand for technical reports in a different format for our clients.
 This sudden increase in workload resulted in resource constraints, which led to an evaluation of the potential for automation and standardisation opportunities using AI to expedite the report generation process.""")
st.write("""The goal of exploring these opportunities is to free up more time for our Gi3 team to concentrate on focused review and advisory work and explore the application of cutting-edge Artificial Intelligence (AI) solutions to alleviate a significant pain point for the Gi3 team.""")
st.write("This is an extremely early phase demonstration of what the GI3 tool could look like. It utilises an AutoGPT agent and Google Serper API and is written in Python.")
# with col2:
#     lottie_hello = load_lottieurl("https://cdnl.iconscout.com/lottie/premium/preview-watermark/ai-7299861-5975354.mp4?h=700")
#     st_lottie(lottie_hello, key="hello")