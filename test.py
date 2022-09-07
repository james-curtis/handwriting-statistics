import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.scatter([i for i in range(99)], [i for i in range(99)])
    plt.ylabel('some numbers')
    plt.show()
