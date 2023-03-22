import streamlit as st
import numpy as np
import cv2
from PIL import Image


part1, part2  = st.columns([0.8,0.2])
with part1:
    st.markdown('Upload your Image')

    
st.sidebar.markdown("Image Converter App")
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    part1, part2 = st.columns([0.5,0.5])
    
    with part1:
        st.markdown('Uploaded image')
        st.image(image,width=300)
        
    with part2:
        st.markdown('Changed image')
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

    