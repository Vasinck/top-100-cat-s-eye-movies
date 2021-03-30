import re

def get_msg(html):
    reg = r'<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="score">.*?.*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i>.*?</dd>'
    pattern = re.compile(reg,re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            '排名':item[0],
            '名称':item[1],
            '主演':item[2].strip()[3:],
            '时间':item[3].strip()[5:],
            '分数':item[4] + item[5],
        }
    

