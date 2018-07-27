# -*- coding=utf-8 -*-
#生成字典文件

import itertools

'''
#检验结束
def check_end(pwd, end_char):
    only=[]
    for i in pwd:
        if i not in only:
            only.append(i)
    if len(only) == 1 and only == end_char:
        return True
    else:
        return False
'''

#提取包含字符，去重
def cancel_repeat(origin):
    origin_list=list(origin)
    _char=[]
    for i in origin_list:
        if i not in _char:
            _char.append(i)
    char=''.join(_char)
    return char

#确定字符串长度
def get_length():
    while 1:
        try:
            length=int(input('请输入要求密码长度：'))
        except:
            print('输入不正确，请继续输入')
            continue
        break
    return length

'''
#生成字典
while 1:
    _pwd=[]
    for i in char:
        _pwd.append(i)  #生成阶段卡住了，后来发现存在 itertools 模块
        #控制长度
        if len(_pwd) >= length:
            break
    pwd=''.join(_pwd)
    with open('dictionary.txt','a') as fp:
        f.write(pwd+'\n')
    if check_end(pwd, char[length-1]):
        break
'''

#生成字典
def create_dictionary(origin):
    char=cancel_repeat(origin)
    length=get_length()
    pwd=itertools.product(char, repeat=length)
    for i in pwd:
        with open('dictionary.txt','a') as fp:
            fp.write(''.join(i)+'\n')
    print('字典已生成')

if __name__ == '__main__':
    origin=input('请输入需要包含的字符：')
    create_dictionary(origin)

