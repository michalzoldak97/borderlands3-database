import requests
import pandas as pd
import weapon_dataextract as wd


def _load_raw_html(url: str, target_pth: str):
    r = requests.get(url)

    print("doing request to {}".format(url))
    print(r.status_code)

    with open(target_pth, 'a') as f:
        f.write(str(r.content))


def main():
    # _load_raw_html('https://www.lootlemon.com/db/borderlands-3/weapons?3493d0c0_page=4',
    #                './data/weapons-source.txt')
    wd_ex = wd.WeaponDataExtractor('./data/weapons-source.txt')
    df = wd_ex.get_df()
    print(df.head())


if __name__ == "__main__":
    main()
