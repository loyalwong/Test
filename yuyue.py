# coding=utf-8
from splinter.browser import Browser
from time import sleep

#网址
index_url = "http://yuyue.shdc.org.cn/Main/Default.aspx"
#用户名，密码
username = "15921615178"
password = "87994566"
#医生
doctor = u"姓名：王琛"
hospital = u"医院：曙光西院"

def login():
    while b.is_element_present_by_value(u'登 录'):
        print("in the start of loop of login")
        sleep(5)
        try:
            b.fill('txtUserName',username)
            b.fill('txtPassword',password)
            sleep(10)
            b.find_by_value(u'登 录').click()
            print("click login button")
        except Exception:
            print("can't find login button")
        sleep(5)
        if b.is_element_present_by_value(u'注销退出'):
            print("already logined")
            break

def expert_choose():
    try:
        b.click_link_by_text(u'我的专家')

        element1 = b.find_by_id('ctl00_ContentPlaceHolder1_divdoctorlist')
        element2 = element1.find_by_css('div.content_doctor') + element1.find_by_css('div.content_doctor_even')
        for each2 in element2:
            element3 = each2.find_by_css('div.content_doctor_action')
            element4 = each2.find_by_css('div.content_doctor_detail')
            element5 = element4.find_by_css('div.content_doctor_detail_top')
            element6 = element5.find_by_tag('p')
            for each6 in element6:
                if each6.text == doctor:
                    doctor_flag = TRUE
                if each6.text == hospital:
                    hospital_flag = TRUE
            if doctor_flag == TRUE and hospital_flag == TRUE:
                element7 = element3.find_by_css('div.content_doctor_action_bottom')
                break

        button_appointment = element7.find_by_id('btnOrder0')
        button_appointment.click()

    except Exception:
        print("error occur")

def yuyue():
    global b
    b = Browser(driver_name="chrome")
    b.visit(index_url)
    login()

    expert_choose()

    sleep(10)
    b.quit()

if __name__ == "__main__":
    yuyue()
