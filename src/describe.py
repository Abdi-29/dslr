from parsing import check_input
import sys
from feature import Feature, NUMERICAL_COLUMNS
import pandas as pd

def display_statistics_table(data):
    features = [Feature(column, data[column].dropna().values) for column in NUMERICAL_COLUMNS]

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
    
    display_statistics_table(data)