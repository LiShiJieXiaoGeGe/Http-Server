#!/usr/bin/python3
#coding:utf-8
import sys, os
import urllib

length = os.getenv('CONTENT_LENGTH')

if length:  #* post请求 标准输入和标注输出已被子进程重定向
    #? 从标准输入读
    postdata = sys.stdin.read(int(length))

    #? 输入到标准输出, 给父进程读
    print("Content-type:text/html\n")
    print()

    print('<html>')
    print('<head>')
    print('<title>POST</title>')
    print('</head>')
    print('<body>')
    print('<h2> Your POST data: </h2>')
    print('<ul>')
    for data in postdata.split('&'):
        print('<li>' + data + '</li>')
    print('</ul>')
    print('</body>')
    print('</html>')

else:  #* get请求
    print("Content-type:text/html\n")
    print('no found')
