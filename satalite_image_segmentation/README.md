# Satalite Image Segmentation Project 🚀

This project focuses on image segmentation using autoencoder with MobelNet and U-Net.

## Project Overview 🎦

The project combines deep learning models to segment images:

1. A modified MobileNet model for feature extraction
2. Add Decoder layers to up sample images and creat mask
3. An U-Net model to encode and decode images with skip connection layers

### Modified MobileNet And Building Decoder 

We use a pre-trained MobileNet model as a encoder model to extract features.
building decoder model with ConvTranspose layers to upsample image again and creat segmented mask.

### Building U-Net model

we used U-Net archtichure a Common model for image segmentation task to compare between two models.

## Requirements

- Python 3.7+
- Jupyter Notebook
- TensorFlow 2.x
- pytifflib
- NumPy
- Matplotlib (for visualization)

## Usage

1. Prepare your dataset of teeth images.
2. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```

## Project Structure

```
├── satalite_segmentation.ipynb
|
└── README.md
```
