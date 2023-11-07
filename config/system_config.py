#!/usr/bin/env python
#coding:utf-8

"""
@software: ChatGPT Function Call Red Team Tools
@author: magicming200
@site: https://github.com/magicming200
@time: 2023/11/05 22:28
"""

# ChatGPT api config
api_chatgpt_key = ''
api_chatgpt_model = "gpt-3.5-turbo-16k"
api_chatgpt_temperature = 0.2
api_chatgpt_max_token = 2000 # the maximum token value for a single question
api_chatgpt_max_tokens = 8000 # the maximum token value of all questions and answers

# Encryption and decryption api config
api_decrypt_url = 'http://www.cmd5.com/api.ashx'
api_decrypt_email = ''
api_decrypt_key = ''

# Open ports query api config
api_ports_url = 'https://fofa.info/api/v1/search/all'
api_ports_email = ''
api_ports_key = ''
api_ports_fields = 'host,ip,port'
api_ports_page = 1
api_ports_size = 200

# Subdomains query api config
api_subdomain_url = 'https://api.hackertarget.com/hostsearch/'

# DNS query api config
api_dns_url = 'https://api.hackertarget.com/dnslookup/'

# IP and file reputation query api config
api_reputation_url_base = 'https://api.threatbook.cn/v3/'
api_reputation_url_ip_reputation = 'scene/ip_reputation'
api_reputation_url_file_reputation = 'file/report'
api_reputation_key = ''

# The maximum length returned by the function, to prevent the message sent to openai from being too long
function_return_max_len = 2000


