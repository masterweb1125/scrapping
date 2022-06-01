import extruct
import requests
from w3lib.html import get_base_url
import time
import random


def extract_metadata(url):

    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
               'TE':'trailers', 'Accept':'*/*', 'Accept-Encoding':'gzip, deflate, br', 'Accept-Language':'en-US,en;q=0.5',
               'Cache-Control':'max-age=0', 'Connection':'keep-alive','Host':'www.hepsiemlak.com',
               'Sec-Fetch-Dest':'script','Referer':'https://www.hepsiemlak.com/istanbul-gungoren-tozkoparan-satilik/daire/0-38252071',
               'Sec-Fetch-Mode':'no-cors', 'Sec-Fetch-Site':'same-origin'
               }
    '''
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers)

    base_url = get_base_url(r.text, r.url)
    metadata = extruct.extract(r.text,
                               base_url=base_url,
                               uniform=True,
                               syntaxes=['json-ld',
                                         'microdata',
                                         'opengraph'])
    print(r.status_code)

    return metadata



if __name__ == "__main__":


    url = 'https://www.hepsiemlak.com/istanbul-avcilar-denizkoskler-satilik/daire/0-36934620'

    full_dict = extract_metadata(url)

    print(full_dict)
