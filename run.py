from flask import Flask
from user_agents import parse
from werkzeug import serving
from werkzeug._internal import _log


class LimitLogHandler(serving.WSGIRequestHandler):
    def log(self, type, message, *args):
        host_header = self.headers.getheader('X-Forwarded-For', 'unknown')
        ua_header = user_agent_from(self.headers.getheader('User-Agent', 'user-agent unknown'))
        msg = message % args
        _log(type, '%s [%s - %s]\n' % (msg, host_header, ua_header))


def user_agent_from(user_agent_header):
    parsed = parse(user_agent_header)
    os = parsed.os.family
    device = parsed.device.family
    browser = parsed.browser.family
    return "%s, %s, %s" % (os, device, browser)


app = Flask(__name__)

index = open("index.html").read()


@app.route("/")
def hello():
    return index


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app.logger.info('server start...')
app.run(request_handler=LimitLogHandler, host='127.0.0.1')
