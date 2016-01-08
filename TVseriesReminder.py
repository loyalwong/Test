# -*-coding:utf-8-*-
import urllib2
from bs4 import BeautifulSoup
import string
import csv
import codecs
import sys
import smtplib
from email.mime.text import MIMEText
import time


def send_mail(sub, content):
    mailto_list = ['loyalwong@gmail.com']
    mail_host = "smtp.gmail.com"  # 设置服务器
    mail_port = 465
    mail_user = "loyalwong.ifttt@gmail.com"  # 用户名
    mail_pass = "wyzmsjylezewnqjf"  # 口令
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = '美剧' + sub + '已更新'
    msg['From'] = u"美剧更新自动提醒"
    msg['To'] = ";".join(mailto_list)
    try:
        server = smtplib.SMTP_SSL(mail_host, mail_port)
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(mail_user, mailto_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

def TVseries_diff(episodes_arrived):
    reload(sys)
    sys.setdefaultencoding("utf8")

    file_list = csv.reader(file('list.csv', 'rb'))
    for file_line in file_list:
        url = file_line[0]
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        episodes_new = []
        for link in soup.find_all('a'):
            if string.find(link.get_text(), '.mp4') != -1:
                newline = []
                newline.append(link.get_text())
                newline.append(link.get('href'))
                episodes_new.append(newline)

        title_code = string.split(url, '/')[4]
        try:
            file_episodes_old = csv.reader(codecs.open(title_code + '.csv', 'r', 'utf-8'))
        except Exception:
            file_episodes_old = []
        episodes_old = []
        for line in file_episodes_old:
            newline = []
            for col in line:
                cell = unicode(col, 'utf-8')
                newline.append(cell)
            episodes_old.append(newline)

        episodes_diff = []
        if episodes_new != [] and episodes_old != []:
            list_new = []
            for line in episodes_new:
                list_new.append(line[0])
            list_old = []
            for line in episodes_old:
                list_old.append(line[0])
            set_new = set(list_new)
            set_old = set(list_old)
            set_diff = set_new.difference(set_old)
            list_diff = list(set_diff)
            for line in episodes_new:
                matched = []
                for s in list_diff:
                    if line[0] == s:
                        matched = line
                        break
                if matched != []:
                    episodes_diff.append(matched)
        elif episodes_new != [] and episodes_old == []:
            episodes_diff.append(episodes_new)

        if episodes_diff != []:
            writer = csv.writer(codecs.open(title_code + '.csv', 'wb', 'utf-8'))
            writer.writerows(episodes_new)
            episodes_arrived += episodes_diff
            for each in episodes_diff:
                send_mail(file_line[1],each[0])


if __name__ == '__main__':
    while 1 > 0:
        episodes_arrived = []
        TVseries_diff(episodes_arrived)
        sleep(3600)

