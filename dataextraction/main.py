import dataload as dl
import dataextract as dex
import analysis


# weapon: [:-4], shield: [:-1], grenade [3:-1], mod [3:], artifact [4:]


def main():
    # dl.load_raw_html('https://www.lootlemon.com/db/borderlands-3/artifacts',
    #                './data/artifacts-source.txt')
    ex = dex.HTMLDataExtractor('data/artifacts-source.txt')
    print(ex.print_file_data())
    print(ex.get_df(0, 0).columns)


if __name__ == "__main__":
    main()
