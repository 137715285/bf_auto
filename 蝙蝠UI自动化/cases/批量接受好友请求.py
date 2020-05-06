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
# 定位账号输入框
mm = driver.find_elements_by_id("et")

# 读取excel
book = load_workbook(r'C:\\Users\\13771\\Desktop\\jhy.xlsx')
sheet = book.active
vals = []
for cell in sheet['A']:
    vals.append(cell.value)

 # 循环登录读取的账号
for val in vals[1:3]:

    mm[0].send_keys(val)
    mm[1].send_keys('1234567x')
    driver.find_element_by_id("btnLogin").click()
    # 点击联系人
    wd = driver.find_element_by_android_uiautomator(
        'new UiSelector().text("联系人")'
    )
    wd.click()
    # 点新朋友
    xpy = driver.find_element_by_android_uiautomator(
        'new UiSelector().text("新朋友")'
    )
    xpy.click()
    # 点接受
    driver.find_element_by_id("tvAccept").click()

    # 返回首页
    driver.keyevent(4)
    # 点击我的
    wd = driver.find_element_by_android_uiautomator(
        'new UiSelector().text("我的")'
    )
    wd.click()
    # 点击个人设置
    driver.find_element_by_id("tvBatId").click()
    # 点击退出登录
    driver.find_element_by_id("btnExit").click()
    # 点击确定
    driver.find_element_by_id("confirm").click()

    # 账号登录
    driver.find_element_by_id("btnLogin").click()
    # 点击使用 batid登录
    driver.find_element_by_id("tvLoginById1").click()

pass