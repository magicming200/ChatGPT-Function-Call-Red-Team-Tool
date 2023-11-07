#!/usr/bin/env python
#coding:utf-8

"""
@software: ChatGPT Function Call Red Team Tools
@author: magicming200
@site: https://github.com/magicming200
@time: 2023/11/05 22:28
"""

import os
from tool import tool

def save_text_file(content):
    '''
    Save content as txt file.
    :param content:text content that needs to be saved as a file
    :return:the saving result prompts, if the saving is successful, the file path will be output
    '''
    function_return = ''
    try:
        file_name = f"{tool.get_current_time_microsecond()}.txt"
        file_dir = 'output'
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_path = os.path.join(file_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        function_return = 'File saved successfully, file path:' + file_path
        return function_return
    except IOError as e:
        return f'{e}'
    except Exception as e:
        return f'{e}'


if __name__ == "__main__":
    # content = 'Hello, this i\ns  content to b\ne saved in th\ne txt file.'
    # print(save_text_file('admin',content))
    pass






