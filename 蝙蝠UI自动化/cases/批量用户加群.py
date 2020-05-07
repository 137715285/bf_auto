from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from openpyxl import load_workbook
import time

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '8', # 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.woyue.batchat', # 启动APP Package名称
  'appActivity': '.act.SplashActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 账号登录
driver.find_element_by_id("btnLogin").click()
# 点击使用 batid登录
driver.find_element_by_id("tvLoginById1").click()

# # 定位账号输入框
# mm = driver.find_elements_by_id("et")
# print(mm)

def th_dly():
    # 在首页，退出到登录页面
    wd = driver.find_element_by_android_uiautomator(
        'new UiSelector().text("我的")'
    )
    wd.click()
    # 点击个人设置
    w = driver.find_element_by_id("tvBatId")
    w.click()
    # 点击退出登录
    w = driver.find_element_by_id("btnExit")
    w.click()
    # 点击确定
    w = driver.find_element_by_id("confirm")
    w.click()


def login_sy():
    # 点击 登录 按钮
    w = driver.find_element_by_id("btnLogin")
    w.click()
    # 点击 使用bat id登录
    w = driver.find_element_by_id("tvLoginById1")
    w.click()


# 读取excel
book = load_workbook(rf"C:\\Users\\13771\\Desktop\\蝙蝠UI自动化\\cases\\jhy.xlsm")
sheet = book.active
vals = []
for cell in sheet['A']:
    vals.append(cell.value)



 # 循环登录读取的账号
for val in vals[20:190]:
    # 定位 账号输入框，并输入账号
    zh = driver.find_element_by_android_uiautomator(
        'new UiSelector().text("请输入Bat ID")'
    )
    zh.send_keys(val)
    doc = open('out.txt', 'w')
    print(val)
    print(val, file=doc)
    # 定位 密码输入框，并输入密码
    ele = driver.find_element_by_xpath(rf'//android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.EditText')
    ele.send_keys('1234567q')
    # 点击登录按钮
    dl = driver.find_element_by_id("btnLogin")
    dl.click()

    # 点击右上角+号
    jia = driver.find_element_by_id("imgRight")
    jia.click()
    # 点击加好友/群
    rlist = driver.find_elements_by_id("title")
    rlist[1].click()
    # 点击输入框
    sr = driver.find_element_by_id("tvSearch")
    sr.click()
    # 跳转页面定位输入框输入群号
    sr = driver.find_element_by_id("inputView")
    sr.send_keys('395360')
    # 点击找群
    q = driver.find_element_by_id("tvGroupHint")
    q.click()
    # 点击搜索结果群
    q = driver.find_element_by_id("tvNum")
    q.click()

    #yl = driver.find_element_by_id("tvSendMessage").is_displayed()
    try:
        driver.find_element_by_id("tvSendMessage").click()
        driver.keyevent(4)
        time.sleep(1)
        th_dly()
        login_sy()

    except :

        # 点击申请加群
        q = driver.find_element_by_id("tvApplyGroup")
        q.click()
        time.sleep(1)

        # 返回首页
        driver.keyevent(4)
        time.sleep(1)
        th_dly()
        login_sy()

pass