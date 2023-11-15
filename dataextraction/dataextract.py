import pandas as pd


class HTMLDataExtractor():
    EX_ELEMENTS = ["nonelemental", "incindiary", "shock", "corrosive", "cryo", "radiation"]

    def __init__(self, raw_source_txt_pth: str):
        self.raw_source_txt_pth = raw_source_txt_pth

    def _extract_elements_data(self, chunk: list) -> dict:
        elements = []
        for i, c in enumerate(chunk):
            if c[-3:] == 'svg' and any([el in c for el in self.EX_ELEMENTS]):
                if 'invisible' in chunk[i + 10]:
                    continue

                el = c.split('_')[1][:-4]
                elements.append(el)

        if len(elements) < 1:
            return {}

        return {"name": "elements", "data": elements}

    def _extract_attr_data(self, attr_text: str) -> dict:
        f = attr_text.split('"')
        if len(f) > 3:
            el_data = self._extract_elements_data(f)
            if el_data:
                return el_data
            return {}

        if len(f) < 2 or len(f[1]) < 1:
            return {}

        return {"name": f[0][1:-1], "data": f[1]}

    def _extract_attr(self, field: str) -> dict:
        field_data_split = _get_readable_list(field.lower().split('data'))

        res = {}
        for i, f in enumerate(field_data_split):
            fd = self._extract_attr_data(f)
            if fd:
                res[fd['name']] = fd['data']

        return res

    def _get_file_text(self) -> list:
        file = ''
        with open(self.raw_source_txt_pth) as f:
            file = f.read()

        return file.split('<div class="db_item-data')

    def extract_file_data(self) -> list:
        data_fields = []
        for line in self._get_file_text():
            line_attributes_data = self._extract_attr(line)
            if line_attributes_data:
                data_fields.append(line_attributes_data)

        return data_fields

    def get_df(self, start_idx: int, stop_idx: int) -> pd.DataFrame:
        df = pd.DataFrame.from_records(self.extract_file_data())

        if stop_idx == 0:
            return df[df.columns[start_idx:]]

        return df[df.columns[start_idx:stop_idx]]
    
    def print_file_data(self):
        f_data = self.extract_file_data()
        for l in f_data:
            print(l)
        
        print("File data consists of {} lines".format(len(f_data)))


def _get_readable_list(all_fields: list) -> list:
    for i, f in enumerate(all_fields):
        if len(f) < 1:
            del all_fields[i]
            continue

        if f[0] != '-':
            del all_fields[i]
            continue

        if f.find('=') == -1:
            del all_fields[i]

    return all_fields
