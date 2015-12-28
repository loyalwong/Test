# coding=utf-8

from splinter import Browser
import time

b= Browser(driver_name="chrome")
b.visit("http://yuyue.shdc.org.cn/Main/Default.aspx")
b.fill("txtUserName","15921615178")
b.fill("txtPassword","87994566")
time.sleep(10)
button = b.find_by_value(u"登录")
button.click()
#b.is_text_present("splinter.readthedocs.org")
#b.quit()
