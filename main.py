import requests
import os
import argparse
from dotenv import load_dotenv

HEADERS = {"Authorization": "Bearer {}".format(USER_TOKEN)}
USER_URL = "https://api-ssl.bitly.com/v4/user"
BITLINKS_URL = "https://api-ssl.bitly.com/v4/bitlinks"
BITLINKS_SUMMARY_URL = '''https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'''

load_dotenv()
USER_TOKEN = os.getenv("BITLY_TOKEN")

def create_parser():
    parser = argparse.ArgumentParser(description='''
      Программа получает на вход ссылку и сокращает её.
      Либо принимает сокращенную в bitlink ссылку
      и возвращает сумму кликов по ней.
      ''')
    PARSER.add_argument('link', help='Нужно ввести ссылку')
    return PARSER

PARSER = create_parser()
LINK = PARSER.parse_args()

def create_bitlink(url):
    if url.startswith("http://") or url.startswith("https://"):
        url = url
    else:
        url = 'http://' + url
    params = {
      "long_url": url
    }

    response = requests.post(BITLINKS_URL, json=params, headers=HEADERS)
    if response.ok:
        return response.json()["id"]
    else:
        return


def count_clicks(bitlink):

    if bitlink.startswith("https://"):
        bitlink = bitlink[8:]
    elif bitlink.startswith("http://"):
        bitlink = bitlink[7:]

    params = {
        "unit": "day",
        "units": "-1"
    }

    bitlinks_summ_url = BITLINKS_SUMMARY_URL.format(bitlink)

    response = requests.get(bitlinks_summ_url, params=params, headers=HEADERS)

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
