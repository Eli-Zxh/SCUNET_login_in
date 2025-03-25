import requests
import re
import logging
import os

urlcode_dict = {
    '中国联通' : '%E8%81%94%E9%80%9A%E5%87%BA%E5%8F%A3',
    '中国电信' : '%E7%94%B5%E4%BF%A1%E5%87%BA%E5%8F%A3',
    '中国移动' : '%E7%A7%BB%E5%8A%A8%E5%87%BA%E5%8F%A3',
    '校园网' : 'internet',
}# 运营商字典

def setup_logging():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(script_dir, 'log')
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    logging.basicConfig(filename=os.path.join(log_dir, 'netconnect.log'), level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def getLoginMsg():
    url = 'http://192.168.2.135'
    r = requests.get(url=url)
    try:
        pattern = r"href='(\S+)'"
        match = re.search(pattern=pattern, string=r.text)
        if match:
            href = match.group(1)
        else:
            logging.info("Already logged in or no login page found.")
            return None
    except Exception as e:
        logging.error(f"Error parsing login page: {e}")
        return None
    destination = href.split('?')[0]  # 跳转目标url
    params = href.split('?')[1]  # params字符串
    return params

def login(userId, password, type):
    url = 'http://192.168.2.135/eportal/InterFace.do?method=login'
    paramstr = getLoginMsg()
    if paramstr is None:
        return
    params = {
        "method": "login"
    }
    data = {
        "userId": userId,
        "password": password,
        "service": urlcode_dict[type],# 服务名，如果是中国联通换成'联通出口'，电信换成'电信出口'，移动换成'移动出口'，使用urlcode编码
        "queryString": paramstr,
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": "",
        "passwordEncrypt": "false"
    }
    r = requests.post(url=url, params=params, data=data)
    if r.json()["result"] == "success":
        logging.info("login success")
    else:
        logging.info("login fail")
        logging.error(r.json()["msg"])

if __name__ == "__main__":
    setup_logging()
    # 检查是否能访问外网
    userId= ''#输入你的学号
    password= ''#输入你的密码
    type= '校园网'#输入你的运营商选择['中国联通','中国移动','中国电信','校园网']
    login(userId=userId,password=password,type=type)
