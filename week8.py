
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder

def test(data, name):
    df = pd.DataFrame(data)
    X = df.iloc[:, :-1].copy()
    y = LabelEncoder().fit_transform(df.iloc[:, -1])

    for col in X.columns:
        X[col] = LabelEncoder().fit_transform(X[col].astype(str))

    model = DecisionTreeClassifier(criterion="entropy")
    model.fit(X, y)

    print("\n", name)
    print(export_text(model, feature_names=list(X.columns)))
    print("Tree Depth:", model.get_depth())
    print("No. of Leaves:", model.get_n_leaves())

# Test Case 1: Play Tennis Dataset
play_tennis = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"]
]

test(play_tennis, "Test Case 1: Play Tennis")

# Test Case 2: Clear Class Separation
clear_data = [
    ["A", "Yes"],
    ["B", "Yes"],
    ["C", "No"],
    ["D", "No"]
]

test(clear_data, "Test Case 2: Clear Class Separation")
