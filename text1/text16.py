import requests
import json
from requests.exceptions import RequestException
import re
import time


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # 在Python的正则表达式中，有一个参数为re.S。它表示“.”（不包含外侧双引号，下同）的作用扩展到整个字符串，包括“\n”。
    items = re.findall(pattern, html)
    # compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象。
    # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:]if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:]if len(item[4]) > 5 else '',
            'score': item[5] + item[6]
        }

#a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
