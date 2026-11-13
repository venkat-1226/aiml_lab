
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Test Case 1: Linearly Separable Data
X1 = np.array([[1,1],[2,2],[3,3],[7,7],[8,8],[9,9]])
y1 = np.array([0,0,0,1,1,1])

model1 = SVC(kernel='linear')
model1.fit(X1, y1)

pred1 = model1.predict(X1)
print("Test Case 1")
print("Actual:", y1)
print("Predicted:", pred1)
print("Accuracy:", accuracy_score(y1, pred1))

# Test Case 2: Two-Class Data
X2 = np.array([[2,2],[3,3],[8,8],[9,9]])
y2 = np.array([0,0,1,1])

model2 = SVC(kernel='linear')
model2.fit(X2, y2)

test = np.array([[2,2],[8,8]])
pred2 = model2.predict(test)

print("\nTest Case 2")
print("Test points:", test)
print("Predicted labels:", pred2)
print("Result: Success")
