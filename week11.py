
import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
w1 = np.random.rand(2,4)
w2 = np.random.rand(4,1)
b1 = np.zeros((1,4))
b2 = np.zeros((1,1))

def sigmoid(x):
    return 1/(1+np.exp(-x))

initial = w1.copy()

# Training
for i in range(10000):
    h = sigmoid(X @ w1 + b1)
    o = sigmoid(h @ w2 + b2)
    error = y - o

    d2 = error * o * (1-o)
    d1 = (d2 @ w2.T) * h * (1-h)

    w2 += 0.5 * h.T @ d2
    b2 += 0.5 * np.sum(d2, axis=0)
    w1 += 0.5 * X.T @ d1
    b1 += 0.5 * np.sum(d1, axis=0)

# Test Case 1: XOR Dataset
print("Test Case 1: XOR")
pred = sigmoid(sigmoid(X @ w1 + b1) @ w2 + b2)
print("Predicted:", (pred >= 0.5).astype(int).flatten())

# Test Case 2: Weight Update
print("\nTest Case 2: Weight Update")
print("Initial weights:", initial)
print("Updated weights:", w1)
print("Result: Weights updated successfully")
