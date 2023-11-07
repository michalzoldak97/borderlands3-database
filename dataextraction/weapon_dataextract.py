import requests


EX_ELEMENTS = ["nonelemental", "incindiary", "shock", "corrosive", "cryo", "radiation"]


def _extract_elements_data(chunk: list) -> dict:
    elements = []
    for i, c in enumerate(chunk):
        if c[-3:] == 'svg' and any([el in c for el in EX_ELEMENTS]):
            if 'invisible' in chunk[i + 10]:
                continue

            el = c.split('_')[1][:-4]
            elements.append(el)

    if len(elements) < 1:
        return None

    return {"name": "elements", "data": elements}


def _extract_attr_data(attr_text: str) -> dict:
    f = attr_text.split('"')
    if len(f) > 3:
        el_data = _extract_elements_data(f)
        if el_data != None:
            return el_data
        return None
    
    if len(f) < 2 or len(f[1]) < 1:
        return None
    
    return {"name": f[0][1:-1], "data": f[1]}


def _get_readable_list(all_fields: list) -> list:
    for i, f in enumerate(all_fields):
            if f[0] != '-':
                del all_fields[i]
                continue

            if f.find('=') == -1:
                del all_fields[i]

    return all_fields


def _extract_attr(field: str) -> dict:
    field_data_split = _get_readable_list(field.lower().split('data'))

    res = {}
    for i, f in enumerate(field_data_split):
      fd = _extract_attr_data(f)
      if fd != None:
            res[fd['name']] = fd['data']

    return res


def _extract_weapon_data() -> int:
    cnt = 0
    with open('data/weapons-processed.txt') as data_file:
        for line in data_file.readlines():
            if line != None:
                cnt += 1
                print(_extract_attr(line))
    
    return cnt


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
    #_improve_readability('./data/weapons-source.txt')
    print("dataset contains {} weapons".format(_extract_weapon_data()))


if __name__ == "__main__":
    main()
