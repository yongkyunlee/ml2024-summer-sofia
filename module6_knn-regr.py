import numpy as np

class KNNRegressor:
    def __init__(self):
        self.x = np.array([])
        self.y = np.array([])

    def add_point(self, X, Y):
        if self.x.size == 0:
            self.x = np.array([X])
            self.y = np.array([Y])
        else:
            self.x = np.append(self.x, X)
            self.y = np.append(self.y, Y)

    def predict(self, X_pred, K):
        if K > len(self.x):
            raise ValueError("K cannot be larger than the number of data points")

        distances = np.abs(self.x - X_pred)
        k_nearest_indices = np.argsort(distances)[:K]
        k_nearest_y = self.y[k_nearest_indices]
        return np.mean(k_nearest_y)

if __name__ == "__main__":
    knn = KNNRegressor()

    N = int(input("Enter N: "))
    k = int(input("Enter k: "))
    if k > N:
        print("k cannot be larger than N")
        exit()

    for _ in range(N):
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        knn.add_point(x, y)

    input_x = float(input("Enter x to predict: "))

    try:
        result = knn.predict(input_x, k)
        print("Predicted y: ", result)
    except ValueError as e:
        print("Error:", str(e))
