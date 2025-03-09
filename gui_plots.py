import os
import tkinter as tk
import ttkbootstrap as ttk  # ✅ Use ttkbootstrap for a modern look
from ttkbootstrap import Style
from tkinter import filedialog, messagebox
import pandas as pd
import pdfkit
import baseline_html
import importlib

# ✅ Reload `baseline_html.py` to ensure the latest functions are loaded
importlib.reload(baseline_html)

# ✅ PDF Configuration
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
options = {'enable-local-file-access': '', 'page-size': 'A4', 'encoding': "UTF-8"}

# ✅ Fetch `graphs` Dictionary Automatically
graphs = baseline_html.graphs if hasattr(baseline_html, "graphs") else {}

# ✅ Function to Browse Directories
def browse_csv():
    folder = filedialog.askdirectory()
    csv_entry.delete(0, tk.END)
    csv_entry.insert(0, folder)

def browse_output():
    folder = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder)

# ✅ Start Processing
def start_conversion():
    """Processes CSV files, generates HTML, and optionally converts to PDF."""
    csv_path = csv_entry.get()
    country = country_entry.get().strip()
    output_path = output_entry.get()
    generate_pdf = pdf_var.get()

    if not csv_path or not os.path.exists(csv_path):
        messagebox.showerror("Error", "Invalid CSV Directory!")
        return
    if not country:
        messagebox.showerror("Error", "Country Code is required!")
        return
    if not output_path or not os.path.exists(output_path):
        messagebox.showerror("Error", "Invalid Output Directory!")
        return

    working_directory = os.path.join(output_path, country)
    os.makedirs(working_directory, exist_ok=True)

    selected_csvs = list(graphs.keys())

    log_text.insert(tk.END, f"📂 Processing {len(selected_csvs)} CSV files for {country}...\n")
    log_text.update_idletasks()

    progress_bar["value"] = 0
    progress_bar["maximum"] = len(selected_csvs)

    process_data(csv_path, country, working_directory, generate_pdf, selected_csvs)

# ✅ Processing Function
def process_data(csv_path, country, working_directory, generate_pdf, selected_csvs):
    """Reads CSV, generates HTML, and converts to PDF."""
    dataframes = {}
    completed_files = 0

    os.makedirs(working_directory, exist_ok=True)

    # ✅ Read CSV Files
    for csv in selected_csvs:
        file_path = os.path.join(csv_path, csv)
        if os.path.exists(file_path):
            try:
                dataframes[csv] = pd.read_csv(file_path, encoding="ISO-8859-1")
                log_text.insert(tk.END, f"✅ Loaded {csv}\n")
            except Exception as e:
                log_text.insert(tk.END, f"❌ Failed to read {csv}: {e}\n")
        else:
            log_text.insert(tk.END, f"⚠️ Missing: {csv}\n")

        completed_files += 1
        progress_bar["value"] = completed_files
        log_text.update_idletasks()

    image_directory = os.path.join(working_directory, "images")
    
    os.makedirs(image_directory, exist_ok=True)
    # ✅ Generate HTML
    html_file = os.path.join(working_directory, f"{country}.html")
    with open(html_file, 'w', encoding="utf-8") as outfile:
        outfile.write(f"<html><head><meta charset='UTF-8'><title>{country}</title></head>\n")
        outfile.write("<link rel='stylesheet' type='text/css' href='dfstyle.css'/>\n")
        outfile.write(f"<body><h3>MS Baselines Country: {country}</h3>\n")

        for csv in selected_csvs:
            if csv in dataframes:
                try:
                    graphs[csv](dataframes[csv], country, outfile, image_directory)
                except Exception as e:
                    log_text.insert(tk.END, f"❌ Error processing {csv}: {e}\n")

        outfile.write("</body></html>\n")

    # ✅ Generate CSS (Only Once)
    css_path = os.path.join(working_directory, "dfstyle.css")
    if not os.path.exists(css_path):
        css_content = """ 
        .dataframe { font-size: 11pt; font-family: Arial; border-collapse: collapse; border: 1px solid silver; }
        .dataframe td, th { padding: 5px; text-align: left; }
        .dataframe tr:nth-child(even) { background: #E0E0E0; }
        .dataframe tr:hover { background: silver; cursor: pointer; }
        * { font-size: 100%; font-family: Arial; }
        """
        with open(css_path, "w", encoding="utf-8") as css_file:
            css_file.write(css_content)
        print(f"✅ CSS file created: {css_path}")

    # ✅ Generate PDF (if selected)
    if generate_pdf:
        pdf_file = os.path.join(working_directory, f"{country}.pdf")
        try:
            pdfkit.from_file(html_file, pdf_file, configuration=config, options=options)
            log_text.insert(tk.END, f"📄 PDF Created: {pdf_file}\n")
        except Exception as e:
            log_text.insert(tk.END, f"❌ Error creating PDF: {e}\n")

    log_text.insert(tk.END, f"✅ Process Completed for {country}\n")
    log_text.update_idletasks()
    progress_bar["value"] = len(selected_csvs)

# ✅ Close Application
def exit_application():
    root.quit()
    root.destroy()

# ✅ Tkinter GUI
def create_gui():
    global root, csv_entry, country_entry, output_entry, log_text, progress_bar, pdf_var, photo

    root = ttk.Window(themename="pulse")  # ✅ Modern UI theme
    style = Style(theme="pulse")

    root.title("CSV to PDF Converter")
    root.geometry("600x900")

    ttk.Label(root, text="CSV Directory").pack(pady=2)
    ttk.Label(root, text="Select the csv Directory.").pack()
    
    csv_entry = ttk.Entry(root, width=50)
    csv_entry.pack(pady=2)
    ttk.Button(root, text="Browse", command=browse_csv).pack(pady=2)

    ttk.Label(root, text="Country Code").pack(pady=2)
    ttk.Label(root, text="Enter the country code (e.g., 'DE' for Germany, 'FR' for France).").pack()
    country_entry = ttk.Entry(root, width=5)
    country_entry.pack(pady=2)

    ttk.Label(root, text="Output Directory").pack(pady=2)
    ttk.Label(root, text="Choose a folder where the generated PDF will be saved.").pack()
    output_entry = ttk.Entry(root, width=50)
    output_entry.pack(pady=2)
    ttk.Button(root, text="Browse", command=browse_output).pack(pady=2)

    pdf_var = ttk.IntVar()
    ttk.Checkbutton(root, text="Generate PDF", variable=pdf_var).pack(pady=5)

    ttk.Button(root, text="Start Conversion", command=start_conversion, bootstyle="success").pack(pady=10)

    ttk.Label(root, text="Process Log").pack(pady=2)
    log_text = ttk.Text(root, height=10, width=70)
    log_text.pack(pady=5)

    progress_bar = ttk.Progressbar(root, length=400, mode='determinate', bootstyle="info")
    progress_bar.pack(pady=5)

    ttk.Button(root, text="Exit", command=exit_application, bootstyle="danger").pack(pady=2)

    root.mainloop()

# ✅ Run GUI
if __name__ == "__main__":
    create_gui()
