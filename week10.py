
from sklearn.neighbors import KNeighborsClassifier

def knn(X, y, test, k=3):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)
    return model.predict(test)


# Test Case 1: Numeric Data
X1 = [[1,1], [2,2], [3,3], [10,10], [11,11], [12,12]]
y1 = [0,0,0,1,1,1]

print("Test Case 1: Numeric Data")
print("Input:", [2,2])
print("Output:", knn(X1, y1, [[2,2]]))


# Test Case 2: Clearly Separated Classes
X2 = [[1,1], [1,2], [2,1], [2,2],
      [10,10], [10,11], [11,10], [11,11]]
y2 = [0,0,0,0,1,1,1,1]

print("\nTest Case 2: Separated Classes")
print("Input:", [[1.5,1.5], [10.5,10.5]])
print("Output:", knn(X2, y2, [[1.5,1.5], [10.5,10.5]]))
