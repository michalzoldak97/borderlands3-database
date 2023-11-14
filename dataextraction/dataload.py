import requests as rq


def load_raw_html(url: str, target_pth: str):
    r = rq.get(url)

    print("doing request to {}".format(url))
    print(r.status_code)

    with open(target_pth, 'a') as f:
        f.write(str(r.content))
