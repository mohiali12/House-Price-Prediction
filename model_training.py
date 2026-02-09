import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from joblib import dump

# 1) Load dataset
df = pd.read_csv("train.csv")

# 2) Features + target
features = ["LotArea","OverallQual","YearBuilt","TotalBsmtSF","GrLivArea","BedroomAbvGr","FullBath"]
target = "SalePrice"

X = df[features]
y = df[target]

# 3) Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4) Build model
model = LinearRegression()
model.fit(X_train, y_train)

# 5) Save model
dump(model, "house_price_model.pkl")
print("Model trained and saved!")
