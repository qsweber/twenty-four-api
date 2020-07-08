import logging
import json

import typing

from flask import Flask, jsonify, request, Response
from raven import Client  # type: ignore
from raven.contrib.flask import Sentry  # type: ignore
from raven.transport.requests import RequestsHTTPTransport  # type: ignore

from twenty_four.lib import get_solutions


app = Flask(__name__)
sentry = Sentry(app, client=Client(transport=RequestsHTTPTransport,),)
logger = logging.getLogger(__name__)


@app.route("/api/v0/status", methods=["GET"])
def status() -> Response:
    logger.info("recieved request with args {}".format(json.dumps(request.args)))

    response = jsonify({"text": "ok"})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return typing.cast(Response, response)


@app.route('/api/v0/solutions', methods=['GET'])
def index() -> Response:
    numbers = [
        int(i)
        for i in request.args['values'].split(',')
    ]

    if len(numbers) != 4:
        return 'must contain 4 comma-separated values', 500

    solutions = {'values': get_solutions(numbers)}

    response = jsonify(solutions)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return typing.cast(Response, response)
