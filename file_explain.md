# 文件说明

- /handlers：接口主程序文件夹
- /conf：配置文件夹
	- tornado_nginx.conf：nginx配置文件
	- tornado_super.conf：supervisor配置文件
- /static：静态文件目录
	- swagger-ui：swagger-ui页面文件
	- v1：swagger-ui配置
- /tmp_logs：日志文件夹
- /：项目根目录
	- consts.py：选择常数
	- utils.py：公用程序
	- routes.py：路由映射
	- server.py：服务启动
	- log_dir.txt：日志位置说明
	- requirements.txt：python依赖包
	- user_agents.list：user_agent列表