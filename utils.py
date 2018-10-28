import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


def load_dataset():
    df = pd.read_csv('datasets/baseSCL2017.csv', dtype={'Vlo-I': str, 'Vlo-O': str})
    df.drop(columns=['Unnamed: 0'], inplace=True)
    for col in df.columns:
        if df[col].nunique() < 100:
            df[col] = df[col].astype('category')
    return df


df.info()

df['DIANOM'] = df['DIANOM'].astype(str)
df.info()
df['DIANOM'].value_counts()


df = pd.read_csv('datasets/baseSCL2017.csv', dtype={'Vlo-I': str, 'Vlo-O': str})
df.drop(columns=['Unnamed: 0'], inplace=True)
df['DIANOM'].value_counts()
_ = plt.hist(df['DIANOM'].value_counts())
plt.show()
