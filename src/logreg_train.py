import matplotlib.pyplot as plt
from parsing import check_input
from feature import NUMERICAL_COLUMNS, HOUSES
import pandas as pd
import sys
import seaborn as sb

def process_data(data):
    x = data[NUMERICAL_COLUMNS].fillna(0)

    x = (x - x.mean()) / x.std()

    x.insert(0, 'Bias', 1)

    return x.values

if __name__ == "__main__":
    check_input(sys.argv)

    data = pd.read_csv(sys.argv[1], index_col=0)

    houses = data['Hogwarts House'].unique()
    y_encode = {house: (data['Hogwarts House'] == house).astype(int) for house in houses}
    print(y_encode)

    process_data(data)