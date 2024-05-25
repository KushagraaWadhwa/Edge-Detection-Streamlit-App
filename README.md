# Edge Detection Streamlit App

This repository contains a Streamlit web application for performing edge detection on images using Sobel and Prewitt operators. Users can upload an image and adjust the magnitude of the Sobel operator to see real-time edge detection results. The application demonstrates the process of converting an image to grayscale, applying convolution with edge detection kernels, and visualizing the results.

## Features

- **Image Upload:** Upload images in PNG, JPG, or JPEG format.
- **Grayscale Conversion:** Convert the uploaded image to grayscale using the luminosity method.
- **Edge Detection:** Apply Sobel and Prewitt edge detection operators to the grayscale image.
- **Adjustable Sobel Operator Magnitude:** Adjust the magnitude of the Sobel operator to see its effect on edge detection.
- **Result Visualization:** View the original image, Sobel operator results in X and Y directions, combined Sobel edges, and Prewitt edges side-by-side.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/edge-detection-app.git
   cd edge-detection-app
   ```

2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App:**
   ```sh
   streamlit run app.py
   ```

## Usage

1. Open the Streamlit app in your web browser.
2. Upload an image by clicking on "Choose an image..." and selecting a file from your computer.
3. Adjust the Sobel operator magnitude using the slider.
4. View the results displayed side-by-side:
   - Original Image
   - Sobel X
   - Sobel Y
   - Sobel Edges
   - Prewitt Edges

## Dependencies

- `streamlit`
- `numpy`
- `pillow`

These dependencies are listed in the `requirements.txt` file and will be installed when you follow the installation steps.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. 
