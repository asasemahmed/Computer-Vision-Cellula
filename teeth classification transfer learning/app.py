import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np


model = tf.keras.models.load_model(r'P:\python_test\teeth classification transfer learning\model_mobilnet.keras')

def preprocess_image(image):
    
    image = image.resize((224, 224))  
    image = np.array(image)
    image = image / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

st.title('Image Teeth Classifier')

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

classes = ['CaS', 'CoS', 'Gum', 'MC', 'OC', 'OLP', 'OT']

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    
    st.image(image, caption='Uploaded Image', use_column_width=True)

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction, axis=1)

    st.write(f"predicted class: {classes[predicted_class[0]]}")

