import matplotlib.pyplot as plt
from parsing import check_input
import pandas as pd
import sys
import seaborn as sb

def find_most_similar_features(data, numerical_columns):
    correlation_matrix = data[numerical_columns].corr(method='pearson')

    """
        print(correlation_matrix)
        sb.heatmap(correlation_matrix, 
                xticklabels=correlation_matrix.columns,
                yticklabels=correlation_matrix.columns,
                cmap='RdBu_r',
                annot=True,
                linewidth=0.5)
        plt.show()
    """

    corr_pairs = correlation_matrix.unstack()
    corr_pairs = corr_pairs[corr_pairs < 1]  # Exclude self-correlation
    sorted_corr = corr_pairs.sort_values(ascending=False)

    most_similar = sorted_corr.idxmax()
    highest_correlation = sorted_corr.max()

    return most_similar, highest_correlation


def plot_all_feature_pairs(data, numerical_columns):
    colors = {'Ravenclaw': 'blue', 'Slytherin': 'green', 'Gryffindor': 'red', 'Hufflepuff': 'orange'}
    
    most_similar_features, correlation_value = find_most_similar_features(data, numerical_columns)
    print(most_similar_features, correlation_value)
    # plt.style.use('ggplot')
    plt.figure(num='Similar features', figsize=(8,6))
    ax = plt.subplot(111)
    plt.title(f"The two features that are similar: {most_similar_features}")
    sb.scatterplot(x=most_similar_features[1], y=most_similar_features[0], hue='Hogwarts House', palette=colors, data=data, ax=ax)
    ax.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    check_input(sys.argv)

    data = pd.read_csv(sys.argv[1], index_col=0)

    numerical_columns = [
    'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts',
    'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
    'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'
    ]

    plot_all_feature_pairs(data, numerical_columns)