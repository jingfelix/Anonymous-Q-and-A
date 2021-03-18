# usage: command-line application for reply

from .config import question_file_path, reply_file_path, plate

def init():

    question_file = open(question_file_path, 'r', encoding='gb2312')

    question_list = question_file.readlines()
    question_num = len(question_list) / 2

    print(question_num+'questions received!')
    for i in range(0, question_num):
        print('# '+(i+1)+' ：'+question_list[2*(i+1)])

    # TODO:命令行工具

def reply(question_list, question_num):

    order = input('select ')

    if order == 'exit':
        exit(0)
    else:
        while(not order.isdigit()):
            print('Unknown order!')
            order = input('select: ')
    
    question_name = question_list[2 * int(order) - 1]
    print('Question:' + question_name)

    content = input('reply:')

    render(question_name, content)

def render(question_name, reply_content):

    reply_file = open(reply_file_path, 'a+', encoding='gb2312')

    # TODO:替换 问题名 和 内容 保存文件
    # TODO:记得关闭文件

    reply_file.close()