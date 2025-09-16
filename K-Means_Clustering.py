import numpy as np

np.random.seed(42)

# Generate 2D data points around two centers
cluster1 = np.random.randn(50, 2) + np.array([2, 2])
cluster2 = np.random.randn(50, 2) + np.array([7, 7])

data = np.vstack((cluster1, cluster2))

print("Sample Data Points:\n", data[:5]) 


def initialize_centroids(data, k):
    indices = np.random.choice(data.shape[0], size=k, replace=False)
    return data[indices]

# Initialize 2 centroids for k = 2
k = 2
centroids = initialize_centroids(data, k)

print("Initial Centroids:\n", centroids)


def assign_clusters(data, centroids):
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

cluster_assignments = assign_clusters(data, centroids)
print("Cluster Assignments for first 5 points:\n", cluster_assignments[:5])


def update_centroids(data, cluster_assignments, k):
    new_centroids = np.zeros((k, data.shape[1]))
    for i in range(k):
        points = data[cluster_assignments == i]
        new_centroids[i] = points.mean(axis=0)
    return new_centroids

centroids = update_centroids(data, cluster_assignments, k)
print("Updated Centroids:\n", centroids)


def k_means(data, k, max_iters=100):
    centroids = initialize_centroids(data, k)
    for iteration in range(max_iters):
        cluster_assignments = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, cluster_assignments, k)

        # Check if centroids have changed
        if np.allclose(centroids, new_centroids):
            print(f"Converged after {iteration} iterations")
            break

        centroids = new_centroids

    return centroids, cluster_assignments

# Run K-Means
final_centroids, final_assignments = k_means(data, k)

print("Final Centroids:\n", final_centroids)


for i in range(k):
    count = np.sum(final_assignments == i)
    print(f"Cluster {i} has {count} points.")


