import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("Project/md.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_dev)

first_std_deviation_start, first_std_deviation_end = mean-std_dev, mean+std_dev
second_std_deviation_start, second_std_deviation_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_dev), mean+(3*std_dev)
print("Standard deviation 1:",first_std_deviation_start, first_std_deviation_end)
print("Standard deviation 2:",second_std_deviation_start, second_std_deviation_end)
print("Standard deviation 3:",third_std_deviation_start,third_std_deviation_end)

df = pd.read_csv("Project/md.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample 1: ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="Mean of intervention data"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score1 = (mean - mean_of_sample1)/std_dev
print("The z-score is",z_score1)
