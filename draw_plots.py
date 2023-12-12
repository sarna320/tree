import matplotlib.pyplot as plt


# Autor Pawel Sarnacki
def draw_one_plot(times, number_data, what=""):
    ax = plt.subplots()[1]
    ax.plot(number_data, times)
    ax.set_xlabel("Number of entry data")
    ax.set_ylabel(f"Time of {what} [s]")
    # ax.legend()
    ax.set_title(f"For {what} operations")
    plt.savefig("plots/" + f"{what}" + ".png")
    plt.show()

# Autor Piotr Niedziałek
def draw_plots(times1, times2, number_data, label1="", label2=""):
    fig, ax = plt.subplots()
    ax.plot(number_data, times1, label=label1)
    ax.plot(number_data, times2, label=label2)
    ax.set_xlabel("Number of entry data")
    ax.set_ylabel("Time [s]")
    ax.legend()
    ax.set_title("For operations")
    plt.savefig("plots/" + f"{label1}_{label2}" + ".png")
    plt.show()
