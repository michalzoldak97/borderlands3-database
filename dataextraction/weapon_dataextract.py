import dataextract as dex


class WeaponDataExtractor(dex.HTMLDataExtractor):
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
