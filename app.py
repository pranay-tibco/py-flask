import os
import uuid
import socket
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

app = Flask(__name__)

uid = uuid.uuid4()
app.secret_key = str(uid)


@app.route('/')
def hello():
    return redirect('/visits-counter')


# ...
@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1  # setting session data
    return "Hello from Server [" + socket.gethostname() \
           + "] Total visitors on this server : {}".format(session.get('visits'))


@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)  # delete visits
    return 'Visits deleted'


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    httpPort = 8080
    if 'HTTP_PORT' in os.environ:
        try:
            httpPort = int(os.environ['HTTP_PORT'])
        except ValueError:
            print("****** Failed to parse environment variable [HTTP_PORT], will use default port 8080")

    print("Starting server on Port: " + str(httpPort))
    app.run(host='0.0.0.0', port=httpPort)

