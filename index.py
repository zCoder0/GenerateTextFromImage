import streamlit as st
from PIL import Image
from Model import ImageModel

# Set up the Tesseract path if needed (only for local Tesseract setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Path\to\tesseract.exe'
model = ImageModel()
st.title("Image to Text Bot ")
st.subheader("Upload an image and get the Generated text!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    gen_text = model.predict(image)
    st.write("Processing the image...")

    try:
       
        st.success("Here is the Generated text:")
        st.write(gen_text)

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("---")
