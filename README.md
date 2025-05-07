# NLP Feedback Analyzer

A simple Natural Language Processing (NLP) app to analyze user feedback and extract sentiment and key themes, built using Python, Streamlit, and Hugging Face Transformers.

## 🧠 Project Overview

This project demonstrates a basic pipeline for sentiment analysis using pre-trained NLP models. The goal is to simulate how businesses might automatically extract insights from customer feedback using AI.

Users can:
- Upload a `.csv` file containing textual feedback
- Automatically classify sentiment (positive, neutral, negative)
- View summary statistics and sample predictions
- Visualize sentiment distribution using matplotlib/seaborn

## 🛠️ Tools & Technologies

- **Python 3**
- **Pandas** for data handling
- **Transformers (Hugging Face)** for NLP sentiment analysis
- **Matplotlib / Seaborn** for data visualization
- **Streamlit** for the interactive web interface

## 🧪 Sample Workflow

1. Prepare a CSV file with a column named `text` containing customer feedback.
2. Upload the file using the Streamlit interface.
3. The model will classify each feedback item.
4. Visual summary and prediction samples will be displayed.

