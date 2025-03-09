# 📊 CSV to HTML/PDF Converter

## 📌 Project Overview
This project provides a **GUI-based tool** for converting CSV data into **HTML reports with graphs** and optionally exporting them to **PDF**. It is designed for handling **WISE water data** but can be adapted for other datasets.

✅ **CSV Processing** to generate structured reports

✅ **Data Visualization** with `matplotlib`

✅ **Export to HTML & PDF**

✅ **User-Friendly GUI** built with `ttkbootstrap`


---

## 🛠️ Installation
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/ThGoulis/CSV-HTML-PDF-Converter.git
cd CSV-HTML-PDF-Converter
```

### 2️⃣ **Set Up a Virtual Environment** *(Recommended)*
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🚀 Usage
### **1️⃣ Run the GUI (Recommended)**
```sh
python gui_plots.py
```
- Select the **CSV folder** containing the dataset.
- Enter the **country code** (e.g., `DE` for Germany, `FR` for France).
- Choose an **output folder**.
- Optionally enable **PDF export**.
- Click **"Start Conversion"**.

### **2️⃣ Run in Terminal (CLI Mode)**
```sh
python baseline_html.py input_folder/ output_folder/
```
This processes the CSVs and generates HTML reports.

---

## 📂 Project Structure
```
CSV-HTML-PDF-Converter/
│── gui_plots.py         # GUI Interface for CSV to PDF
│── baseline_html.py     # HTML generation from CSV
│── baseline_plots.py    # Data visualization functions
│── requirements.txt     # Required dependencies
│── README.md            # Project Documentation
```

---

## 📌 Dependencies
- Python 3.x
- `pandas`
- `matplotlib`
- `ttkbootstrap`
- `pdfkit`
- `tkinter`

Install all dependencies via:
```sh
pip install -r requirements.txt
```

---

## 🔥 Contributing
Pull requests are welcome! Feel free to submit issues and suggestions.

---

## 📝 License
MIT License. See `LICENSE` file for details.

