# 📊 Data Visualization Generator
**Data Visualization Generator** is a user-friendly desktop application built with **PyQt5**, **Pandas**, and **Matplotlib**. It allows users—especially those without coding experience—to easily visualize data from CSV or Excel files through an intuitive graphical interface.

With just a few clicks, users can upload data, explore it, and generate plots without writing a single line of code.

---

## ✨ Features

### 📁 Upload Function  
- Open your file manager to load a `.csv` or `.xlsx` file.  
- The data is automatically displayed in a table format upon selection.

### 📊 Plot Type Selection (ComboBox)  
- Choose from five supported plot types:
  - `plot` (line graph)
  - `hist` (histogram)
  - `scatter` (scattered plot)
  - `bar` (bar graph)
  - `pie` (pie chart)
- Each plot type provides clearly divided input fields:
  - **Required**: essential fields for generating the plot  
  - **Optional**: customization or enhancements (e.g., labels, colors)

### 🧾 Data Frame Viewer  
- Displays the loaded DataFrame in a readable table format.
- Helps in quickly referencing column names and values for plotting.

### 📈 Plot Output  
- Displays the generated plot based on your selected type and input.
- Leverages the power of Matplotlib for clean, customizable visualizations.

### ℹ️ Data Info Panel  
- Presents useful metadata and summary stats of your dataset:
  - `df.info()` for structure and types
  - Mean and median for all numeric columns

---

## 💡 Why Use This Tool?
- No coding required — ideal for beginners or quick exploration.
- Simplifies Pandas and Matplotlib usage into a visual experience.
- Perfect for quick reports, data presentations, and educational use.

---

## 🛠️ Tech Stack
- **Python**
- **PyQt5** – GUI framework
- **Pandas** – data processing and analysis
- **Matplotlib** – data visualization

---

## 🚀 Getting Started

```bash
pip install pyqt5 pandas matplotlib
python main.py
