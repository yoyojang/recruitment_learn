from .base import *
# 把base导入进来，然后再用以下参数覆盖

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = "w$46bks+b3-7f(13#i%v@jwejrnxc$^^#@#@^t@fofizy1^mo9r8(-939243423300"

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
LDAP_AUTH_URL = "ldap://xxxxx:389"
LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "your_admin_credentials"

INSTALLED_APPS += (
    # other apps for production site
)


## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=3e28a8bbd2ee664ca3e2083dcdbf5ac36a4593fdb9d0a9fda21be74dc90b541b"
QYWX_WEB_HOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=edf47793-2156-4c21-9634-a58d67948916"