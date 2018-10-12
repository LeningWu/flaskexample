
from flask import Flask, render_template, request , make_response ,redirect , flash ,get_flashed_messages

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
app.secret_key='noecoder'

@app.route('/index/')
@app.route('/')
def index():
    res = ''
    for msg in get_flashed_messages():
        res = res + msg + '<br>'
    res += 'hello'
    return 'Hello World!'


@app.route('/profile/<int:uid>/')
def profile(uid):
    colors = ('red', 'green')
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)

@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'
    res =res + request.url+'++'+request.path + '<br>'
    for property in dir(request):
        res = res + str(property) +'|==|<br>' + str(eval('request.' + property)) + '<br>'
    response=make_response(res)
    response.set_cookie('nowcoderid' , key)
    response.status = '404'
    return response

@app.route('/newpath')
def newpath():
    return 'newpath'

@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('newpath',code=code)


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('not_found.html', url=request.url)

@app.route('/login')
def login():
    flash('登录成功 ')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
