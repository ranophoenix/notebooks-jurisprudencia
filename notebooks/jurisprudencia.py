import pandas as pd

def load_dataset():
    df = pd.read_csv('dataset/asg.csv.gz', parse_dates=['data'])
    
    return df