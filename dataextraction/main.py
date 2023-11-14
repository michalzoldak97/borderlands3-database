import requests
import pandas as pd
import weapon_dataextract as wd


def _load_raw_html(url: str, target_pth: str):
    r = requests.get(url)

    print("doing request to {}".format(url))
    print(r.status_code)

    with open(target_pth, 'a') as f:
        f.write(str(r.content))


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


def main():
    # _load_raw_html('https://www.lootlemon.com/db/borderlands-3/weapons?3493d0c0_page=4',
    #                './data/weapons-source.txt')
    wd_ex = wd.WeaponDataExtractor('./data/weapons-source.txt')
    analyze_w_df_inc(wd_ex.get_df())


if __name__ == "__main__":
    main()
