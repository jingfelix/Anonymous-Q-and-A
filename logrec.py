# 
import time
from os import getcwd

log_file_path = getcwd() + '\data\log.txt'

def ipRecorder(ip):
    '''
    记录访问的ip地址并写入日志
    '''
    localtime = time.asctime(time.localtime(time.time()))
    file = open(log_file_path, 'a+')
    file.write(localtime + ' ' + str(ip) + '\n')
    file.close()

    pass

def errorRecorder(status):
    '''
    记录错误状态码并写入日志
    '''
    localtime = time.asctime(time.localtime(time.time()))
    file = open(log_file_path, 'a')
    file.write(localtime +  'ErrorStatus:' + str(status) + '\n')
    file.close()

    pass