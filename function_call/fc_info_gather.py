#!/usr/bin/env python
#coding:utf-8

"""
@software: ChatGPT Function Call Red Team Tools
@author: magicming200
@site: https://github.com/magicming200
@time: 2023/11/05 22:28
"""

import requests
from tool import tool
from config import system_config

def search_open_ports(host):
    '''
    Search for open ports on the target host, api details: https://fofa.info/api
    :param host:ip or ip segment or level 1 domain name
    :return:ports opened by the target host
    '''
    if len(system_config.api_ports_url) == 0:
        return 'Error: api url is empty'
    elif len(system_config.api_ports_email) == 0:
        return 'Error: decryption email is empty'
    elif len(system_config.api_ports_key) == 0:
        return 'Error: decryption key is empty'
    target_format = 0
    url = system_config.api_ports_url
    # Determine whether the parameter is in IP or domain name format
    if tool.is_ip_format(host): #ip format
        target_format = 1
        query = 'ip="' + host + '"'
    elif tool.is_ip_segment_format(host): #ip segment format
        target_format = 2
        query = 'ip="' + host + '"'
    elif tool.is_level_n_domain(host):
        target_format = 3
        query = 'host="' + host +'"'
    else:
        #return mytarget
        return host+'The target format is incorrect. IP、IP segment and domain formats are supported, for example: 8.8.8.8、 8.8.8.8/24、 qq.com'
    params = {
        'email': system_config.api_ports_email,
        'key': system_config.api_ports_key,
        'qbase64': tool.get_base64(query),
        'fields': system_config.api_ports_fields,
        'page': system_config.api_ports_page,
        'size': system_config.api_ports_size,
    }
    try:
        result = ''
        response = requests.get(url, params=params)
        response.raise_for_status()
        jres = response.json()
        if jres.get('error') == False:
            if jres.get('results'):
                myresult = jres.get('results')
                if len(myresult) > 0 :
                    myset = set()
                    for yuansu in myresult:
                        host = yuansu[0]
                        ip = yuansu[1]
                        port = yuansu[2]
                        if target_format == 1:
                            myset.add(port)
                        elif target_format == 2:
                            myset.add(ip + ':' + port + ' ')
                        elif target_format == 3:
                            host = host.replace("https://", "")
                            index_of_colon = host.find(':')
                            if index_of_colon != -1:
                                host = host[:index_of_colon]
                            if host.endswith(host):
                                myset.add(host + ':' + port)
                    topn = 40
                    if target_format == 1:
                        result = host + ' open ports: '
                        for index, value in enumerate(myset):
                            if index < topn:
                                result = result + value + ' '
                            else:
                                break
                    else:
                        result = ''
                        for index, value in enumerate(myset):
                            if index < topn:
                                result = result + value + '  '
                            else:
                                break
                else:
                    result = 'No open port found.'
                return result
            else:
                return 'No open port found.'
        else:
            return 'API request failed, the request rate needs to be < 2/S, please try again later.'
    except requests.exceptions.HTTPError as err:
        return f'{err}'
    except Exception as err:
        return f'{err}'

def search_subdomains(domain):
    '''
    Search subdomains of the target domain, api details: https://hackertarget.com/
    :param domain:level 1 domain name
    :return:list of subdomains
    '''
    subdomain_result = ''
    url = system_config.api_subdomain_url
    if tool.is_level_1_domain(domain):
        query = domain
    else:
        return 'The domain format is incorrect, please enter the first-level domain name.'
    params = {
        'q': query
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        lines = response.content.decode('utf-8').split('\n')
        domain_list = [line.split(',')[0] for line in lines]
        subdomain_topn_result = '  '.join(domain_list[:50]) # top 50 subdomains
        return subdomain_topn_result
    except requests.exceptions.HTTPError as err:
        return f'{err}'
    except Exception as err:
        return f'{err}'

def search_dns(domain):
    '''
    Search DNS records for the target domain, api details: https://hackertarget.com/
    :param domain:level 1 domain name
    :return:DNS records
    '''
    result = ''
    if tool.is_level_n_domain(domain):
        query = domain
    else:
        return 'Domain format is incorrect.'
    params = {
        'q': query
    }
    try:
        response = requests.get(system_config.api_dns_url, params=params)
        response.raise_for_status()
        result = response.content.decode('utf-8')
        result = result.replace("\n", "  ")
        if len(result) > system_config.function_return_max_len:
            result = result[:system_config.function_return_max_len]
        return result
    except requests.exceptions.HTTPError as err:
        return f'{err}'
    except Exception as err:
        return f'{err}'


if __name__ == "__main__":
    # print(search_open_ports('8.8.8.8'))
    # print(search_open_ports('8.8.8.8/16'))
    # print(search_open_ports('x.com'))
    # print(search_subdomains('x.com'))
    # print(search_dns('google.com'))
    pass
