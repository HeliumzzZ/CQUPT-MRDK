# 使用教程

## 抓包

使用此脚本需要抓微信的`openid`，这里以苹果Stream抓包工具为例，教程如下：

- 打开Stream，点击开始抓包
- 点开微信进入we重邮小程序
- 点击下方的资讯后退出微信
- 打开Stream，点击停止抓包，查看抓包历史找到`url`里带`news`这个字段的请求，即可获取`openid`

## Server酱

可以查看打卡结果，并推送到微信。

server酱链接为：https://sct.ftqq.com/forward

拿到这个apikey

![image](https://user-images.githubusercontent.com/96455578/170548761-844a3d7b-511c-4151-b74c-ac89ba9b236f.png)


## 脚本部署

这里使用的是Github Action

- 将此项目fork到自己的仓库

- 点击`setting`设置密钥，填写对应字段，`SERVER`为SERVER酱apikey，`XH`为学号，`OPENID`为上面抓包抓到的`openid`

  ![image](https://user-images.githubusercontent.com/96455578/170548824-0779c826-374c-487a-8f92-7970c7d8cb07.png)

  ![image](https://user-images.githubusercontent.com/96455578/170548857-9b953970-2511-49a3-a49c-d4d4c7a6b750.png)

- 修改`自动打卡.py`中的姓名，性别，地址，详细地址字段

  ![image](https://user-images.githubusercontent.com/96455578/170548901-52f09aa8-70c6-42d5-ad99-123f51a97be3.png)

**到这里所有的配置就已经完成了**

# 声明

该脚本只是本人闲来无事开发玩的，疫情期间注意安全，该打卡打卡，使用此脚本造成的任何后果与本人无关，我都要寄了！！！！

链接：https://github.com/HeliumzzZ/CQUPT-MRDK


