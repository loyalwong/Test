#-*-coding:utf-8-*-
import urllib2
from bs4 import BeautifulSoup
import string
import csv
import codecs
import sys

reload(sys)
sys.setdefaultencoding("utf8")

file_list = csv.reader(file('list.csv', 'rb'))
for line in file_list:
    url = line[0]
#    print(url)
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    episodes_new = []

    for link in soup.find_all('a'):
        if string.find(link.get_text(),'.mp4') != -1:
            newline = []
            newline.append( link.get_text())
            newline.append( link.get('href'))
            episodes_new.append(newline)

    title_code = string.split(url,'/')[4]

    try:
        file_episodes_old = csv.reader(codecs.open(title_code + '.csv','rb','utf-8'))
    except Exception:
        file_episodes_old = []
    episodes_old = []
    for line in file_episodes_old:
        episodes_old.append(line)

    episodes_diff = []
    if episodes_new != [] and episodes_old != []:
        for line in episodes_new:
            if string.find(episodes_old, line[0]) == -1:
                    episodes_diff.append(line)

    elif episodes_new != [] and episodes_old == []:
        episodes_diff = episodes_new

    if episodes_diff != []:
        writer = csv.writer(codecs.open(title_code + '.csv','wb','utf-8'))
        writer.writerows(episodes_new)
        writer = csv.writer(codecs.open('diff.csv','wb','utf-8'))
        writer.writerows(episodes_diff)


