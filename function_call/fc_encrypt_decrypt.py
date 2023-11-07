#!/usr/bin/env python
#coding:utf-8

"""
@software: ChatGPT Function Call Red Team Tools
@author: magicming200
@site: https://github.com/magicming200
@time: 2023/11/05 22:28
"""

import hashlib
import requests
from config import system_config

str_encrypt_begin = 'The encryption result is '
str_decrypt_begin = 'The decryption result is '
str_end = '.'

def md5_encrypt(plain_string):
    '''
    Md5 algorithm encrypt string.
    :param plain_string:Plain text that needs to be encrypted
    :return:Encrypted string
    '''
    md5 = hashlib.md5()
    md5.update(plain_string.encode('utf-8'))
    hash = md5.hexdigest()
    return_str = str_encrypt_begin + hash + str_end
    return return_str

def sha1_encrypt(plain_string):
    '''
    Sha1 algorithm encrypt string.
    :param plain_string:Plain text that needs to be encrypted
    :return:Encrypted string
    '''
    hash_object = hashlib.sha1()
    hash_object.update(plain_string.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return_str = str_encrypt_begin + hex_dig + str_end
    return return_str

def sha256_encrypt(plain_string):
    '''
    Sha256 algorithm encrypt string.
    :param plain_string:Plain text that needs to be encrypted
    :return:Encrypted string
    '''
    sha256 = hashlib.sha256()
    sha256.update(plain_string.encode('utf-8'))
    hex_dig = sha256.hexdigest()
    return_str = str_encrypt_begin + hex_dig + str_end
    return return_str

def sha512_encrypt(plain_string):
    '''
    Sha512 algorithm encrypted string.
    :param plain_string:Plain text that needs to be encrypted
    :return:Encrypted string
    '''
    hash_object = hashlib.sha512()
    hash_object.update(plain_string.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return_str = str_encrypt_begin + hex_dig + str_end
    return return_str

def hash_decrypt(hash_string):
    '''
    Decrypt hash string, support common hash data types, decryption API details:https://cmd5.com
    :param hash_string:The hash string that needs to be decrypted
    :return:Decrypted string
    '''
    if len(system_config.api_decrypt_url) == 0:
        return 'Error: decryption url is empty'
    elif len(system_config.api_decrypt_email) == 0:
        return 'Error: decryption email is empty'
    elif len(system_config.api_decrypt_key) == 0:
        return 'Error: decryption key is empty'
    url = system_config.api_decrypt_url
    params = {
        'email': system_config.api_decrypt_email,
        'key': system_config.api_decrypt_key,
        'hash': hash_string,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        myres = response.content.decode()
        if myres.strip() == 'CMD5-ERROR:0':
            return_str = myres + ' API Error：Decryption failed'
        elif myres.strip() == 'CMD5-ERROR:-1':
            return_str = myres + ' API Error：Invalid username and password'
        elif myres.strip() == 'CMD5-ERROR:-2':
            return_str = myres + ' API Error：Insufficient balance'
        elif myres.strip() == 'CMD5-ERROR:-3':
            return_str = myres + ' API Error：Decryption server failure'
        elif myres.strip() == 'CMD5-ERROR:-4':
            return_str = myres + ' API Error：Unrecognized ciphertext'
        elif myres.strip() == 'CMD5-ERROR:-7':
            return_str = myres + ' API Error：Unsupported type'
        elif myres.strip() == 'CMD5-ERROR:-8':
            return_str = myres + ' API Error：API permission is prohibited'
        elif myres.strip() == 'CMD5-ERROR:-9':
            return_str = myres + ' API Error：The number of entries exceeds 200'
        elif myres.strip() == 'CMD5-ERROR:-999':
            return_str = myres + ' API Error：Other errors'
        else:
            return_str = str_decrypt_begin + myres + str_end
        return return_str
    except requests.exceptions.HTTPError as err:
        return f'{err}'
    except Exception as err:
        return f'{err}'


if __name__ == "__main__":
    pass
    '''
     cmd5 response packet return format:
     When the decryption is successful, the result is returned directly, and multiple results are separated by TAB.
     In other cases, the string "CMD5-ERROR:" + numeric code is returned. Listed below:
     CMD5-ERROR:0 Decryption failed
     CMD5-ERROR:-1 Invalid username and password
     CMD5-ERROR:-2 Insufficient balance
     CMD5-ERROR:-3 Decryption server failure
     CMD5-ERROR:-4 Unrecognized ciphertext
     CMD5-ERROR:-7 Unsupported type
     CMD5-ERROR:-8 api permission is prohibited
     CMD5-ERROR:-9 The number of entries exceeds 200
     CMD5-ERROR:-999 Other errors
    '''


