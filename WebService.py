from flask import Flask, jsonify, request
app = Flask(__name__)
animals = { 'Ellie' : { 'type': 'Elephant', 'born': 1996 },
            'Monty' : { 'type': 'Python'  , 'born': 2013 },
            'Zed'   : { 'type': 'Zebra'   , 'born': 2017 } }


@app.route('/')
def index():
    url = f'http://localhost:{port}/animal'
    return f"""<!DOCTYPE html><html><head><title>Flask RESTful API</title></head>
              <body><h1>RESTful API in Python with Flask</h1>
              <ul>
              <li><b>GET all (read):</b> <pre>curl -i {url}s</pre></li>
              <li><b>GET one (read):</b> <pre>curl -i {url}/Ellie</pre></li>
              <li><b>POST (create):</b> <pre>curl -i -H "Content-type: 
application/json" -X POST -d "{{ \\"Max\\": {{ \\"type\\": \\"Mouse\\", \\"born\\": 
2019 }} }}" {url}</pre></li>
              <li><b>PUT (update):</b> <pre>curl -i -H "Content-type: 
application/json" -X POST -d "{{ \\"type\\": \\"Giraffe\\", \\"born\\": 2017 }}" 
{url}/Zed</pre></li>
              <li><b>DELETE (delete):</b> <pre>curl -i -X DELETE {url}/Ellie</pre>
</li>
              </ul>
              </body></html>"""


@app.route('/animals')
def getAll():
    return jsonify(animals)


@app.route('/animal/<name>')
def getOne(name):
    if name in animals:
        return jsonify(animals[name])
    else:
        return jsonify(None)


@app.route('/animal', methods=['POST'])
def addOne():
    post_content = request.get_json()
    animals.update(post_content)
    return jsonify(animals)


@app.route('/animal/<name>', methods=['POST'])
def updateOne(name):
    animals[name] = request.get_json()
    return jsonify(animals)


@app.route('/animal/<name>', methods=['DELETE'])
def removeOne(name):
    if name in animals:
        del animals[name]
    return jsonify(animals)


if __name__ == '__main__':
    port = 8888
    app.run(port=port, debug=True)