
from flask import Flask, render_template, request , make_response ,redirect

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'


@app.route('/index/')
@app.route('/')
def index():
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
        res =res+str(property)+'|==|<br>' + str(eval('request.' + property)) + '<br>'
    response=make_response(res)
    response.set_cookie('nowcoderid',key)
    response.status='404'
    return response

@app.route('/newpath')
def newpath():
    return 'newpath'

@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('newpath',code=code)


if __name__ == '__main__':
    app.run(debug=True)
