import numpy as np
from sklearn.neighbors import KNeighborsRegressor

if __name__ == "__main__":
    N = int(input("Enter N: "))
    k = int(input("Enter k: "))
    if k > N:
        exit("Error: k is greater than N")

    X = np.zeros((N, 1))
    y = np.zeros(N)

    for i in range(N):
        X[i] = float(input("Enter X: "))
        y[i] = float(input("Enter y: "))

    test_x = float(input("Enter test input X: " ))

    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, y)

    prediction = knn.predict([[test_x]])
    print(f'Prediction output: {prediction[0]}')

    variance = np.var(y)
    print(f'Traning set variance: {variance}')
