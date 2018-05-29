from flask import Flask,url_for,render_template

app = Flask(__name__)
@app.route('/')
def one():
    return 'Better Call Goodman'
#'/test/' with '/' in the end could also accept url '/test'; However, '/test'is the only url and it could not accept '/test/'
@app.route('/test/')
def test():
    return 'Test Successful'
#conventor could accept types such as int,float and path; notice the <int:number> rule;
@app.route('/test/<int:number>')
def show_number(number):
    string = ''
    for i in range(1,number):
        string=string+str(i)
    return 'Test conventor result: %s' %string
#'url_for' could generate url from given functions
@app.route('/test/url_for')
def urlfor():
    return url_for('test')
#this rule of 'url_for' could generate a url from given static file path
@app.route('/test/url_for_static')
def urlfor_static():
    return url_for('static', filename='css/core.css')
@app.route('/<name>.html')
def htmltest(name="index"):
    return render_template(name+'.html')
if __name__ == '__main__':
    app.run('127.0.0.2','4000')
#host ip and the port number
