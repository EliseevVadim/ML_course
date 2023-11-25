import matplotlib.pyplot as plt


def plot_time_series(df, title, x_label, y_label):
    df.plot(marker='.')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_prediction(actual, prediction, title, x_label, y_label):
    plt.plot(actual, marker='.', label="Реальные значения")
    plt.plot(prediction, marker='.', label="Спрогнозированные значения", color='green')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.tight_layout()
    plt.show()
