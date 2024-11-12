import matplotlib.pyplot as plt
from parsing import check_input
import pandas as pd
import sys


def show_histogram(data, numerical_columns):
    houses = data['Hogwarts House'].unique()
    print(houses)
    grouped_data = data.groupby('Hogwarts House')
    print(grouped_data.get_group('Gryffindor').head())

    fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(15, 15))
    fig.suptitle("Hogwarts Courses Score Distribution by House")

    for i, column in enumerate(numerical_columns):
        ax = axes[i // 4, i % 4]
        
        for house in houses:
            house_data = grouped_data.get_group(house)[column].dropna()
            ax.hist(house_data, alpha=0.5, label=house, bins=10)
        
        ax.set_title(column)
        # ax.set_xlabel("Score")
        ax.set_ylabel("Frequency")
        ax.legend()

    plt.tight_layout(rect=[10, 0.03, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    check_input(sys.argv)

    data = pd.read_csv(sys.argv[1], index_col=0)

    numerical_columns = [
    'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts',
    'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
    'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'
    ]

    show_histogram(data, numerical_columns)

