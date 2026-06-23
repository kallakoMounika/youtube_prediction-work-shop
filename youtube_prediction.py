import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load Dataset
df = pd.read_csv("youtube_earnings.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Features (Inputs)
X = df[
    [
        "Subscribers",
        "Total_Views",
        "Videos_Uploaded",
        "Avg_Views_Per_Video"
    ]
]

# Target (Output)
y = df["Monthly_Earnings"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# Take User Inputs
print("\nEnter Channel Details")

subscribers = int(input("Subscribers: "))
total_views = int(input("Total Views: "))
videos_uploaded = int(input("Videos Uploaded: "))
avg_views = int(input("Average Views Per Video: "))

# Predict
prediction = model.predict(
    [[
        subscribers,
        total_views,
        videos_uploaded,
        avg_views
    ]]
)

print("\n================================")
print(f"Predicted Monthly Earnings: ${prediction[0]:,.2f}")
print("================================")