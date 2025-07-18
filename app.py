from flask import Flask, render_template
from redis import Redis
import socket
import random
import os

app = Flask(__name__)

# 🔧 Use REDIS_HOST env var, default to 'redis' (for Docker), fallback to 'localhost' if not set
redis_host = os.getenv("REDIS_HOST", "redis")

# Optional: if 'redis' fails to connect, fallback to 'localhost'
try:
    redis = Redis(host=redis_host, port=6379)
    redis.ping()  # Try a test connection
except Exception:
    redis = Redis(host="localhost", port=6379)

quotes = [
    "“Somewhere, something incredible is waiting to be known.” – Carl Sagan",
    "“We are made of star-stuff.” – Carl Sagan",
    "“The cosmos is within us. We are a way for the universe to know itself.” – Carl Sagan",
    "“Not only is the universe stranger than we imagine, it is stranger than we can imagine.” – Arthur Eddington"
]

@app.route("/")
def home():
    try:
        redis.incr('hits')
        hits = redis.get('hits').decode('utf-8')
    except Exception:
        hits = "unknown"
    hostname = socket.gethostname()
    quote = random.choice(quotes)
    return render_template("index.html", hits=hits, hostname=hostname, quote=quote)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
