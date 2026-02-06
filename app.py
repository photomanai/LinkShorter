from flask import Flask, render_template, request, abort
import redis
import string
import random

app = Flask(__name__)

# Redis Connection
# Edit here if Redis is password protected or on a different port
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Hash generator function (To keep it short and unique)
def generate_short_id(length=5):
    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choices(characters, k=length))
        # Check if this key exists in Redis (to avoid collisions)
        if not r.exists(short_id):
            return short_id

@app.route('/panel', methods=['GET', 'POST'])
def panel():
    new_link = None
    if request.method == 'POST':
        original_url = request.form.get('url')
        expire_option = request.form.get('expire')

        if original_url:
            short_id = generate_short_id()
            
            # Duration calculation (In seconds)
            ttl = None
            if expire_option == '1h':
                ttl = 3600
            elif expire_option == '1d':
                ttl = 86400
            elif expire_option == '1w':
                ttl = 604800
            elif expire_option == '1m':
                ttl = 2592000
            # If 'never' is selected, ttl remains None (indefinite)

            # Save to Redis
            # Key: short_id, Value: original_url
            r.set(short_id, original_url)
            
            # If there is a duration, set expire
            if ttl:
                r.expire(short_id, ttl)

            # Create the link (Gets the domain dynamically)
            new_link = f"{request.host_url}go/{short_id}"

    return render_template('panel.html', new_link=new_link)

@app.route('/go/<short_id>')
def go(short_id):
    # Retrieve URL from Redis
    original_url = r.get(short_id)
    
    if original_url:
        # If link is found, go to the intermediate page
        return render_template('go.html', original_url=original_url)
    else:
        # If link does not exist or has expired, return 404
        return render_template('go.html', error="This link has expired or does not exist.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)