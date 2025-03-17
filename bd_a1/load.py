import pandas as pd

def load_dataset(path):
    df=pd.read_csv(path)
    return df

df=load_dataset('Sleep_health_and_lifestyle_dataset.csv')
print(df.head())