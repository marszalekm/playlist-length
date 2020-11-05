from bs4 import BeautifulSoup
import requests


def playlistlength(url):

    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        block = soup.find_all('script')[-4].contents[0]
        total = []
        for line in block.split():
            if 'lengthSeconds' in line:
                for param in line.split(','):
                    if param.startswith('"lengthSeconds"'):
                        seconds = param.split(':')[1]
                        total.append(int(seconds.strip('"')))

        hours = sum(total) / 3600
        minutes = sum(total) % 3600 / 60
        seconds = sum(total) % 3600 % 60
        return int(hours), int(minutes), seconds

    else:
        return 'wrong_url'
