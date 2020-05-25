import numpy as np
from matplotlib import pyplot as plt
import sys

if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    f1 = []
    f2 = []
    with open(file1) as f:
        lines = f.readlines()
        for line in lines:
            f1.append(float(line.strip()))
    with open(file2) as f:
        lines = f.readlines()
        for line in lines:
            f2.append(float(line.strip()))
    f1 = np.array(f1)
    f2 = np.array(f2)
    plt.boxplot([f1, f2], labels=['Strategy 1', 'Strategy 2'])
    plt.title("Fitness for 11 replications")
    plt.ylabel('Fitness')
    plt.show()

    print(f1.mean(), f1.std())
    print(f2.mean(), f2.std())
