import pandas as pd
import plotly.figure_factory as ff
import csv 
import statistics
import random 
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df['average'].tolist()

def remean(counter):
    dataone = []
    for i in range(0,counter):
        randomone = random.randint(0,len(data)-1)
        value = data[randomone]
        dataone.append(value)
    mean = statistics.mean(dataone)
    return mean

def showfig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([df],['average'],show_hist= False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1] , mode='lines', name='mean'))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        randommean = remean(100)
        mean_list.append(randommean)
    showfig(mean_list)

setup()

    