# coding=utf-8
from splinter.browser import Browser
from time import sleep

#网址
index_url = "http://yuyue.shdc.org.cn/Main/Default.aspx"
#用户名，密码
username = "15921615178"
password = "87994566"
#医生
doctor = "王琛"

def login():
    while b.is_element_present_by_value(u'登 录'):
        print("in the start of loop of login")
        sleep(5)
        b.fill('txtUserName',username)
        b.fill('txtPassword',password)
        sleep(10)
        try:
            b.find_by_value(u'登 录').click()
            print("click login button")
        except Exception:
            print("can't find login button")
        sleep(5)
        if b.is_element_present_by_value(u'注销退出'):
            print("already logined")
            break


def yuyue():
    global b
    b = Browser(driver_name="chrome")
    b.visit(index_url)
    login()

    try:
        print("inside try")
        b.click_link_by_text(u'我的专家')

        element1 = b.find_by_id('ctl00_ContentPlaceHolder1_divdoctorlist')
        for each1 in element1:
            element2 = each1.find_by_css('div.content_doctor')
            for each2 in element2:
                element3= each2.find_by_css('div.content_doctor_detail_top')
                for each3 in element3:
                    try:
                        element4 = each3.find_by_text(doctor)
                        print("find specified doctor")
                        print(element4.value)
                        print(each3.value)
                        print(each2.value)
                        print(each1.value)
                        break
                    except Exception:
                        print("can't find specified doctor")



    except Exception:
        print("error occur")

#    w = b.windows[0]
#    print(w.title)
#    w.close()

if __name__ == "__main__":
    yuyue()
