---
# ❤️ Heart Disease Prediction App

An interactive desktop application built with **Python**, **Tkinter**, and **Scikit-learn** that helps predict a person’s risk of heart disease based on lifestyle and medical indicators. This tool combines a user-friendly interface with a machine learning model to provide fast and informative health insights.

---

## 🧠 What It Does

This application predicts whether a person is at **high or low risk of heart disease** using key health inputs such as:

- Age, Gender
- Cholesterol, Blood Pressure, Heart Rate
- Smoking & Alcohol Intake
- Exercise Patterns
- Family History, Diabetes, Obesity
- Stress Level, Blood Sugar
- Angina and Chest Pain Type

The backend uses a **Random Forest Classifier** trained on a real dataset and enhanced with preprocessing techniques like **Label Encoding** and **Feature Scaling**.

---

## 📸 GUI Preview
![alt text](<Screenshot .jpg>)
---

## 🧰 Technologies Used

- 🐍 Python 3
- 💻 Tkinter for GUI
- 📊 Scikit-learn (Random Forest, LabelEncoder, StandardScaler)
- 📦 Joblib (for saving/loading the model and encoders)
- 📈 Pandas, NumPy

---

## 🗂️ Project Structure

```

Heart-Disease-Prediction/
│
├── model\_training/
│   ├── train\_model.ipynb
│   ├── scaler.pkl
│   ├── heart\_disease\_model.pkl
│   ├── le\_gender.pkl
│   ├── le\_smoking.pkl
│   └── ... (label encoders for all categorical fields)
│
├── gui\_app/
│   ├── app.py
│   ├── icon.ico
│   └── screenshot.png
│
└── README.md

````

---

## 🚀 How to Run the App

1. **Clone or Download** this repository to your local machine.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the app directory:

   ```bash
   cd gui_app
   ```
4. Launch the GUI:

   ```bash
   python heart_gui.py
   ```

---

## 🔍 How It Works

* **Input**: User enters health-related parameters (e.g., age, cholesterol level) via a simple GUI form.
* **Output**: The trained model processes the input and displays one of the following results:

  * ✅ **Low Risk of Heart Disease**
  * ⚠️ **High Risk of Heart Disease**

---

## 📁 Important Notes

* Ensure all `.pkl` files — the trained model, scaler, and label encoders — are **in the same folder** as `heart_gui.py`.
* Inputs are automatically **preprocessed** to match the model's format.
* ⚠️ **Disclaimer**: This is a machine learning demonstration. It is **not intended for real-world diagnosis** or a substitute for medical advice.

---

## 🤝 Contributions Welcome

Want to make it better? You’re encouraged to fork the repo and submit a pull request. Ideas like:

* Adding charts or visual summaries
* Exporting predictions to PDF
* Supporting multiple languages

...are all welcome!

---

## 👩‍💻 Author

**Wajiha Batool**
Passionate about combining machine learning with meaningful solutions in healthcare and beyond.

---
