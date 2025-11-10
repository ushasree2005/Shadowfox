# 🛍️ Store Sales and Profit Analysis using Python

## 📖 Overview

This project explores and analyzes retail store sales data using Python.
The goal is to uncover key business insights — such as top-performing categories, profit trends, and customer behavior — to help a retail business make smarter, data-driven decisions.

We use a real-world sample dataset: **Sample - Superstore.csv**.

---

## 🎯 Objective

The purpose of this analysis is to:

* Understand overall **sales** and **profit performance**
* Identify **best-selling categories and products**
* Detect **unprofitable segments or discounts**
* Visualize **trends over time** (monthly sales & profits)
* Support **strategic business decisions** through data insights

---

## 🧰 Tools & Libraries

You’ll need the following Python libraries:

```bash
pip install pandas matplotlib openpyxl numpy
```

**Libraries used:**

* **Pandas** → data cleaning & analysis
* **NumPy** → calculations & transformations
* **Matplotlib** → data visualization
* **OpenPyXL** → export results to Excel

---

## 📂 Dataset

File used: **Sample - Superstore.csv**

| Column Name   | Description                                    |
| ------------- | ---------------------------------------------- |
| Order Date    | Date when the order was placed                 |
| Ship Date     | Date when the order was shipped                |
| Category      | Product category (e.g., Furniture, Technology) |
| Sub-Category  | Specific product type                          |
| Sales         | Revenue from the sale                          |
| Profit        | Profit earned on the sale                      |
| Quantity      | Number of units sold                           |
| Region        | Geographic region of the customer              |
| Customer Name | Customer who placed the order                  |

---

## 🧪 Steps Performed

### 1️⃣ Load and Inspect Data

* Read the CSV file into a Pandas DataFrame
* Check for missing values and duplicates
* Ensure date columns are properly formatted

### 2️⃣ Data Cleaning

* Remove duplicate entries
* Handle missing or invalid data
* Convert columns like “Order Date” into datetime format
* Create additional columns:

  * `Order Year`
  * `Order Month`
  * `Profit Margin` (Profit ÷ Sales)

### 3️⃣ Exploratory Data Analysis (EDA)

* Calculate total sales, total profit, and average profit margin
* Group data by:

  * Category
  * Sub-Category
  * Region
  * Month
  * Customer
* Identify top-performing products and customers
* Detect negative-profit (loss) items

### 4️⃣ Data Visualization

Visualized with Matplotlib:

* 📈 Monthly sales trend
* 💰 Monthly profit trend
* 📊 Sales by category
* 🏆 Top 10 products by sales
* ⚖️ Sales vs Profit scatter plot

### 5️⃣ Export Results

All results and summaries are exported to an Excel file:

```
superstore_analysis_summary.xlsx
```

with multiple sheets:

* Summary Statistics
* Missing Values
* Sales by Category
* Top Products
* Top Customers
* Sales by Month

---

## 📊 Key Insights (Example)

Here’s a sample of what you might find:

* **Technology** is the highest revenue category
* **Office Supplies** sells a lot but has a lower profit margin
* Some orders show **negative profits** (too much discounting)
* Sales and profit are moderately correlated (r ≈ 0.48)
* Clear **seasonal sales peaks** during year-end months

---

## 💡 Recommendations

1. Review **discounts and shipping costs** on unprofitable orders
2. Focus marketing on **Technology** and **high-margin subcategories**
3. Optimize **inventory** around peak months (based on trend analysis)
4. Identify **loyal customers** for personalized loyalty programs

---

## 🖥️ How to Run the Project

### Option 1: Using Jupyter Notebook

1. Open Jupyter Notebook or Google Colab
2. Upload your dataset (`Sample - Superstore.csv`)
3. Copy and paste the Python code from the analysis script
4. Run all cells step by step
5. View plots and check exported Excel results

### Option 2: Using a Python Script

1. Save your Python analysis file as `superstore_analysis.py`
2. Place the dataset in the same folder
3. Run from terminal:

   ```bash
   python superstore_analysis.py
   ```
4. Open the generated Excel file and PNG charts for insights

---

## 📈 Example Output Files

After running the analysis, you’ll get:

* 🧾 **superstore_analysis_summary.xlsx** → Full analytical report
* 🖼️ **Charts:**

  * `monthly_sales.png`
  * `monthly_profit.png`
  * `sales_by_category.png`
  * `top10_products.png`
  * `sales_vs_profit.png`

---



