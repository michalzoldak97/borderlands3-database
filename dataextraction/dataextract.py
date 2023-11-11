import abc
import pandas as pd


class HTMLDataExtractor(abc.ABC):
    EX_ELEMENTS = ["nonelemental", "incindiary", "shock", "corrosive", "cryo", "radiation"]

    def __init__(self, raw_source_txt_pth: str):
        self.raw_source_txt_pth = raw_source_txt_pth

    @abc.abstractmethod
    def _extract_attr_data(self, attr_text: str) -> dict:
        """
        extracts data for a single data attribute
        :param attr_text:
        :return: dictionary with attribute name and value
        """

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

    def get_df(self) -> pd.DataFrame:
        df = pd.DataFrame.from_records(self.extract_file_data())
        return df[df.columns[:-4]]
    
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
