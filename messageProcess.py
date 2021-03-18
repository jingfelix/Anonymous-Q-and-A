import time
from os import getcwd

question_file_path = getcwd() + r'\data\questions.txt'
reply_file_path = getcwd() + r'\data\reply.txt'

notice = '<div class="menuitem">已经提交了哦！</div>'

def inputProcess(message):
    '''
    对接收到的POST中的信息进行处理
    增加时间和换行
    '''
    localtime = time.asctime(time.localtime(time.time()))    
    
    content = localtime + '\n' + message + '\n'

    file = open(question_file_path, 'a')
    file.write(content)
    file.close()

    pass

def replyRender():
    '''
    负责渲染回复部分
    '''
    content = ''

    file = open(reply_file_path, 'r', encoding='utf-8')
    content = file.read()
    
    file.close()
    return content