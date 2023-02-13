from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def GetMain () :
    arg1 = request.args.get('arg1')
    print(arg1)
    return 'DONE'

@app.route('/', methods=['POST'])
def PostMain() :
    arg1 = request.form('arg1')
    print(arg1)
    return 'DONE'
    
@app.route('/all', methods=['GET'])
def GetAll() :
    print("--------   INFO   -------- ")
    print(request)
    print("-------- HEADERS -------- ")
    print(request.headers)
    print("-------- COOKIES -------- ")
    if(len(request.cookies) > 0) :
        for i in request.cookies :
            print(i + "  :  " + request.cookies[i])
    else :
        print("NO COOKIES")
    print("--------  DATA   -------- ")
    print(request.data)
    
    return 'DONE'
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=1337, debug=True)
    
    
#python2 -m SimpleHTTPServer 1337
#python3 -m http.server 1337