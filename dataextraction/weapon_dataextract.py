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
        return {}

    return {"name": "elements", "data": elements}


def _extract_attr_data(attr_text: str) -> dict:
    f = attr_text.split('"')
    if len(f) > 3:
        el_data = _extract_elements_data(f)
        if el_data:
            return el_data
        return {}

    if len(f) < 2 or len(f[1]) < 1:
        return {}

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
        if fd:
            res[fd['name']] = fd['data']

    return res


def extract_weapon_data(f_pth: str) -> int:
    cnt = 0
    with open(f_pth) as data_file:
        for line in data_file.readlines():
            cnt += 1
            print(_extract_attr(line))

    return cnt
