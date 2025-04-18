import streamlit as st
import torch
import cv2
from PIL import Image
import numpy as np

# Load your model
model = torch.load('your_model.pt', map_location=torch.device('cpu'))
model.eval()

st.title("Helmet Detection App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert PIL to tensor
    image_tensor = ...  # your image preprocessing logic
    with torch.no_grad():
        output = model(image_tensor.unsqueeze(0))

    # Visualize results (draw boxes)
    result_img = ...  # draw bounding boxes on original image
    st.image(result_img, caption="Detection Result", use_column_width=True)
