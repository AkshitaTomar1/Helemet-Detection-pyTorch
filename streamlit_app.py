import streamlit as st
from helmet.pipeline.prediction_pipeline import PredictionPipeline
import base64

st.set_page_config(page_title="Helmet Detection", layout="centered")
st.title("🪖 Helmet Detection Web App")
st.markdown("Upload an image to detect helmets using your trained model.")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Convert file to bytes
    image_data = uploaded_file.read()

    with st.spinner("Running prediction..."):
        try:
            # Initialize pipeline and run prediction
            pipeline = PredictionPipeline()
            result_image_base64 = pipeline.run_pipeline(image_data)

            # Convert base64 to displayable image
            result_image_str = result_image_base64.decode("utf-8")
            result_image_uri = f"data:image/jpeg;base64,{result_image_str}"

            st.success("Prediction completed!")
            st.image(result_image_uri, caption="Prediction Result", use_column_width=True)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
