from flask import Flask
from redis import Redis
import socket
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s time and my hostname is %s .' %(redis.get('hits'),socket.gethostname())
#           "Your current server is " + socket.gethostname()
#@app.route('/host')
#def host():
#	return "Your current server is " + socket.gethostname()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
