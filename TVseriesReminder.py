import urllib2
from bs4 import BeautifulSoup
import string
import csv

TV_list = csv.reader(file('list.csv', 'rb'))
for line in TV_list:
    url = line[0]
    print(url)
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    episodes_new = []
    file1 = file('csv_test.csv','wb')
    writer = csv.writer(file1)
    for link in soup.find_all('a'):
        if string.find(link.get_text(),'.mp4') != -1:
#            newline = ["('" +  link.get_text() + "')" + "," +  "('" + link.get('href') + "')" ]
            writer.writerow(('rpw'))
#            episodes_new = episodes_new + newline
#    print episodes_new

    writer.writerows(episodes_new)

    title_code = string.split(url,'/')[4]
    try:
        episodes_old = csv.reader(file(title_code + '.csv','rb'))
    except IOError:
        episodes_old = csv.reader(file(title_code + '.csv','wb'))
    print episodes_old

