# encoding: utf-8

import hashlib
import random


# POST请求参数加密
def param_md5(str_encode):
    param = hashlib.md5()
    param.update(str_encode.encode('utf-8'))
    return param.hexdigest()


# 随机获取列表中一个user_agent
def get_agent():
    agents = open('./user_agents.list').readlines()
    agent = random.choice(agents)
    agent = agent.replace('\n', '').replace('\r', '')  # 去除行尾换行符
    return agent

USER_AGENT = get_agent()

