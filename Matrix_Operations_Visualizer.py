import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array ([[9, 8, 7],
               [6, 5, 4],
               [3, 2, 1]])

print("First Matrix is: \n", A)
print("Second Matrix is: \n", B)


def matrix_addition(X, Y):
  return X + Y
Add = matrix_addition(A, B)



def matrix_subtraction(X, Y):
  return X - Y
Sub = matrix_subtraction(A, B)



def matrix_multiplication(X, Y):
  return np.dot(X, Y)
Multi = matrix_multiplication(A, B)



def matrix_transpose(X):
  return X.T
Trans = matrix_transpose(A)



opration = int(input("Enter the Operation Number you want to Perform: \nAdd(1), subtract(2), multiply(3), transpose(4): \n"))


if opration == 1:
    print("Matrix Addition is: \n", Add)

elif opration == 2:
    print("Matrix Subtraction is: \n", Sub)

elif opration == 3:
    print("Matrix Multiplication is: \n", Multi)

elif opration == 4:
    print("Matrix Transpose is: \n", Trans)

else:
    print("Invalid Operation Number")
    