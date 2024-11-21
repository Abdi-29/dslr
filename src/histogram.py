import matplotlib.pyplot as plt
from parsing import check_input
from feature import std_deviation
import pandas as pd
import sys


import matplotlib.pyplot as plt

def calculate_course_homogeneity(numerical_columns, houses, grouped_data):
    homogeneity_scores = {}

    for course in numerical_columns:
        stds = []
        for house in houses:
            house_data = grouped_data.get_group(house)[course].dropna()
            std = std_deviation(house_data)
            stds.append(std)
        homogeneity_scores[course] = std_deviation(stds)

    most_homogeneous_course = min(homogeneity_scores, key=homogeneity_scores.get)
    return homogeneity_scores, most_homogeneous_course

def show_focused_histogram(most_homogeneous_course, houses, grouped_data):
    colors = {'Ravenclaw': 'blue', 'Slytherin': 'green', 'Gryffindor': 'red', 'Hufflepuff': 'orange'}

    plt.figure(figsize=(8, 6))
    for house in houses:
        house_data = grouped_data.get_group(house)[most_homogeneous_course].dropna()
        plt.hist(house_data, bins=10, alpha=0.5, label=house, color=colors[house], density=True)

    plt.title(f"Most Homogeneous Course: {most_homogeneous_course}")
    plt.xlabel("Score")
    plt.ylabel("Frequency (Density)")
    plt.legend(loc='best')
    plt.show()



if __name__ == "__main__":
    check_input(sys.argv)

    data = pd.read_csv(sys.argv[1], index_col=0)

    numerical_columns = [
    'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts',
    'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
    'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'
    ]

    houses = data['Hogwarts House'].unique()

    grouped_data = data.groupby('Hogwarts House')

    homogeneity_scores, most_homogeneous_course = calculate_course_homogeneity(numerical_columns, houses, grouped_data)
    print(f"Homogeneity Scores: {homogeneity_scores}")
    print(f"The most homogeneous course is: {most_homogeneous_course}")

    show_focused_histogram(most_homogeneous_course, houses, grouped_data)

