import datetime
import json
import uuid

import service_template.clients.sqs_v2 as module
from tests.app.requests.sqs_message import test_input, test_output


def test_json_round_trip_encoding():
    input_object = [uuid.uuid4(), datetime.datetime.now()]

    output_object = json.loads(
        json.dumps(input_object, cls=module.RoundTripEncoder,),
        cls=module.RoundTripDecoder,
    )

    assert input_object == output_object


def test_parse_sqs_message():
    raw = test_input

    sqs_client = module.SqsClient()
    result = sqs_client.parse_sqs_messages(raw)

    assert result == test_output
