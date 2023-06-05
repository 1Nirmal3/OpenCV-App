import streamlit as st
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
    background-image: url("data:image/jpeg;base64,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");
    background-size:cover;
    }}

[data-testid = "stSidebar"]{{
    background-color: #C8EAF2;
    background-repeat: no repeat;
    }}
[data-testid="stHeader"]{{
    background-color: #B3EAF4;
    background-repeat: no repeat;
    }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

import numpy as np
import cv2
from PIL import Image

st.title('Image Converter Application')


part1, part2  = st.columns([0.8,0.2])
with part1:
    st.markdown('Upload your Image here by clicking Browse Files button given below.')

    
st.sidebar.subheader("Image Conversion Application using OpenCV and PIL")
st.sidebar.info("This application is designed to convert your image to the desired outcome based on the choices selected by the user. Upload your Image for Conversion.")
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    part1, part2 = st.columns([0.5,0.5])
    
    with part1:
        st.markdown('Uploaded image')
        st.image(image,width=300)
        
    with part2:
        st.markdown('Changed image')
        st.sidebar.write("Select below for desired Image to be converted.")
        filter = st.sidebar.radio('Convert your photo:',['Original','Gray Image','Black and White','Gray Image(1/2 Size)','Gray Image(1/4 Size)'])
        if filter == 'Gray Image':
            img = np.array(image.convert('RGB'))
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            st.image(gray_img, width=300)
        elif filter == 'Black and White':
            img = np.array(image.convert('RGB'))
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            slider = st.sidebar.slider('Alter the intensity', 1, 255, 0, step=1)
            (thresh, blackAndWhiteImage) = cv2.threshold(gray_img, slider, 255, cv2.THRESH_BINARY)
            st.image(blackAndWhiteImage, width=300)
        elif filter == 'Gray Image(1/2 Size)':
            img = np.array(image.convert('RGB'))
            resized_image = cv2.resize(img,None,fx=0.5, fy=0.5)
            gray_img = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)
            st.image(gray_img,width=225)
        elif filter == 'Gray Image(1/4 Size)':
            img = np.array(image.convert('RGB'))
            resized_image = cv2.resize(img,None,fx=0.25, fy=0.25)
            gray_img = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)
            st.image(gray_img,width=150)
        else: 
            st.image(image, width=300)
st.sidebar.title(' ') #Used to create some space between the filter widget and the comments section
st.sidebar.markdown(' ') #Used to create some space between the filter widget and the comments section
st.sidebar.write("Hope You like it :smiley: ")
    