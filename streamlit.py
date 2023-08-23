from genericpath import isfile
from macpath import join
import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from io import BytesIO
import torch
import os
import detect
import numpy as np
from PIL import Image, ImageOps
import cv2
import json
import pathlib
import base64
st.set_page_config(page_title="Defect Detection in Motherboard",page_icon=":tada:",layout="wide")

title_style =""" <style>{
# color:Blue;
#font-size: 20px;
font-family:Cascdia Code;
}</style>"""
            


def imgInput():
    uploaded_file = st.file_uploader("Test Your Image Here...", type=['png', 'jpeg', 'jpg', 'JPG'])
    col1, col2 = st.columns(2)
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        with col1:
            
            file_path = os.path.abspath(os.path.join("Dataset/test/images",uploaded_file.name))
            command = r'python detect.py --source {} --weights runs/train/exp/weights/best.pt'.format(file_path)
            image = Image.open(file_path)
            new_image1 = image.resize((600, 400))
            return_value = os.popen(command).read()
            st.success(file_path)
            st.image(new_image1, caption='Uploaded image', use_column_width=True)
            
           
        with col2:
            path,str= detect.run(source=file_path)
            img_paths = os.path.join(path,uploaded_file.name)
            st.warning('Defects found in images: {}'.format(file_path))
            image1 = Image.open(img_paths)
            new_image2 = image1.resize((600, 400))
            st.image(new_image2,caption='Detected image',use_column_width=True)  
            st.write(str)
            
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    # -- Sidebarst.markdown(title_style, unsafe_allow_html=True)
    url = requests.get(
    "https://assets10.lottiefiles.com/packages/lf20_4kji20Y93r.json")
    url_json = dict()
  
    if url.status_code == 200:
        url_json = url.json()
    else:
       print("Error in the URL")
  
  
  
    st_lottie(url_json,reverse=True,
          # height and width of animation
          height=400,  
          width=400,
          # speed of animation
          speed=1,  
          # means the animation will run forever like a gif, and not as a still image
          loop=True,  
          # quality of elements used in the animation, other values are "low" and "medium"
          quality='high',
           # THis is just to uniquely identify the animation
          key='Animation' )
    st.write('<h1 style="color: Blue; font-size: 40px;">Defect Detection in Motherboard</h1>', unsafe_allow_html=True)
    st.write('<h3 style="color:Yellow; font-size: 25px;">here you can check the defects in the motherboard</h1>',unsafe_allow_html=True)
    st.sidebar.title('⚙️ Choose option')
    datasrc = st.sidebar.radio("Select input source.", ['From Device', 'From URL'])
    
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    
       
                
    # # option = st.sidebar.radio("Select input type.", ['DEVICE', 'URL'])
    # if torch.cuda.is_available():
    #     deviceoption = st.sidebar.radio("Select compute Device.", ['cpu', 'cuda'], disabled = False, index=1)
    # else:
    #     deviceoption = st.sidebar.radio("Select compute Device.", ['cpu', 'cuda'], disabled = True, index=0)
    # # -- End of Sidebar

    # st.header('Livestock Farming')
    # st.subheader('Select options left-haned menu bar.')
    # st.sidebar.markdown("https://github.com/thepbordin/Obstacle-Detection-for-Blind-people-Deployment")
    if datasrc == "From Device":    
        imgInput()
    elif datasrc == "From URL": 
        urlInput()


if __name__ == '__main__':
    main()
   
    st.markdown("""
              <style>
              body {
              background: #ff0099; 
              background: -webkit-linear-gradient(to right, #ff0099, #493240); 
              background: linear-gradient(to right, #ff0099, #493240); 
               }
              </style>
              """, unsafe_allow_html=True)