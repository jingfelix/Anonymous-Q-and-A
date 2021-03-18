# 匿名提问箱 服务器端开发
# Time:2021 03 08
from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form
from messageProcess import inputProcess, replyRender, notice
from logrec import errorRecorder, ipRecorder


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yourkey'
# 声明路由的修饰器

# 接受所有初始对象

@app.route('/', methods=['GET', 'POST'])
def index():
    ipRecorder(str(request.remote_addr))
    if request.method == 'POST':
        inputProcess(request.form.get('text'))
        return render_template('index.html', content=replyRender(), notice = notice)
    else:
        # 使用了jinja2模板引擎
        return render_template('index.html', content=replyRender(), notice = '')

@app.route('/about')
def about():
    '''
    响应返回about界面
    '''
    return render_template('about.html')

# 自定义错误界面
@app.errorhandler(404)
def page_not_found(e):
    '''
    404错误响应
    '''
    errorRecorder(404)
    # 返回404页面和状态码
    return render_template('error.html', error = 404), 404

@app.errorhandler(500)
def server_error(e):
    '''
    500错误响应
    '''
    errorRecorder(500)
    return render_template('error.html', error = 500), 500

# 运行服务器
if __name__ == '__main__':
    app.run(debug=True)