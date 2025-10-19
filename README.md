# 🏠 Bangalore House Price Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Framework-Django-darkgreen.svg)
![Machine Learning](https://img.shields.io/badge/Model-Linear%20Regression-orange.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 📘 Overview

**Bangalore House Price Prediction** is a full-stack **Machine Learning + Django web application** designed to predict house prices across different locations in **Bangalore**.  
It combines a trained regression model with an interactive web interface where users can input property details and instantly receive an estimated price.

This project demonstrates **end-to-end machine learning deployment**, from data preprocessing to model training, retraining, and prediction — all integrated within a web-based environment.

---

## 🚀 Features

- 🧠 **Machine Learning Model (Linear Regression)** trained on housing datasets.
- ⚙️ **Preprocessing Script** to encode and transform user inputs into model-compatible data.
- 🔄 **Retrain Model Button** in the navigation bar — automatically retrains the model using updated data and replaces the old model in the database.
- 💾 **Database Model Storage** using Django’s `BinaryField`.
- 🧩 **Django ORM Integration** for smooth data handling and model retrieval.
- 🧍 **Interactive UI** with forms for entering details like area, location, furnishing type, property type, etc.
- 📈 **Real-Time Prediction Output** displayed directly on the web page.
- 🔒 **CSRF-Protected Retraining Form** for security.
- 📊 **Scalable and Easy to Extend** — can be upgraded with more models (RandomForest, XGBoost, etc.).

---

## 🧮 Tech Stack

| Category | Technologies Used |
|-----------|-------------------|
| **Frontend** | HTML5, CSS3, Bootstrap |
| **Backend** | Django 5.2.7 |
| **Programming Language** | Python 3.12 |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Database** | SQLite / PostgreSQL |
| **Version Control** | Git & GitHub |

---

## 🧠 Model Workflow

1. **Data Collection** – Gather housing dataset (area, location, BHK, amenities, etc.).
2. **Data Preprocessing** – Handle missing data, encode categorical variables, and create new derived features (e.g., `bhk_per_bath`).
3. **Model Training** – Train the Linear Regression model using processed data.
4. **Model Saving** – Serialize (pickle) and store the model binary in the database (`MLModel` table).
5. **Prediction** – Fetch the model, preprocess input data, and predict price.
6. **Retraining** – Admin clicks **Retrain Model**; script fetches updated data, retrains the model, and updates the saved version.

---

## MY KAGGLE
![kaggle](https://www.kaggle.com/sydsxdiq)
