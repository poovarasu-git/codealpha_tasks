
# Handwritten Character Recognition

This project implements a convolutional neural network (CNN) to recognize handwritten English alphabets (A–Z) using the EMNIST dataset.


---# Task 1: Handwritten Character Recognition

👤 **Submitted by:**  
Poovarasan D.  
📧 dpoo.aiml2024@rmd.ac.in  
🎓 CodeAlpha Internship (May–June 2025)

## 📌 Project Overview
This project detects and recognizes handwritten alphabet characters using a Convolutional Neural Network (CNN). It processes image inputs and maps them to corresponding characters.

## 🚀 How to Run
1. Install dependencies:  
   `pip install -r requirements.txt`

2. Run the training script or load the saved model.

3. Use the interface (if any) or run prediction code to classify new handwritten input images.

## 📁 Files Included
- `code/` – source code and model training scripts  
- `model/` – trained CNN model  
- `README.md` – this file


## Features
- Trains a CNN on EMNIST letter dataset
- Predicts handwritten character from an image
- Streamlit web interface for demo (optional)

## Setup Instructions
```bash
pip install -r requirements.txt
python src/train_model.py
python src/predict.py
streamlit run app.py  # optional
```

## Dataset
Download EMNIST Letters dataset from: https://www.nist.gov/itl/products-and-services/emnist-dataset
