# 一个用Tornado编写API的模板

安装依赖：
```
(env_py2.7) root@ubuntu:/spiders/tornado_api# pip install -r requirements.pip
```
启动项目：
```
(env_py2.7) root@ubuntu:/spiders/tornado_api# python server.py
```
如果遇到报错：
```
  File "/spiders/tornado_api/handlers/spider_hotsearch.py", line 6, in <module>
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
ImportError: cannot import name InsecureRequestWarning
```
更新requests库即可：
```
(env_py2.7) root@ubuntu:/spiders/tornado_api# pip install -U requests
```

请求示例：
```
POST : 127.0.0.1:8888/v1/spider/hotsearch/weibo

{
"keyword":"hotsearch",
"platform":"weibo",
"date":"2019/08/23",
"version":"1.0",
"token":"a05355f9cbc40e1da03deaa04f76f4a9"
}
```