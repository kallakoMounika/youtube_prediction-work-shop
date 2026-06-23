# youtube_prediction-work-shop
youtube_prediction workshop
# 📊 YouTube Earnings Predictor using Linear Regression

A machine learning project that predicts **Monthly Earnings** of a YouTube channel based on key channel statistics using **Linear Regression**.

> 🏫 Built during the **Machine Learning Workshop** conducted by **Revanth Software Solutions Pvt. Ltd.**

---

## 🏢 About the Workshop

| Detail | Info |
|---|---|
| 🏷️ **Workshop Name** | Machine Learning Workshop |
| 🏢 **Organized By** | Revanth Software Solutions Pvt. Ltd. |
| 📚 **Topics Covered** | Python, Data Science, ML Algorithms, Real-world Projects |
| 🛠️ **Project Built** | YouTube Earnings Predictor using Linear Regression |

This project was developed as part of a hands-on Machine Learning workshop, where participants learned core ML concepts and applied them to real-world datasets.

---

## 🚀 Project Overview

This project uses a dataset of YouTube channel metrics to train a Linear Regression model that can predict how much a channel earns per month. It is built using **Python** and **Google Colab**.

---

## 📁 Dataset — `youtube_earnings.csv`

The dataset contains the following columns:

| Feature | Description |
|---|---|
| `Subscribers` | Total number of subscribers |
| `Total_Views` | Total views on the channel |
| `Videos_Uploaded` | Number of videos uploaded |
| `Avg_Views_Per_Video` | Average views per video |
| `Monthly_Earnings` | 💰 Target variable (output) |

---

## 🧠 Model Used

- **Algorithm**: Linear Regression
- **Library**: `scikit-learn`
- **Train/Test Split**: 80% training, 20% testing
- **Random State**: 42

---

## 🛠️ Technologies Used

- Python 3
- Google Colab
- Pandas
- Scikit-learn (sklearn)

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-earnings-predictor.git
   ```

2. Upload `youtube_earnings.csv` to your Colab or local environment

3. Open `Untitled2.ipynb` in Google Colab or Jupyter Notebook

4. Run all cells — it will:
   - Load and display the dataset
   - Train the Linear Regression model
   - Ask you to enter your channel details
   - Predict your **Monthly Earnings** 💰

---

## 📊 Sample Output

```
Dataset Loaded Successfully

   Subscribers  Total_Views  Videos_Uploaded  Avg_Views_Per_Video  Monthly_Earnings
0       100000      1000000               50                20000              1000
1       500000      5000000              150                33333              5000

Model Trained Successfully

Enter Channel Details:
Subscribers: 5000
Total Views: 2500
Videos Uploaded: 1000
Average Views Per Video: 500

================================
Predicted Monthly Earnings: $50.00
================================
```

---

## 📌 Key Learnings

- Data preprocessing using Pandas
- Feature selection and target variable definition
- Splitting data using `train_test_split`
- Training and predicting with `LinearRegression`
- Taking user input for real-time prediction

---

## 🙋 Author

**Your Name**
- LinkedIn: [your-linkedin-profile]
- GitHub: [your-github-profile]

---

## 🤝 Acknowledgement

Special thanks to **Revanth Software Solutions Pvt. Ltd.** for organizing this amazing Machine Learning Workshop and providing hands-on experience with real-world ML projects. 🙏

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
