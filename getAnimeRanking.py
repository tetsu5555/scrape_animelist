import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# ランキングを格納するリストを作成
csv_list = []

# アクセスするURL
url = "https://akiba-souken.com/anime/ranking/"

# リクエストしてhtmlを取得する
html = urllib.request.urlopen(url)

# htmlをパースする
soup = BeautifulSoup(html, "html.parser")

#idを作成
ids = range(1, 101)
for id in ids:
    csv_list.append([id])

# タイトルを取って来て配列に挿入
list = soup.select('h2 a')
for i in range(len(list)):
    csv_list[i].append(list[i].string)

# 画像一覧を取って来て、配列に挿入
imglist = soup.select('.itemImg a img')
for i in range(len(imglist)):
    csv_list[i].append(imglist[i]["src"])

# 説明欄を取って来て、配列に挿入
detail_list = soup.select('.itemTxt p')
for i in range(len(detail_list)):
    csv_list[i].append(detail_list[i].string)

# csvファイルを開く
f = open('animelist.csv', 'a')
writer = csv.writer(f, lineterminator='\n')

# CSVに書き込みを行う
for row in csv_list:
    writer.writerow(row)
f.close()
