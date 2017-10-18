import uuid

import boto3
from flask import Flask, request, jsonify

from twenty_four.lib import get_solutions

app = Flask(__name__)


@app.route('/api/v0/solutions', methods=['GET'])
def index():
    numbers = [
        int(i)
        for i in request.args['values'].split(',')
    ]

    if len(numbers) != 4:
        return 'must contain 4 comma-separated values', 500

    solutions = {'values': get_solutions(numbers)}

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Rides')
    table.put_item(
        Item={
            'RideId': str(uuid.uuid4()),
            'input': numbers,
            'output': solutions,
        },
    )

    response = jsonify(solutions)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
