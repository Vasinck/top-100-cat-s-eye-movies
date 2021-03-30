import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36'}

def get_html(url):
    html = requests.get(url,headers = headers)
    if html.status_code == 200:
        return html.text
    else:
        return None