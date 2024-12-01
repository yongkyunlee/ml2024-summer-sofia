import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, LeaveOneOut

if __name__ == "__main__":
    N = int(input("Number of points in training set: "))
    if N <= 0:
        exit('N must be a positive integer.')
    X_train = np.zeros(N, dtype=int)
    y_train = np.zeros(N, dtype=int)
    for i in range(N):
        X_train[i] = float(input("X (real number): "))
        y_train[i] = int(input("y (non-negative integer): "))
        if y_train[i] < 0:
            exit("y must be a non-negative integer")

    M = int(input("Number of points in test set: "))
    if M <= 0:
        exit("M must be a positive integer.")
    X_test = np.zeros(M)
    y_test = np.zeros(M, dtype=int)
    for i in range(M):
        X_test[i] = float(input("X (real number): "))
        y_test[i] = int(input("y (non-negative integer): "))
        if y_test[i] < 0:
            exit("y must be a non-negative integer")

    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)

    cv = LeaveOneOut()
    grid_param = {'n_neighbors': range(1, min(N, M, 11))}
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, grid_param, cv=cv)
    grid_search.fit(X_train, y_train)

    best_k = grid_search.best_params_['n_neighbors']
    test_accuracy = grid_search.score(X_test, y_test)

    print(f"Best K: {best_k}")
    print(f"Test accuracy for best k: {test_accuracy}")
