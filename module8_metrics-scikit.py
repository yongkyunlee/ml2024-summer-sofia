import numpy as np
from sklearn.metrics import precision_score, recall_score

if __name__ == "__main__":
    N = int(input("Number of points: "))

    x = np.zeros(N, dtype=int)
    y = np.zeros(N, dtype=int)

    for i in range(N):
        x_input = int(input("X (Ground Truth): "))
        if x_input != 0 and x_input != 1:
            exit("X must be either 0 or 1")
        x[i] = x_input
        y_input = int(input("y (Predicted Class): "))
        if y_input != 0 and y_input != 1:
            exit("y must be either 0 or 1")
        y[i] = y_input

    precision = precision_score(x, y)
    recall = recall_score(x, y)

    print("\n")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
