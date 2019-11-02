import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Q1
diabetes_data = pd.read_csv(filepath_or_buffer='data/diabetes.data',
                      sep='\t',
                      header=0)
# Q2 - 1
pretty_print("Statistics summary Diabetes data", diabetes_data.describe())

# Q2 - 2
pretty_print("Correlation in Diabetes data", diabetes_data.corr())
