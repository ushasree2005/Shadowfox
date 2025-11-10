# train_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

print("🏠 Boston House Price Prediction Model Trainer\n")

# Load dataset
data = pd.read_csv("HousingData.csv")
data.fillna(data.mean(), inplace=True)

# Split features and target
X = data.drop("MEDV", axis=1)
y = data["MEDV"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"✅ Model trained successfully!")
print(f"📊 MAE: {mae:.2f} | RMSE: {rmse:.2f} | R²: {r2:.2f}")

# Save model
joblib.dump(model, "model.pkl")
print("\n💾 model.pkl created successfully!")
print("Now run:  streamlit run app.py")
