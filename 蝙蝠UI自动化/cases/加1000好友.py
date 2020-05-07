from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from openpyxl import load_workbook
import time

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '6', # 手机安卓版本
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

# 如果有`提示更新`界面，点击`×`
#iknow = driver.find_element_by_id("ivClose")
#if iknow:
#    iknow.click()

# 账号登录
# driver.find_element_by_id("btnLogin").click()
# # 点击使用 batid登录
# driver.find_element_by_id("tvLoginById1").click()
# # 输入账号密码
# mm = driver.find_elements_by_id("et")
# mm[0].send_keys('170720')
# mm[1].send_keys('1234567t')
time.sleep(2)
# 点击右上角+号
driver.find_element_by_id("imgRight").click()
# 点击加好友/群
rlist = driver.find_elements_by_id("title")
rlist[1].click()
# 点击输入框
driver.find_element_by_id("tvSearch").click()
# 跳转页面再点击输入框
sbox = driver.find_element_by_id("inputView")

# 读取excel
book = load_workbook(rf"C:\\Users\\Administrator\\Desktop\\jhy.xlsm")
sheet = book.active

vals = []
for cell in sheet['A']:
    vals.append(cell.value)

# 循环读取列表昵称
for val in vals[1:1001]:
  print(val)
  sbox.send_keys(val)
  time.sleep(1)
  # 点击找人
  driver.find_element_by_id("tvUserHint").click()

  # 点击搜索结果联系人
  driver.find_element_by_id("tvNickName").click()
  # 点击加好友
  driver.find_element_by_id("addFriend").click()
  # 点击发送
  driver.find_element_by_id("btnSend").click()
  # 点击×号
  # driver.find_element_by_id("btnClean").click()
  time.sleep(1)
  driver.keyevent(4)
  time.sleep(.5)
  driver.keyevent(4)
  time.sleep(2)
  # 点击输入框
  w = driver.find_element_by_id("tvSearch")
  w.click()
  time.sleep(1)

  # 跳转页面再点击输入框
  sbox = driver.find_element_by_id("inputView")
pass

