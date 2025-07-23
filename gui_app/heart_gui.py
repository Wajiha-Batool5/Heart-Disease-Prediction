import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
import joblib

# --- Background Image ---
root = tk.Tk()
root.title("Heart Disease Prediction")
root.state('zoomed')  # Maximize window
root.resizable(True, True)

# Create canvas that fills the window
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def resize_bg(event):
    # Resize background image to window size
    new_width = event.width
    new_height = event.height
    bg_image = Image.open(r"C:\Users\Thinkpad T480\OneDrive\Documents\GitHub\Heart-Disease-Prediction\gui_app\background.png")
    bg_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.bg_photo = bg_photo  # Prevent garbage collection
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

canvas.bind("<Configure>", resize_bg)

# --- Center Frame on Right Side ---
main_frame = ttk.Frame(canvas, padding=24, style="Card.TFrame")
main_frame.place(relx=0.75, rely=0.5, anchor="center", width=520, height=750)

style = ttk.Style()
style.theme_use("clam")
style.configure("Card.TFrame", background="#223A5E", relief="raised")  # Dark blue frame
style.configure("TLabel", background="#223A5E", foreground="#ffffff", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 20, "bold"), foreground="white", background="#8b0000")
style.map("TButton", background=[("active", "#b56969")])

title_label = ttk.Label(main_frame, text="Heart Disease Prediction", font=("Segoe UI", 24, "bold"), foreground="#ffffff", background="#8b0000")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 12))

labels = [
    "Age", "Gender", "Cholesterol", "Blood Pressure", "Heart Rate", "Smoking", "Alcohol Intake",
    "Exercise Hours", "Family History", "Diabetes", "Obesity", "Stress Level", "Blood Sugar",
    "Exercise Induced Angina", "Chest Pain Type"
]

entries = {}

dropdown_options = {
    "Gender": ["Male", "Female"],
    "Smoking": ["Never", "Former", "Current"],
    "Alcohol Intake": ["None", "Moderate", "Heavy"],
    "Family History": ["No", "Yes"],
    "Diabetes": ["No", "Yes"],
    "Obesity": ["No", "Yes"],
    "Exercise Induced Angina": ["No", "Yes"],
    "Chest Pain Type": ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
}

# Smaller entry width and center alignment
for i, label in enumerate(labels, start=1):
    ttk.Label(main_frame, text=label + ":").grid(row=i, column=0, sticky=tk.E, padx=5, pady=5)
    if label in dropdown_options:
        var = tk.StringVar()
        entries[label] = ttk.Combobox(main_frame, textvariable=var, values=dropdown_options[label], state="readonly", font=("Segoe UI", 12), width=16)
        entries[label].current(0)
    else:
        entries[label] = ttk.Entry(main_frame, font=("Segoe UI", 12), width=18)
    entries[label].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

main_frame.columnconfigure(1, weight=1)

# List of categorical columns for encoding
categorical_cols = [
    "Gender", "Smoking", "Alcohol Intake", "Family History",
    "Diabetes", "Obesity", "Exercise Induced Angina", "Chest Pain Type"
]

def preprocess_input(data_dict):
    df = pd.DataFrame([data_dict])
    for col in categorical_cols:
        le_path = f"model_training/le_{col.lower().replace(' ', '_')}.pkl"  # <-- update path
        le = joblib.load(le_path)
        df[col] = df[col].str.strip().str.lower()
        if isinstance(le.classes_[0], str):
            mapping = {cls.lower(): le.transform([cls])[0] for cls in le.classes_}
            df[col] = df[col].map(mapping)
        else:
            raise ValueError(f"LabelEncoder for {col} is not string-based.")
    scaler = joblib.load("model_training/scaler.pkl")  # <-- update path
    df_scaled = pd.DataFrame(scaler.transform(df), columns=df.columns)
    return df_scaled

def predict():
    try:
        input_data = {}
        for label in labels:
            value = entries[label].get()
            if label in dropdown_options:
                input_data[label] = value
            else:
                input_data[label] = float(value)
        processed = preprocess_input(input_data)
        model = joblib.load("model_training/heart_disease_model.pkl")  # <-- update path
        prediction = model.predict(processed)[0]
        result_text = "⚠️ High Risk of Heart Disease" if prediction == 1 else "✅ Low Risk of Heart Disease"
        messagebox.showinfo("Prediction Result", result_text)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

predict_btn = ttk.Button(main_frame, text="Predict", command=predict)
predict_btn.grid(row=len(labels)+1, columnspan=2, pady=14, sticky=tk.EW)

root.mainloop()
