import requests
import pandas as pd
import weapon_dataextract as wd


def _load_raw_html(url: str, target_pth: str):
    r = requests.get(url)

    print("doing request to {}".format(url))
    print(r.status_code)

    with open(target_pth, 'a') as f:
        f.write(str(r.content))

def analyze_df(df: pd.DataFrame):
    print(df.loc[df['content'].notna()].head()) # show rows where content column is not na
    print(df['rarity'].unique())
    df = df.loc[df['content'].notna()]
    print(df.loc[df['content']
                 .str.contains('base')]
                 .groupby('manufacturer')
                 .count()
                 .sort_values('rarity'))
    print(df.describe())


def main():
    # _load_raw_html('https://www.lootlemon.com/db/borderlands-3/weapons?3493d0c0_page=4',
    #                './data/weapons-source.txt')
    wd_ex = wd.WeaponDataExtractor('./data/weapons-source.txt')
    analyze_df(wd_ex.get_df())


if __name__ == "__main__":
    main()
