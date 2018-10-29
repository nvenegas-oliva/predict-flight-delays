import pandas as pd


def load_dataset():
    df = pd.read_csv('datasets/baseSCL2017.csv',
                     parse_dates=['Fecha-I', 'Fecha-O'],
                     dtype={'Vlo-I': str, 'Vlo-O': str})
    df.drop(columns=['Unnamed: 0'], inplace=True)
    for col in df.columns:
        if df[col].nunique() < 100:
            df[col] = df[col].astype('category')
    df.set_index('Fecha-I', inplace=True)
    return df
