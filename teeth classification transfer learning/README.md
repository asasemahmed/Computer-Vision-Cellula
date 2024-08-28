# Teeth Image Classification Project 😬🚀

This project focuses on classifying teeth images using a customized MobileNet model and a Support Vector Classifier (SVC).

## Project Overview 🎦

The project combines deep learning and traditional machine learning techniques to classify teeth images. It consists of two main components:

1. A modified MobileNet model for feature extraction
2. Add Dense leayers for final classification prediction 
3. An another SVC model for final classification (optinal model)

### Modified MobileNet

We use a pre-trained MobileNet model as a base, with customizations to the last few layers to adapt it for our specific teeth classification task.

### SVC Classifier

The convolutional layers of the MobileNet model are used to generate image representations. These representations are then fed into an SVC model for the final classification.

### Deployment

Deploy the model using streamlit lib for using in deffirent apps.

## Requirements

- Python 3.7+
- Jupyter Notebook
- TensorFlow 2.x
- Scikit-learn
- NumPy
- streamlit
- Matplotlib (for visualization)

## Usage

1. Prepare your dataset of teeth images.
2. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```

## Project Structure

```
├── notebooks/
│   ├── teeth_classification.ipynb
|   ├── app.py
|
└── README.md
```

