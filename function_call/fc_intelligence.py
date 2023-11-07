#!/usr/bin/env python
#coding:utf-8

"""
@software: ChatGPT Function Call Red Team Tools
@author: magicming200
@site: https://github.com/magicming200
@time: 2023/11/05 22:28
"""
import json

import requests
from config import system_config

def search_ip_reputation(ip):
    '''
    Search the reputation of the target ip, api details: https://x.threatbook.com/v5/apiDocs
    :param ip:target ip
    :return:the reputation of the target IP, including IP location, whether it is malicious, threat level, threat data, credibility, etc
    '''

    result = ''
    try:
        url = system_config.api_reputation_url_base + system_config.api_reputation_url_ip_reputation
        query = {
        "apikey": system_config.api_reputation_key,
        "resource": ip,
        "lang": "en"
        }
        response = requests.request("POST", url, params=query)
        rjson = response.json()
        # Read basic IP information
        basic = rjson["data"][ip]["basic"]
        carrier = basic["carrier"]
        asn = rjson["data"][ip]["asn"]
        asn_info = ''
        asn_number = ''
        if asn:
            asn_info = asn["info"]
            asn_number = asn["number"]
        ip_base_info = 'Telecom Operators：' + carrier + ', ASN Name：' + asn_info + ', ASN Number：' + str(asn_number) + ', '
        # Read IP geographical location information
        location = basic["location"]
        country = location["country"]
        province = location["province"]
        city = location["city"]
        lng = location["lng"]
        lat = location["lat"]
        ip_localtion_info = 'Country：' + country + ', Province：' + province + ', City：' + city + ', Longitude：' + lng + ', Dimensions：' + lat + ', '
        # Read IP threat information
        severity = rjson["data"][ip]["severity"]
        jus = rjson["data"][ip]["judgments"]
        judgments = ''
        for ju in jus:
            judgments = judgments + ju + ','
        confidence_level = rjson["data"][ip]["confidence_level"]
        is_malicious = rjson["data"][ip]["is_malicious"]
        if is_malicious :
            is_malicious = 'Yes'
        else:
            is_malicious = 'No'
        ip_threat_info = 'Threat severity level：' + severity + ', Threat type：' + judgments + ', malicious：' + is_malicious + ', Credibility：' + confidence_level
        result = 'The query results of ' + ip + ' are as follows. ' + ip_base_info + ip_localtion_info + ip_threat_info
        return result
    except requests.exceptions.HTTPError as err:
        return f'{err}'
    except KeyError as err:
        return f'{err}'
    except Exception as err:
        return f'{err}'

def search_file_reputation(file_hash):
    '''
    Search the reputation of the target file, api details: https://x.threatbook.com/v5/apiDocs
    :param file_hash:target file's hash, md5 format
    :return:returns the reputation information of the target file, including basic information, threat information, anti-virus software scanning results, etc
    '''
    result = ''
    try:
        url = system_config.api_reputation_url_base + system_config.api_reputation_url_file_reputation
        query = {
        "apikey": system_config.api_reputation_key,
        "md5": file_hash,
        "lang": "en"
        }
        response = requests.request("POST", url, params=query)
        rjson = response.json()
        # Read basic file information
        summary = rjson["data"]["summary"]
        md5 = summary["md5"]
        file_name = summary["file_name"]
        file_type = summary["file_type"]
        file_size = str(summary["file_size"])
        file_base_info = 'file md5:'+ md5 + ', file name:' + file_name + ', file type：' + file_type + ', file size：' + file_size + 'B, '
        # Read file threat information
        malware_type = summary["malware_type"]
        malware_family = summary["malware_family"]
        threat_level = summary["threat_level"]
        threat_score = str(summary["threat_score"])
        sandbox_type = summary["sandbox_type"]
        file_threat_info = 'threat type:'+ malware_type + ', threat family:' + malware_family + ', threat level:' + threat_level + ', threat score:' + threat_score + ', sandbox type:' + sandbox_type + ', '
        # Read anti-virus software scan results
        multi_engines = summary["multi_engines"]
        result_list = rjson["data"]["multiengines"]["result"]
        scan_result = ''
        for key, value in result_list.items():
            if value != 'safe':
                scan_result = scan_result + key + ":" + value + ", "
        if len(scan_result)>1500:
            scan_result = scan_result[:1500]
        file_scan_info = 'Antivirus software detection rate:' + multi_engines + ', detection results (only risky results are displayed)：' + scan_result

        result = file_base_info + file_threat_info + file_scan_info
        return result
    except requests.exceptions.HTTPError as err:
        return f'{err}'
    except KeyError as err:
        return f'{err}'
    except Exception as err:
        return f'{err}'


if __name__ == "__main__":
    # print(search_ip_reputation('159.20.55.7')) # ip clean
    # print(search_ip_reputation('8.210.88.161')) # ip malicious
    # print(search_ip_reputation('146.148.34.125')) # ip malicious
    # print(search_file_reputation('c500cdc7ba1c9a3e26a5eab265ad48e1'))
    # print(search_file_reputation('87b010bc90cd7dd776fb42ea5b3f85d3'))
    pass