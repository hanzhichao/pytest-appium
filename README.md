# pytest-data-file

Pytest操作Appium

---

### 如何使用

1. 安装 `pytest-appium`

使用pip从github安装
```
pip install git+https://github.com/hanzhichao/pytest-appium
```

2. 使用方法
新建文件device.json，格式如下：
```json
{
  "caps": {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.lqr.wechat",
    "appActivity": "com.lqr.wechat.ui.activity.SplashActivity",
    "unicodeKeyboard": true,
    "resetKeyboard": true,
    "autoLaunch": false
  },
  "server": "http://localhost:4723/wd/hub"
}
```

> 注意autoLaunch需要设置为false

使用fixture函数: appium
```python
def test_a(appium):
    appium.find_element_by_id('com.lqr.wechat:id/etPhone').send_keys('abc')
    appium.find_element_by_id('com.lqr.wechat:id/etPwd').send_keys('123456')
    appium.find_element_by_id('com.lqr.wechat:id/btnLogin').click()
```
使用pytest --variables=device.json运行
```

---

- Email: <a href="mailto:superhin@126.com?Subject=Pytest%20Email" target="_blank">`superhin@126.com`</a> 
- Blog: <a href="https://www.cnblogs.com/superhin/" target="_blank">`博客园 韩志超`</a>
- 简书: <a href="https://www.jianshu.com/u/0115903ded22" target="_blank">`简书 韩志超`</a>

