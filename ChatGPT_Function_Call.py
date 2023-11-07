#!/usr/bin/env python
#coding:utf-8

"""
@software: ChatGPT Function Call Red Team Tools
@author: magicming200
@site: https://github.com/magicming200
@time: 2023/11/05 22:28
"""

import json
import os
from function_call import fc_encrypt_decrypt, fc_info_gather, fc_save_file, \
    fc_intelligence, fc_exploit_vulnerability
from config import system_config
import openai
from tool.tool import print_gray

messages = []
user_question = ''
ai_answer = ''
functions_info = []

def read_functions_info():
    '''
    Read function description information, the result save to functions_data variable.
    :return:no return value
    '''
    global functions_info
    functions_info_path = os.path.join('config', 'functions_info.json')
    functions_tmp_datas = {}
    if os.path.exists(functions_info_path):
        with open(functions_info_path, 'r', encoding='utf-8') as file:
            json_data = file.read()
        file.close()
        functions_tmp_datas = json.loads(json_data)
    for tmp_data in functions_tmp_datas:
        functions_info.append(tmp_data)


def prepare():
    '''
    Get the question entered by the user and check whether the conversation tokens exceed the maximum value.
    :return:no return value
    '''
    global messages
    global user_question
    user_question = input('\033[92m' + "Me:" + '\033[0m')
    if user_question.lower() == 'quit' or user_question.lower() == 'exit':
        return False
    messages.append({"role": "user", "content": user_question})
    tokens_used = sum([len(m['content']) for m in messages])
    if tokens_used > system_config.api_chatgpt_max_tokens:
        messages = []
        messages.append({"role": "user", "content": user_question})
        print("Token reached maximum limit, conversation cleared.")
    return True


def function_call(function_json):
    '''
    Parse function json, call the correct function, and return the function result.
    :param function_json:function call json information returned by chatgpt
    :return:the target function return value
    '''
    fun_return = ''
    function_name = function_json["name"]
    my_data = json.loads(json.dumps(function_json))
    arguments = json.loads(my_data['arguments'])
    if function_name == "hash_decrypt":
        fun_return = fc_encrypt_decrypt.hash_decrypt(arguments['hash_string'])
    elif function_name == "md5_encrypt":
        fun_return = fc_encrypt_decrypt.md5_encrypt(arguments['plain_string'])
    elif function_name == "sha1_encrypt":
        fun_return = fc_encrypt_decrypt.sha1_encrypt(arguments['plain_string'])
    elif function_name == "sha256_encrypt":
        fun_return = fc_encrypt_decrypt.sha256_encrypt(arguments['plain_string'])
    elif function_name == "sha512_encrypt":
        fun_return = fc_encrypt_decrypt.sha512_encrypt(arguments['plain_string'])
    elif function_name == "search_open_ports":
        fun_return = fc_info_gather.search_open_ports(arguments['host'])
    elif function_name == "search_subdomains":
        fun_return = fc_info_gather.search_subdomains(arguments['domain'])
    elif function_name == "search_dns":
        fun_return = fc_info_gather.search_dns(arguments['domain'])
    elif function_name == "save_text_file":
        fun_return = fc_save_file.save_text_file(arguments['content'])
    elif function_name == "search_ip_reputation":
        fun_return = fc_intelligence.search_ip_reputation(arguments['ip'])
    elif function_name == "search_file_reputation":
        fun_return = fc_intelligence.search_file_reputation(arguments['file_hash'])
    elif function_name == "exploit_vulnerability_CVE_2022_22965":
        fun_return = fc_exploit_vulnerability.exploit_vulnerability_CVE_2022_22965(arguments['url'])
    return fun_return


if __name__ == "__main__":
    read_functions_info()
    while True:
        prepare_ok = prepare()
        if not prepare_ok:
            break
        try:
            openai.api_key = system_config.api_chatgpt_key
            # Make a request to chatgpt
            response = openai.ChatCompletion.create(
                model = system_config.api_chatgpt_model,
                messages = messages,
                temperature = system_config.api_chatgpt_temperature,
                max_tokens = system_config.api_chatgpt_max_token,
                functions = functions_info,
                function_call="auto",
            )
            message = response["choices"][0]["message"]
            # when return function call
            if message.get("function_call"):
                function_call_name = message["function_call"]["name"]
                print_gray('AI call function ' + function_call_name + '...')
                ai_answer = function_call(message.get("function_call"))
            # when not return function call
            else:
                ai_answer = response.choices[0].message['content']
            print('\033[91m' + "AI:", ai_answer + '\033[0m')
            messages.append({"role": "assistant", "content": ai_answer})
        except openai.error.RateLimitError as err:
            print (f'{err}')
        except openai.error.OpenAIError as err:
            print(f'{err}')
        except Exception as err:
            print(f'{err}')