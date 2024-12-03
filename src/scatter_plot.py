import matplotlib.pyplot as plt
from parsing import check_input
import pandas as pd
from feature import NUMERICAL_COLUMNS, HOUSES
import sys
import seaborn as sb

def find_most_similar_features(data):
    correlation_matrix = data[NUMERICAL_COLUMNS].corr(method='pearson')

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


def plot_all_feature_pairs(data):
    colors = {'Ravenclaw': 'blue', 'Slytherin': 'green', 'Gryffindor': 'red', 'Hufflepuff': 'orange'}
    
    most_similar_features, correlation_value = find_most_similar_features(data)
    print(most_similar_features, correlation_value)
    # plt.style.use('ggplot')
    plt.figure(num='Similar features', figsize=(8,6))
    ax = plt.subplot(111)
    plt.title(f"The two features that are similar: {most_similar_features}")
    sb.scatterplot(x=most_similar_features[1], y=most_similar_features[0], hue=HOUSES, palette=colors, data=data, ax=ax)
    ax.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    check_input(sys.argv)

    data = pd.read_csv(sys.argv[1], index_col=0)

    plot_all_feature_pairs(data)