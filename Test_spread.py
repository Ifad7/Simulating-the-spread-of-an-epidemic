from Hate_bein_sick import Disease as dis
import matplotlib.pyplot as plt
import matplotlib.animation as anime
covid = {
    "r0": 2.28,
    "incubation": 5,
    "percent_mild": 0.8,
    "mild_recovery": (7, 14),
    "percent_severe": 0.2,
    "severe_recovery": (21, 42),
    "severe_death": (14, 56),
    "fatality_rate": 0.034,
    "serial_interval": 7
}

def main():
    coronavirus = dis(covid)
    coronavirus.animate()
    plt.show()

if __name__ == "__main__":
    main()
