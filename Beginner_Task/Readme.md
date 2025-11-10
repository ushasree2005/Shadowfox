## 🏠 Boston House Price Prediction

This project uses **Linear Regression** to predict house prices in Boston based on various socioeconomic and housing features.
The dataset used is **`HousingData.csv`**, which contains multiple numerical attributes that describe the characteristics of Boston suburbs.

---

### 📂 Project Structure

```
📁 Boston_House_Price_Prediction
│
├── HousingData.csv              # Dataset
├── Boston_House_Price_Prediction.ipynb   # Jupyter Notebook
└── README.md                    # Project Documentation
```

---

### 🧩 Steps Covered in the Notebook

1. **Import Libraries** – Load all required Python libraries
2. **Load Dataset** – Read `HousingData.csv` using pandas
3. **Handle Missing Values** – Replace missing entries with column means
4. **Exploratory Data Analysis (EDA)** – View summary statistics and correlation heatmap
5. **Feature-Target Split** – Define `X` (features) and `y` (target = MEDV)
6. **Train-Test Split** – Divide data into training (80%) and testing (20%) sets
7. **Train Linear Regression Model** – Fit model using scikit-learn
8. **Model Evaluation** – Calculate MAE, MSE, RMSE, and R² score
9. **Visualization** – Plot Actual vs Predicted Prices
10. **Feature Importance** – Display regression coefficients
11. **Summary** – Conclude model performance

---

### ⚙️ Requirements

Install the following Python libraries before running the notebook:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

### 🚀 How to Run

1. Clone or download this repository
2. Open the Jupyter Notebook file:

   ```bash
   jupyter notebook Boston_House_Price_Prediction.ipynb
   ```
3. Run each cell in order (Parts 1 to 11)
4. The notebook will output:

   * Cleaned dataset info
   * Correlation heatmap
   * Model performance metrics
   * Actual vs Predicted scatter plot
   * Feature importance table

---

### 📊 Results

| Metric                         | Value (Example) |
| :----------------------------- | :-------------- |
| Mean Absolute Error (MAE)      | ~3.4            |
| Mean Squared Error (MSE)       | ~24.5           |
| Root Mean Squared Error (RMSE) | ~4.9            |
| R² Score                       | ~0.65           |

> 💡 *These results may vary slightly depending on random state and dataset cleaning.*

---

### 💡 Insights

* **RM (average number of rooms per dwelling)** has a strong positive correlation with price.
* **LSTAT (percentage of lower-status population)** has a strong negative correlation.
* Linear Regression gives a solid baseline for understanding housing trends.

---

### 🧠 Future Improvements

* Try **Ridge** or **Lasso Regression** for regularization
* Apply **Feature Scaling** for better coefficient comparison
* Use **Polynomial Regression** or **Tree-based Models** for non-linear patterns

---


