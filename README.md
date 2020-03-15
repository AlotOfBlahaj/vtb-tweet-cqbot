vtb-tweet-cqbot
=======

简单易用的转推机器人

功能
---
- 监控目标推特，并将内容转发至QQ群

- 支持多用户，多机器人账号

使用
------
1.Clone 本项目

2.安装依赖库

    pip install -r requirements.txt
    
3.配置config

- 将config_example.json更名为config.json

- 配置范例如下

```json5

{
  "EnableProxy": false, // 是否启用代理
  "Proxy": "127.0.0.1:10800", // HTTP代理服务器
  "CheckSec": 30,  // 监测间隔
  "Twitter_API_KEY": "", // Twitter API密钥
  "Target": [
    {
      "Twitter_UserID": 1200357161747939328, // 目标Twitter用户ID
      "GroupID": [
        123456789  // 转推目标群号
      ],
      "CqHost": "",  // CqHttpApi插件所配置的Host
      "CqToken": ""  // CqHttpApi插件所配置的Token
    },
    {
      "Twitter_UserID": 998336069992001537,
      "GroupID": [
        987654321
      ],
      "CqHost": "",
      "CqToken": ""
    }
  ]
}
```
4.启动程序

    python main.py
    
支持
------------
如有建议或意见，欢迎发送issue或邮件至fzxiao@dd.center
