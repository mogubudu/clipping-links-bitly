import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
USER_TOKEN = os.getenv("BITLY_TOKEN")


def create_parser():
    parser = argparse.ArgumentParser(description='''
      Программа получает на вход ссылку и сокращает её.
      Либо принимает сокращенную в bitlink ссылку
      и возвращает сумму кликов по ней.
      ''')
    parser.add_argument('link', help='Нужно ввести ссылку')
    return parser


def create_bitlink(url):
    bitlinks_url = "https://api-ssl.bitly.com/v4/bitlinks"

    if urlparse(url).scheme == '':
        url = f'http://{url}'

    params = {
      "long_url": url
    }

    response = requests.post(
        bitlinks_url,
        json=params,
        headers={"Authorization": "Bearer {}".format(USER_TOKEN)})

    if response.ok:
        return response.json()["id"]
    else:
        return


def count_clicks(bitlink):
    bitlinks_summary_url = '''https://api-ssl.bitly.com/v4/bitlinks/
                            {}/clicks/summary'''

    bitlink = urlparse(bitlink)
    bitlink = f'{bitlink.netloc}{bitlink.path}'

    params = {
        "unit": "day",
        "units": "-1"
    }

    bitlinks_summ_url = bitlinks_summary_url.format(bitlink)

    response = requests.get(
        bitlinks_summ_url,
        params=params,
        headers={"Authorization": "Bearer {}".format(USER_TOKEN)})

    if response.ok:
        return response.json()["total_clicks"]
    else:
        return


def get_count_click_or_create_link(link):
    link = link.link
    if link.startswith("bit.ly"):
        return count_clicks(link)
    else:
        return create_bitlink(link)


def main():
    parser = create_parser()
    LINK = parser.parse_args()
    print(get_count_click_or_create_link(LINK))


if __name__ == "__main__":
    main()
