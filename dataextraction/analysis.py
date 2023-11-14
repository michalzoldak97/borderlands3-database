import pandas as pd


def analyze_w_df(df: pd.DataFrame):
    print(df.loc[df['content'].notna()].head())  # show rows where content column is not na
    print(df['rarity'].unique())
    df = df.loc[df['content'].notna()]
    print(df.loc[df['content']
          .str.contains('base')]
          .groupby('manufacturer')
          .count()
          .sort_values('rarity'))
    print(df.describe())


def analyze_w_df_inc(df: pd.DataFrame):
    df = df.loc[df['content'].notna()]
    base_df = df.loc[df['content'].str.contains('base')].copy()
    pd.options.display.max_columns = None
    print(base_df.describe())
    rarities = ['f-legendary', 'd-epic']
    w_type = 'assault-rifle-bl3'
    print(base_df.loc[base_df['elements']
          .apply(lambda elements: len(elements) == 1 and 'incindiary' in elements)]
          .query("rarity in @rarities")
          .query("type == @w_type"))