import pandas as pd


def analyze_w_df(df: pd.DataFrame):
    print(df.loc[df['content'].notna()].head())  # show rows where content column is not na
    print(df['type'].unique())  # 1. show unique item rarities
    df = df.loc[df['content'].notna()]

    print(df.loc[(df['content']  # 2. show how many SMGs offers each manufacturer for a base game
          .str.contains('base')) & (df['type'] == 'smg-bl3')]
          .value_counts('manufacturer'))

     #print(df.query('rarity == "d-epic" and type == "sniper-bl3"').groupby('manufacturer').count())

    print(df.query('rarity == "d-epic" and type == "sniper-bl3"').value_counts('manufacturer'))  # 3. show which \
    # manufacturer offers the greatest number of epic snipers


def analyze_w_df_inc(df: pd.DataFrame):
    df = df.loc[df['content'].notna()]
    base_df = df.loc[df['content'].str.contains('base')].copy()
    pd.options.display.max_columns = None
    print(base_df.describe())
    # 4. show assault rifles that are epic or legendary and have only incindiary element
    rarities = ['f-legendary', 'd-epic']
    w_type = 'assault-rifle-bl3'
    print(base_df.loc[base_df['elements']
          .apply(lambda elements: len(elements) == 1 and 'incindiary' in elements)]
          .query("rarity in @rarities and type == @w_type"))
