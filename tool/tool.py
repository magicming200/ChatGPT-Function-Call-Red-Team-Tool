#!/usr/bin/env python
#coding:utf-8

"""
@software: ChatGPT Function Call Red Team Tools
@author: magicming200
@site: https://github.com/magicming200
@time: 2023/11/05 22:28
"""

import base64
import re
from datetime import datetime

def get_base64(content):
    '''
    Convert content to base64 encoding.
    :param content:text content that needs to be encode
    :return:base64 encoded string
    '''
    return base64.b64encode(content.encode('utf-8')).decode('utf-8')


def is_ip_format(ip):
    '''
    Whether it is an ip format.
    :param ip:target ip
    :return:if it is an ip, return true; if not, return false
    '''
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return True
    else:
        return False

def is_ip_segment_format(ip_range):
    '''
    Whether it is an ip segment format
    :param ip_range:taeget ip_range, for example:8.8.8.8/24
    :return:if it is an ip segment, return true; if not, return false
    '''
    ip_range_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$'
    if re.match(ip_range_pattern, ip_range):
        return True
    else:
        return False


def is_level_1_domain(domain):
    '''
    Whether it is level 1 domain format.
    :param domain: target level 1 domain
    :return:if it is level 1 domain format, return true; if not, return false
    '''
    domain_pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(domain_pattern, domain):
        return True
    else:
        return False


def is_level_n_domain(domain):
    '''
    Whether it is level n domain format.
    :param domain: target level n domain
    :return:if it is domain format, return true; if not, return false
    '''
    pattern = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)
    return True if pattern.match(domain) else False


def get_current_time_microsecond():
    '''
    Get the current date and time, accurate to microseconds.
    :return:string of current date and time
    '''
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d%H%M%S%f")
    return formatted_time


def print_gray(content):
    '''
    Print gray content.
    :param content:what needs to be printed
    :return:no return value
    '''
    print('\033[90m' + content + '\033[0m')


if __name__ == "__main__":
    # print(is_ip_segment_format('8.8.8.1/8'))
    # print(is_level_1_domain('b.qq.com'))
    # print(is_level_n_domain('h.news.qq.com'))
    pass