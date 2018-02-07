from flask import Flask
from redis import Redis
import socket
import os
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    html_text = 'Hello World! I have been seen "%s" time and my hostname is %s .' %(redis.get('hits'),socket.gethostname())
    region = os.getenv("AWS_region", "no region specified")
    return "<html><body style='font-family: mono;'>" + "<p>" + html_text + "</p>" + "<p>" + region + "</p>" +"</body></html>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)