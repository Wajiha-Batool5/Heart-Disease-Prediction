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

1. **Clone or Download** this repository.
2. Make sure you have all dependencies installed:
   ```bash
   pip install -r requirements.txt
````
3. Navigate to the `gui_app` folder:
   ```bash
   cd gui_app
   ```
4. Run the GUI app:
   ```bash
   python heart_gui.py
   ```

---

## 🔐 Model Inputs & Output

* Input: User-entered health parameters via GUI form
* Output: Message box with prediction

  * ✅ Low Risk of Heart Disease
  * ⚠️ High Risk of Heart Disease

---

## 📁 Important Notes

* All `.pkl` files (model, scaler, and encoders) **must be in the same directory** as your `app.py`.
* The inputs from the GUI are **preprocessed** to match the model’s expected input format.
* This is not a substitute for professional medical advice — it’s a demonstration of applied machine learning.

---

## 🤝 Contributions

Pull requests are welcome! If you’d like to improve the app or add more features (e.g., data visualization, PDF reports, or multi-language support), feel free to fork this repo and open a PR.

---

## 👤 Author

**Wajiha Batool**
Created with passion for both machine learning and impactful health technology.

