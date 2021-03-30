import json

def save_file(content):
    with open(r'C:\Users\Administrator\Documents\python编程源程序\抓取猫眼电影排行TOP100\result.txt','a',encoding = 'utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n' + '\n')
