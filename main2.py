import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv("cricket_betting_dataset.csv")

df_encoded = pd.get_dummies(df, columns=['Team A', 'Team B'])

X = df_encoded.drop(columns=['Match Date', 'Outcome'])
y = (df['Outcome'] == df['Team A']).astype(int)  # 1 if Team A wins, 0 if Team B wins


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=['Team B Wins', 'Team A Wins'])

# Print the model's performance metrics
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", report)
