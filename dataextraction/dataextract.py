import requests
import weapon_dataextract as wd


def _improve_readability(f_pth: str):
    file = ''
    with open(f_pth) as f:
        file = f.read()

    file = (
        file
            .replace('<div class="db_item-data', '\n<div class="db_item-data')
    )

    with open('data/weapons-processed.txt', 'w') as p:
        p.write(file)


def _load_raw_html(url: str, target_pth: str):
    r = requests.get(url)

    print("doing request to {}".format(url))
    print(r.status_code)

    with open(target_pth, 'a') as f:
        f.write(str(r.content))


def main():
    # _load_raw_html('https://www.lootlemon.com/db/borderlands-3/weapons?3493d0c0_page=4',
    #                './data/weapons-source.txt')
    # _improve_readability('./data/weapons-source.txt')
    print("dataset contains {} weapons".format(wd.extract_weapon_data('data/weapons-processed.txt')))


if __name__ == "__main__":
    main()
