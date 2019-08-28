# 一个用Tornado编写API的模板

## 版本概览

| 版本号 | 项目进度 |
|-- |-- |
| v1.0 | Tornado 编写 API |
| v1.1 | 新增Tornado API部署 |
| v1.2 | 解决服务端跨域问题 |
| v1.3 | 使用Swagger-UI展示API文档 |

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
在虚拟机的浏览器上访问 127.0.0.1:9001，输入账号密码，即可查看进程管理界面

重启nginx：
```
root@ubuntu:~# /etc/init.d/nginx restart
```
或者：
```
root@ubuntu:~# systemctl restart nginx.service
```
即可对 192.168.1.89:8088/v1/spider/hotsearch/weibo 进行POST请求

## v1.3：使用Swagger-UI展示API文档

使用swagger-UI展示API文档：

使用swagger-py-codegen生成Python web framework 代码：
```
(env_py2.7) root@ubuntu:/spiders/tornado_exmple# pip install swagger-py-codegen
```
在 http://editor.swagger.io/ 在线编辑API文档，导出为.yaml文件，修改后缀并命名为为api.yml，
将api.yml放在/spiders/tornado_exmple/下，然后生成demo代码文件：
```
(env_py2.7) root@ubuntu:/spiders/tornado_exmple# swagger_py_codegen -s api.yml example-app -p demo -tlp=tornado --ui --spec
```
将/spiders/tornado_exmple/example-app/demo/下的static文件夹拷贝到/spiders/tornado_api下，在nginx中加入静态文件访问（带认证）：
在/etc/nginx/sites-enabled/下的tornado_nginx.conf的server中加入：
```
	location /static {
		alias /spiders/tornado_api/static;
		auth_basic            "Restricted";
		auth_basic_user_file  /etc/nginx/conf.d/.htpasswd;
	}
```
这里使用了之前在nginx用htpasswd创建的用户认证

重启nginx：
```
root@ubuntu:~# /etc/init.d/nginx restart
```
浏览器打开 http://192.168.1.89:8088/static/swagger-ui/index.html ，输入账号密码即可查看swagger-UI展示的API文档

API文档保存在/spiders/tornado_api/static/v1下，可用json格式编写