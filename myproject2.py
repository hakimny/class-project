import sys
import pandas as pd
import matplotlib.pyplot as plt


# sys.argv allows us to have access to parameters passed to a script when its called
file_name = sys.argv[0]
data_file = sys.argv[1]
column1 = sys.argv[2]
column2 = ""
if len(sys.argv) == 4:
	column2 = sys.argv[3]

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# Advanced Section
# Q1
data = pd.read_csv(filepath_or_buffer=data_file,
                      sep="\t",
                      header=0)
# Q2 - 1
pretty_print("Statistics summary for data", data.describe())

# Q2 - 2
pretty_print("Correlation in data", data.corr())

# Reach Section

# Plotting histogram
plt.plot(data[column1], color='g')
plt.title('Data')
plt.xlabel(column1)
plt.ylabel('Count')
image = 'plots/' + column1 + "_plot.png"
plt.savefig(f'{image}', format='png')
plt.clf()

if column2 != "":
	# Plotting scatterplot
	print("Here")
	plt.scatter(data[column1], data[column2], color='r')
	title = column1 + " to " + column2
	plt.title(title)
	plt.xlabel(column1)
	plt.ylabel(column2)
	image = 'plots/' + column1 + "_to_" + column2 + ".png"
	plt.savefig(f'{image}', format='png') 
	print(image)