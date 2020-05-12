import random
import time

import requests

from logger import logger

token = ""

log = logger.get_logger(__name__)


def logon():
    auth = {"method": "do", "login": {"password": "xxx"}}
    r = requests.post('http://tplogin.cn/', json=auth)
    if r and r.ok:
        log.info("log on successfully")
        resp = r.json()
        global token
        token = resp['stok']


# http://tplogin.cn/stok=token/ds
def get_hosts():
    req_online = {"hosts_info": {"table": "online_host"}, "method": "get"}
    global token
    resp = requests.post(f'http://tplogin.cn/stok={token}/ds', json=req_online)
    if resp.status_code == 200:
        data = resp.json()
        if data['hosts_info']:
            return data['hosts_info']['online_host']
    else:
        log.error(f'failed to get online hosts info, error: {resp}')


def create_request(host_info):
    for _, v in host_info.items():
        mac, hostname, up_speed, down_speed, up_limit, down_limit = v['mac'], v['hostname'], int(v['up_speed']), int(
            v['down_speed']), int(v['up_limit']), int(v['down_limit'])
        host_desc = 'mac: {mac}, ip: {ip}, hostanme: {hostname}, up_speed: {up_speed}, down_speed:{down_speed}, ' \
                    'up_limit:{up_limit}, down_limit: {down_limit}, is_cur_host: {is_cur_host}'.format(**v)
        req, action = None, None
        # do some thing
        return req, action


def handle_request(req, desc=None):
    log.info(f'request desc: {desc}, detail:{req}')
    if req:
        global token
        resp = requests.post(f'http://tplogin.cn/stok={token}/ds', json=req)
        if resp.status_code == 200:
            log.info(f'request handle successfully, {resp.text}')
        else:
            log.error(f'request failed, response: {resp}')


if __name__ == '__main__':
    logon()
    while True:
        time.sleep(random.randint(0, 10))
        hosts = get_hosts()
        if hosts:
            for host in hosts:
                # *tuple expand tuple as function parameters
                handle_request(*create_request(host))
