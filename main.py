import numpy as np
from matplotlib import pyplot as plt


def main():
    np.random.seed(160698)
    x = [1, 2, 3, 4]
    px = [0.2, 0.15, 0.3, 0.35]
    pxx = [0.2, 0.35, 0.65, 1.0]
    y = [1, 2, 3, 4]
    py = [0.35, 0.5, 0, 0.15]
    pyy = [0.35, 0.85, 0.85, 1.0]
    pxy = [[0, 1, 0, 0],
           [1.0/3.0, 0, 0, 1],
           [0, 1, 0, 0],
           [0.3/0.35, 0, 0, 1]]

    values = []
    for _ in range(10000):
        rx, ry = np.random.rand(2)
        for x in range(4):
            if rx < pxx[x]:
                for y in range(4):
                    if ry < pxy[x][y]:
                        values.append([x+1, y+1])
                        break
                break
    for pair in values:
        print(pair)




if __name__ == '__main__':
    main()
