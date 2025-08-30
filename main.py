import pandas as pd


train = pd.read_csv("data/playground-series-s3e1/train.csv")
test = pd.read_csv("data/playground-series-s3e1/test.csv")
sample_sub = pd.read_csv("data/playground-series-s3e1/sample_submission.csv")

print("Train shape:", train.shape)
print("Test shape:", test.shape)
print("Sample submission shape:", sample_sub.shape)

print(train.isna().sum())

print("The first few features of the train csv file")
print(train.head())

print("The first few features of the test csv file")
print(test.head())
import matplotlib.pyplot as plt

# Step 2A: Target stats
print(train["MedHouseVal"].describe())

# Step 2B: Target distribution
plt.hist(train["MedHouseVal"], bins=50, edgecolor='k')
plt.xlabel("Median House Value")
plt.ylabel("Frequency")
plt.title("Distribution of Target (MedHouseVal)")
plt.show()

# Step 2C: Feature summaries
print(train.drop(columns=["MedHouseVal"]).describe())
