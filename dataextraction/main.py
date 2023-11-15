import dataload as dl
import dataextract as dex
import analysis


def main():
    # dl.load_raw_html('https://www.lootlemon.com/db/borderlands-3/shields',
    #                './data/shields-source.txt')
    # wd_ex = wd.WeaponDataExtractor('./data/weapons-source.txt')
    # analysis.analyze_w_df_inc(wd_ex.get_df())
    ex = dex.HTMLDataExtractor('data/shields-source.txt')
    print(ex.print_file_data())
    print(ex.get_df(-1).columns)


if __name__ == "__main__":
    main()
