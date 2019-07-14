from html.parser import HTMLParser
import webbrowser
import sys

import requests


CHROME_PATH = 'open -a /Applications/Google\ Chrome.app %s'


class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'source':
            for name, value in attrs:
                if name == 'src':
                    print('opening video at', value)
                    webbrowser.get(CHROME_PATH).open(value)


book_num = int(sys.argv[1])
episode_num = int(sys.argv[2])
total_episode_num = episode_num + (book_num - 1) * 20

url = f'https://veohb.net/vid.php?video=avatar_the_last_airbender_{total_episode_num}'
resp = requests.get(url)
content = resp.content.decode()

parser = Parser()
parser.feed(content)
