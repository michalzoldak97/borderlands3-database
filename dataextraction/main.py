import dataload as dl
import weapon_dataextract as wd
import analysis


def main():
    # dl.load_raw_html('https://www.lootlemon.com/db/borderlands-3/weapons?3493d0c0_page=4',
    #                './data/weapons-source.txt')
    wd_ex = wd.WeaponDataExtractor('./data/weapons-source.txt')
    analysis.analyze_w_df_inc(wd_ex.get_df())


if __name__ == "__main__":
    main()
