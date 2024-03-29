import logging
import sys

from flask import Flask, request
from user_agents import parse

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', stream=sys.stdout)
logger = logging.getLogger("main")

log = logging.getLogger('werkzeug')
log.disabled = True

app = Flask(__name__)

# DEBUG ONLY
# app = Flask(__name__,
#             static_url_path='',
#             static_folder='')

index = open("index.html").read()


@app.route("/")
def hello():
    return index


@app.after_request
def after_request(response):
    remote_addr = request.headers.get('X-Forwarded-For') or request.remote_addr
    logger.info(
        "[%s] \"%s %s\" %s (%s)",
        remote_addr,
        request.method,
        request.path,
        response.status_code,
        user_agent_from(request.user_agent)
    )
    return response


def user_agent_from(user_agent_header):
    parsed = parse(str(user_agent_header))
    os = parsed.os.family
    device = parsed.device.family
    browser = parsed.browser.family
    return "%s, %s, %s" % (os, device, browser)


server_port = 5000
logger.info('server start on port: {}'.format(server_port))
app.run(host='127.0.0.1', port=server_port)
