

#%%
#Above command allows you to run interactive jupyter for graph
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Great functions to create dataset
def get_dataset(size):
    # Create Fake Dataset
    df = pd.DataFrame()
    #df['size'] = np.random.choice(['big', 'medium', 'small'], size)
    #df ['team' ] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    #df['win'] = np.random.choice(['yes', 'no'], size)
    dates = pd.date_range('2020-01-01', '2022-12-31')
    #df['date'] = np.random.choice(dates, size)
    df['date'] = (2015,2016,2017,2018)
    df['friends'] = (2,3,5,7)
    df['moles'] = np.random.randint(1, 7, size)
    return df

df = get_dataset(4)
randomnumbertest = np.random.randint(20, 50)
graph =df
#specify x axis 
graph.plot(kind='line', x='date', grid=True, title="Ages on Dates", ylabel="Life Indicators", xlabel="Date", ylim = (1,10))
#plt.show() #if not using jupyter
# %%
