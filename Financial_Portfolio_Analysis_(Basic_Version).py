import numpy as np 

np.random.seed(42)

num_days = 100 
num_stocks = 3

mean_return = 0.001
std_dev = 0.02

returns = np.random.normal(mean_return, std_dev, size=(num_days, num_stocks))

print("Sample Returns (first 5 days):\n", returns[:5])


mean_returns = np.mean(returns, axis=0)

print("Mean Daily Returns for each stock:\n", mean_returns)


variance = np.var(returns, axis=0)
std_dev = np.std(returns, axis=0)

print("Variance of Returns:\n", variance)
print("Standard Deviation of Returns:\n", std_dev)


correlation_matrix = np.corrcoef(returns, rowvar=False)

print("Correlation Matrix between stocks:\n", correlation_matrix)


# Define portfolio weights for each stock 
weights = np.array([0.4, 0.4, 0.2])

# Portfolio mean return
portfolio_return = np.sum(mean_returns * weights)

# Portfolio variance
portfolio_variance = np.dot(weights, np.dot(np.cov(returns, rowvar=False), weights))

# Portfolio standard deviation
portfolio_std_dev = np.sqrt(portfolio_variance)

print("Portfolio Expected Return:", portfolio_return)
print("Portfolio Risk (Standard Deviation):", portfolio_std_dev)



print("\n--- Portfolio Summary ---")
print("Mean Returns:\n", mean_returns)
print("Variances:\n", variance)
print("Standard Deviations:\n", std_dev)
print("Correlation Matrix:\n", correlation_matrix)
print("Portfolio Expected Return:", portfolio_return)
print("Portfolio Risk (Std Dev):", portfolio_std_dev)



