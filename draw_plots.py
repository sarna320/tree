import matplotlib.pyplot as plt


# Autor Pawel Sarnacki
def draw_plots(times, number_data,what=""):
    ax = plt.subplots()[1]  
    ax.plot(number_data, times)
    ax.set_xlabel("Number of entry data")
    ax.set_ylabel(f"Time of {what} [s]")
    #ax.legend()
    ax.set_title(f"For {what} operations")
    plt.savefig("plots/" + f"{what}" + ".png")
    plt.show()


    
