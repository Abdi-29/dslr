import matplotlib.pyplot as plt
from parsing import check_input
import pandas as pd
import sys
import itertools


# def scatter_plot(numerical_columns, houses, grouped_data):
#     colors = {
#                 'Ravenclaw': 'blue',
#                 'Slytherin': 'green',
#                 'Gryffindor': 'red',
#                 'Hufflepuff': 'orange'
#             }
#     nrows, ncols = 3, 5

if __name__ == "__main__":
    check_input(sys.argv)

    data = pd.read_csv(sys.argv[1], index_col=0)

    numerical_columns = [
    'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts',
    'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
    'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'
    ]

    houses = data['Hogwarts House'].unique()

    colours = {
    'Gryffindor': 'red',
    'Ravenclaw': 'blue',
    'Slytherin': 'green',
    'Hufflepuff': 'orange'
}

    feature_pairs = list(itertools.combinations(numerical_columns, 2))
    nrows, ncols = 10, 5
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(20, 20))
    fig.suptitle("Scatter Plots of Hogwarts Courses by House", fontsize=16)

    axes = axes.flatten()

    for i, (feature1, feature2) in enumerate(feature_pairs):
        if i >= len(axes):
            break

        ax = axes[i]
        for house in houses:
            house_data = data[data['Hogwarts House'] == house]
            ax.scatter(
                house_data[feature1],
                house_data[feature2],
                alpha=0.6,
                label=house,
                color=colours[house]
            )
        ax.set_title(f"{feature1} vs {feature2}")
        ax.set_xlabel(feature1)
        ax.set_ylabel(feature2)

    # Remove empty subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])


    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=4, fontsize='large')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
