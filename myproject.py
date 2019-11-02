import pandas as pd
import matplotlib.pyplot as plt

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# Advanced Section
# Q1
diabetes_data = pd.read_csv(filepath_or_buffer='data/diabetes.data',
                      sep='\t',
                      header=0)
# Q2 - 1
pretty_print("Statistics summary Diabetes data", diabetes_data.describe())

# Q2 - 2
pretty_print("Correlation in Diabetes data", diabetes_data.corr())

# Reach Section

# Plotting histogram
plt.plot(diabetes_data['BMI'], color='g')
plt.title('DIABETES - BMI')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.savefig(f'plots/bmi_plot.png', format='png')
plt.clf()


# Plotting scatterplot
plt.scatter(diabetes_data['AGE'], diabetes_data['BMI'], color='r')
plt.title('Age to BMI')
plt.xlabel('AGE')
plt.ylabel('BMI')
plt.savefig(f'plots/age_to_bmi.png', format='png')