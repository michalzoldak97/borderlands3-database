import dataload as dl
import weapon_dataextract as wd
import shield_dataextract as sd
import analysis


def main():
    # dl.load_raw_html('https://www.lootlemon.com/db/borderlands-3/shields',
    #                './data/shields-source.txt')
    # wd_ex = wd.WeaponDataExtractor('./data/weapons-source.txt')
    # analysis.analyze_w_df_inc(wd_ex.get_df())
    sd_ex = sd.ShieldDataExtractor('data/shields-source.txt')
    sd_ex.print_file_data()


if __name__ == "__main__":
    main()
