import matplotlib.pyplot as plt
# import numpy as np
from IPython import display

plt.ion()

# RED = (200,0,0)
# BLUE2 = (0, 100, 255)


def plot(scores, mean_scores):
    display.clear_output(wait=True)
    # for ax in plt.gcf().axes:
    #     ax.get_lines()[0].set_color("blue")
    display.display(plt.gcf())
    # plt.clf()


    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')

    plt.plot(scores,"r-") # red lin
    plt.plot(mean_scores,color="blue")

    plt.ylim(ymin=0)

    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))