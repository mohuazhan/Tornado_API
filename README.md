# 一个用Tornado编写API的模板


## v1.0：项目程序运行

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

## v1.1：Tornado部署

/spiders/tornado_api/conf/下分别是nginx和supervisord的配置文件，
其中，tornado_nginx.conf须放在/etc/nginx/sites-enabled/下，tornado_super.conf则作为supervisord的启动文件
运行supervisor服务，查看supervisor的状态：
```
root@ubuntu:~# /spiders/env_py2.7/bin/supervisord -c /spiders/tornado_api/conf/tornado_super.conf
root@ubuntu:~# /spiders/env_py2.7/bin/supervisorctl -c /spiders/tornado_api/conf/tornado_super.conf status
```
在虚拟机的浏览器上访问http://127.0.0.1:9001/，输入账号：xiaomo，密码：19940809，即可查看进程管理界面

重启nginx：
```
root@ubuntu:~# /etc/init.d/nginx restart
```
或者：
```
root@ubuntu:~# systemctl restart nginx.service
```
即可对 192.168.1.89:8088/v1/spider/hotsearch/weibo 进行POST请求
