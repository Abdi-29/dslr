from parsing import check_input
import sys
from feature import Feature
import pandas as pd

def display_statistics_table(data, numerical_columns):
    features = [Feature(column, data[column].dropna().values) for column in numerical_columns]

    statistics = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

    table = {stat: [] for stat in statistics}

    for feature in features:
        stats = feature.calculate_statistics()
        for stat in statistics:
            table[stat].append(f"{stats[stat]:.6f}" if stats[stat] is not None else "N/A")

    header = " ".join([f"{f.name:>10}" for f in features])
    print(f"{'':>5} {header}")
    
    for stat in statistics:
        row = " ".join([f"{value:>15}" for value in table[stat]])
        print(f"{stat:<15} {row}")


if __name__ == "__main__":
    check_input(sys.argv)
    data = pd.read_csv(sys.argv[1], index_col=0)
    
    numerical_columns = [
        'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts',
        'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
        'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'
    ]
    
    display_statistics_table(data, numerical_columns)