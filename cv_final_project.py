import streamlit as st
import numpy as np
from PIL import Image

def rgb_to_grayscale(image):
    # Convert an RGB image to grayscale using the luminosity method
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

def apply_convolution(image, kernel):
    # Manually apply a convolution kernel to an image
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    pad_height, pad_width = kernel_height // 2, kernel_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    convolved = np.zeros_like(image)
    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i+kernel_height, j:j+kernel_width]
            convolved[i, j] = np.sum(region * kernel)
    return convolved

def edge_detection_operator(image, operator='sobel', scale=1):
    if operator == 'sobel':
        sobel_x = np.array([[-1, 0, 1],
                            [-scale, 0, scale],
                            [-1, 0, 1]])
        
        sobel_y = np.array([[-1, -scale, -1],
                            [0, 0, 0],
                            [1, scale, 1]])
    elif operator == 'prewitt':
        sobel_x = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]])
        
        sobel_y = np.array([[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]])

    gray_image = rgb_to_grayscale(image)
    grad_x = apply_convolution(gray_image, sobel_x)
    grad_y = apply_convolution(gray_image, sobel_y)
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    magnitude = ((magnitude - magnitude.min()) * 255 / (magnitude.max() - magnitude.min())).astype(np.uint8)
    return grad_x,grad_y,magnitude

st.title("Edge Detection with Sobel and Prewitt Operators")

uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
scale = st.slider("Adjust Sobel Operator Magnitude", 1, 10, 1)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    image = np.array(image)

    sobel_x, sobel_y, sobel_edges = edge_detection_operator(image, 'sobel', scale)
    sobel_x_pil = Image.fromarray(sobel_x)
    sobel_y_pil = Image.fromarray(sobel_y)
    sobel_edges_pil = Image.fromarray(sobel_edges)
    
    prewitt_edges = edge_detection_operator(image, 'prewitt')[2]  # Taking only magnitude for prewitt
    prewitt_edges_pil = Image.fromarray(prewitt_edges)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(image, caption="Original Image", use_column_width=True)
    with col2:
        st.image(sobel_x, caption="Sobel X", use_column_width=True)
    with col3:
        st.image(sobel_y, caption="Sobel Y", use_column_width=True)
    with col4:
        st.image(sobel_edges, caption="Sobel Edges", use_column_width=True)
    with col5:
        st.image(prewitt_edges, caption="Prewitt Edges", use_column_width=True)
else:
    st.text("Upload an image to get started.")