import numpy as np 

np.random.seed(42)

X = np.random.randint(20, 60, 10)
Y = np.random.normal(50000, 10000, 10)
print(X)
print(Y)

mean_X = np.mean(X)
mean_Y = np.mean(Y)

print("Mean of X (Ages):", mean_X)
print("Mean of Y (Income):", mean_Y)


median_X = np.median(X)
median_Y = np.median(Y)

print("Median of X (Ages):", median_X)
print("Median of Y (Income):", median_Y)


variance_X = np.var(X)
std_dev_X = np.std(X)

variance_Y = np.var(Y)
std_dev_Y = np.std(Y)

print("Variance of X (Ages):", variance_X)
print("Standard Deviation of X (Ages):", std_dev_X)

print("Variance of Y (Income):", variance_Y)
print("Standard Deviation of Y (Income):", std_dev_Y)


correlation = np.corrcoef(X, Y)[0, 1]

print("Correlation between X (Ages) and Y (Income):", correlation)


def summarize_data(X, Y):
    print("Summary of Dataset:\n")

    print("Mean of X:", np.mean(X))
    print("Mean of Y:", np.mean(Y))
    print()

    print("Median of X:", np.median(X))
    print("Median of Y:", np.median(Y))
    print()

    print("Variance of X:", np.var(X))
    print("Standard Deviation of X:", np.std(X))
    print()

    print("Variance of Y:", np.var(Y))
    print("Standard Deviation of Y:", np.std(Y))
    print()

    correlation = np.corrcoef(X, Y)[0, 1]
    print("Correlation between X and Y:", correlation)


summarize_data(X, Y)

