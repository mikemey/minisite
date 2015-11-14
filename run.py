from flask import Flask
from werkzeug import serving
from werkzeug._internal import _log


class LimitLogHandler(serving.WSGIRequestHandler):
    def log(self, type, message, *args):
        host_header = self.headers.getheader('X-Forwarded-For', 'unknown')
        ua_header = self.headers.getheader('User-Agent', 'user-agent unknown')
        msg = message % args
        _log(type, '%s [%s - %s]\n' % (msg, host_header, ua_header))


app = Flask(__name__)

index = open("index.html").read()


@app.route("/")
def hello():
    return index


if __name__ == "__main__":
    import logging

    # logging.basicConfig(filename='msm-site.log', level=logging.DEBUG,
    #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(filename='/var/log/msm-site.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app.run(request_handler=LimitLogHandler)
