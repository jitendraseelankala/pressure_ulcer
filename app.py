import streamlit as st
from PIL import Image

st.title("Pressure Ulcer Segmentation")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    st.success("Model prediction will appear here")
