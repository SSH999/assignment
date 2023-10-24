import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv('Hyderabad_House_Data.csv')

# Extract numerical data from 'Area' column and convert to integers, filling missing values with 0
df['Area'] = df['Area'].str.extract('(\d+)').astype(float).fillna(0).astype(int)

# Clean the 'Price' column by removing any non-numeric characters and converting to integers
df['Price'] = df['Price'].str.replace('[^\d]', '', regex=True).astype(int)


X = df[['Bedrooms', 'Bathrooms', 'Furnishing', 'Tennants', 'Area']]
y = df['Price']

X_encoded = pd.get_dummies(X, columns=['Bedrooms', 'Bathrooms', 'Furnishing', 'Tennants'])

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")
# Predict property prices
predicted_prices = model.predict(X_encoded)

# Calculate prediction errors
prediction_errors = y - predicted_prices

# Add prediction errors as a new column in your dataset
df['Prediction Error'] = prediction_errors

# Identify properties with significant negative prediction errors (indicating potential undervaluation)
undervalued_properties = df[df['Prediction Error'] < 0]

# Display undervalued properties
print(undervalued_properties)

