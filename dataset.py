

#%%
#Above command allows you to run interactive jupyter for graph
import pandas as pd
import numpy as np

# Great functions to create dataset
def get_dataset(size):
    # Create Fake Dataset
    df = pd.DataFrame()
    df['size'] = np.random.choice(['big', 'medium', 'small'], size)
    df ['age'] = np.random.randint(1, 50, size)
    df ['team' ] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win'] = np.random.choice(['yes', 'no'], size)
    dates = pd.date_range('2020-01-01', '2022-12-31')
    df['date'] = np.random.choice(dates, size)
    df['prob'] = np.random.uniform(0, 1, size)
    return df

df = get_dataset(4)

#y = {'f(x)': [2,10,6,8], 'g(x)': [4,2,-2,6]}
#x = [1,2,3,4]
x = df['date']
z = df['age']
y = [1,2,3,4]
graph = pd.DataFrame(y,x)
graph.plot(kind='line', grid=True, title="Ages on Dates", ylabel="my y title", xlabel="my x title")#, xlim = (1,4))
#z= "WAIT HERE"
# %%
