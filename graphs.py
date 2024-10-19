import matplotlib.pyplot as plt




def create_plot(x, y, title):
    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.grid(True)
    plt.show()


