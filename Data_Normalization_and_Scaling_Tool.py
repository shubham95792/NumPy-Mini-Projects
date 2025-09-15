import numpy as np 

data = np.array([50, 60, 70, 80, 90])
print("Original Data:", data)

def min_max_normalize(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized

normalized_data = min_max_normalize(data)
print("Min-Max Normalized Data:\n", normalized_data)


def z_score_standardize(arr):
    mean = np.mean(arr)
    std = np.std(arr)
    standardized = (arr - mean) / std
    return standardized

standardized_data = z_score_standardize(data)
print("Z-score Standardized Data:\n", standardized_data)


print("Original Data:\n", data)
print("Min-Max Normalized Data:\n", normalized_data)
print("Z-score Standardized Data:\n", standardized_data)



# Example 2D dataset: rows are samples, columns are features
data_2d = np.array([
    [50, 500],
    [60, 600],
    [70, 700],
    [80, 800],
    [90, 900]
])

def min_max_normalize_2d(arr):
    min_val = np.min(arr, axis=0)
    max_val = np.max(arr, axis=0)
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized

def z_score_standardize_2d(arr):
    mean = np.mean(arr, axis=0)
    std = np.std(arr, axis=0)
    standardized = (arr - mean) / std
    return standardized

normalized_2d = min_max_normalize_2d(data_2d)
standardized_2d = z_score_standardize_2d(data_2d)

print("Original 2D Data:\n", data_2d)
print("\nMin-Max Normalized 2D Data:\n", normalized_2d)
print("\nZ-score Standardized 2D Data:\n", standardized_2d)


def summarize_normalization(arr):
    print("Original Data:\n", arr)
    print("\nMin-Max Normalized Data:\n", min_max_normalize(arr))
    print("\nZ-score Standardized Data:\n", z_score_standardize(arr))

# For 1D data
summarize_normalization(data)

# For 2D data
print("\nFor 2D Data:")
print("Original 2D Data:\n", data_2d)
print("\nMin-Max Normalized 2D Data:\n", normalized_2d)
print("\nZ-score Standardized 2D Data:\n", standardized_2d)


