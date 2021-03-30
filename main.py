from get_html import get_html
from save_file import save_file
from get_msg import get_msg
import time

def main():
    for i in range(0,10):
        offset = i * 10
        url = 'http://maoyan.com/board/4?offset=' + str(offset)
        html = get_html(url)
        for each in get_msg(html):
            save_file(each)

main()