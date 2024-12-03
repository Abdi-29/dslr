import matplotlib.pyplot as plt
from parsing import check_input
import pandas as pd
from feature import NUMERICAL_COLUMNS, HOUSES
import sys
import seaborn as sb

def show_pair_plot(data):
    colors = {'Ravenclaw': 'blue', 'Slytherin': 'green', 'Gryffindor': 'red', 'Hufflepuff': 'orange'}

    sb.pairplot(
        data[NUMERICAL_COLUMNS + [HOUSES]],
        hue=HOUSES,
        palette=colors,
        height=2.5,
        diag_kind="hist",
        plot_kws={'alpha': 0.7}
    )

    plt.suptitle("Pair Plot of Hogwarts Courses by House", y=1.02)
    plt.savefig("pair_plot_improved.png", dpi=300, bbox_inches="tight")
    # plt.show()

if __name__ == "__main__":
    check_input(sys.argv)

    data = pd.read_csv(sys.argv[1], index_col=0)

    grouped_data = data.groupby(HOUSES)
    show_pair_plot(data)