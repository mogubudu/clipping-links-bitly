import requests
import os
import argparse
from dotenv import load_dotenv
load_dotenv()


def create_parser():
    parser = argparse.ArgumentParser(description='''
      Программа получает на вход ссылку и сокращает её.
      Либо принимает сокращенную в bitlink ссылку
      и возвращает сумму кликов по ней.
      ''')
    parser.add_argument('link', help='Нужно ввести ссылку')
    return parser

user_token = os.getenv("BITLY_TOKEN")
headers = {"Authorization": "Bearer {}".format(user_token)}

user_url = "https://api-ssl.bitly.com/v4/user"
bitlinks_url = "https://api-ssl.bitly.com/v4/bitlinks"
bitlinks_summary_url = '''https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'''


def create_bitlink(url):
    if url.startswith("https://") or url.startswith("https://"):
        url = url
    else:
        url = 'http://' + url
    params = {
      "long_url": url
    }

    response = requests.post(bitlinks_url, json=params, headers=headers)
    if response.ok:
        return response.json()["id"]
    else:
        return "Проверьте корректность вводимой ссылки"


def count_clicks(bitlink):

    if bitlink.startswith("https://"):
        bitlink = bitlink[8:]
    elif bitlink.startswith("http://"):
        bitlink = bitlink[7:]

    params = {
        "unit": "day",
        "units": "-1"
    }

    bitlinks_summ_url = bitlinks_summary_url.format(bitlink)

    response = requests.get(bitlinks_summ_url, params=params, headers=headers)

    if response.ok:
        return response.json()["total_clicks"]
    else:
        return "Проверьте корректность вводимой ссылки"

parser = create_parser()
link = parser.parse_args()


def check_link(link):
    link = link.link
    if link.startswith("bit.ly"):
        return count_clicks(link)
    else:
        return create_bitlink(link)

if __name__ == "__main__":
    print(check_link(link))
