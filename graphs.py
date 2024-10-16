import matplotlib.pyplot as plt




def create_plot(x, y, kind):
    plt.figure()
    plt.plot(x, y, kind=kind)
    plt.grid(True)
    plt.show()


