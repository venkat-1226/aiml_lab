
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Test Case 1: Two clusters
X1 = [[1,1], [1,2], [2,1], [6,6], [6,7], [7,6]]

model1 = KMeans(n_clusters=2, random_state=0, n_init=10)
model1.fit(X1)

print("Test Case 1: Two Clusters")
print("Cluster labels:", model1.labels_)
print("Centroids:", model1.cluster_centers_)

plt.scatter([x[0] for x in X1], [x[1] for x in X1],
            c=model1.labels_)
plt.title("Two Clusters")
plt.show()


# Test Case 2: Three clusters
X2 = [[1,1], [1,2], [2,1],
      [5,5], [5,6], [6,5],
      [9,9], [9,10], [10,9]]

model2 = KMeans(n_clusters=3, random_state=0, n_init=10)
model2.fit(X2)

print("\nTest Case 2: Three Clusters")
print("Cluster labels:", model2.labels_)
print("Centroids:", model2.cluster_centers_)

plt.scatter([x[0] for x in X2], [x[1] for x in X2],
            c=model2.labels_)
plt.title("Three Clusters")
plt.show()
