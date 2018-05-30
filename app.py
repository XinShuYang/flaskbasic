from flask import Flask,url_for,render_template,make_response
import requests
import urllib3
import urllib.request
from urllib3 import poolmanager
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
@app.route('/website/<name>')
def website(name):
    #response = make_response()
    #r = requests.get('http://www.baidu.com')
    #response.headers.update(r.headers)
    #response.data = r.text
    #return response
    #HTTPConnectionPool.__init__()
    #response = HTTPConnectionPool.urlopen(method='GET',url='http://www.baidu.com')
    #http=poolmanager()
    #response = http.urlopen(method='GET',url='http://www.baidu.com',preload_content=False)
    if (name==None or name==''):
        name='baidu'
    url = 'http://' + name
    #url = 'http://www.'+name+'.com'
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    response = opener.open(url).read()
    return response
@app.route('/websiter/<name>')
def websiter(name):
    url = 'http://' + name 
    response = requests.get(url)
    return response.content.decode('utf-8')
if __name__ == '__main__':
    app.run('127.0.0.2','4000')
#host ip and the port number
