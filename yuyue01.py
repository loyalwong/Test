# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "http://yuyue.shdc.org.cn/"

driver.get(base_url)
driver.find_element_by_link_text(u"登录").click()
driver.find_element_by_css_selector("#loginbox > div.title").click()
driver.find_element_by_id("loginuserName").click()
driver.find_element_by_id("loginuserName").clear()
driver.find_element_by_id("loginuserName").send_keys("15921615178")
driver.find_element_by_id("loginuserPassword").click()
driver.find_element_by_id("loginuserPassword").clear()
driver.find_element_by_id("loginuserPassword").send_keys("87994566")
driver.find_element_by_id("logincertCode").click()
driver.find_element_by_id("logincertCode").clear()
driver.find_element_by_id("logincertCode").send_keys("712129")
driver.find_element_by_xpath(u"//input[@value='登录']").click()
driver.find_element_by_link_text(u"个人中心").click()
elem1 = driver.find_element_by_xpath(u"(//a[contains(text(),'医生关注')])[2]")
elem1.click()
driver.find_element_by_xpath(u"(//a[contains(text(),'预约')])[7]").click()
driver.find_element_by_css_selector("#div1680137 > div[name=\"zhousp\"]").click()
driver.find_element_by_id("tijiaoImage").click()
driver.find_element_by_id("certCode").clear()
driver.find_element_by_id("certCode").send_keys("07")
driver.find_element_by_id("userPhoneVerifyCode").clear()
driver.find_element_by_id("userPhoneVerifyCode").send_keys("0322")
driver.find_element_by_id("tijiaoImage").click()
