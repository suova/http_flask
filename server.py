import datetime

from flask import Flask, request, make_response

app = Flask(__name__)

m_dict = {}


@app.route('/dictionary', methods=['POST'])
def post_key():
    if "key" in request.json and "value" in request.json and len(request.json) == 2:
        data = request.json
        if data['key'] not in m_dict:
            key = data['key']
            value = data['value']
            m_dict[key] = value
            response = make_response(
                (
                    {
                        'result': m_dict[key],
                        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    },
                    201
                )
            )
            return response
        else:
            response = make_response(
                (
                    '409 Conflict: Key already exists',
                    409
                )
            )
            return response
    else:
        response = make_response(
            (
                '400 Bad Request: Missing param or too much params',
                400
            )
        )
        return response


@app.route('/dictionary/<key>', methods=['PUT'])
def put_key(key):
    if "key" in request.json and "value" in request.json and len(request.json) == 2:
        data = request.json
        if key in m_dict:
            m_dict[key] = data['value']
            response = make_response(
                (
                    {
                        'result': m_dict[key],
                        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    },
                    200
                )
            )
            return response
        else:
            response = make_response(
                (
                    "404 Not Found: Key didn't find",
                    404
                )
            )
            return response
    else:
        response = make_response(
            (
                '400 Bad Request: Missing param or too much params',
                400
            )
        )
        return response


@app.route('/dictionary/<key>', methods=['GET'])
def get_key(key):
    if key in m_dict:
        response = make_response(
            (
                {
                    'result': m_dict[key],
                    'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                },
                200
            )
        )
        return response
    else:
        response = make_response(
            (
                "404 Not Found: Key didn't find",
                404
            )
        )
        return response


@app.route('/dictionary/<key>', methods=['DELETE'])
def delete_key(key):
    if key in m_dict:
        m_dict.pop(key)
    response = make_response(
        (
            {
                'result': "null",
                'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            },
            200
        )
    )
    return response


if __name__ == '__main__':
    app.run()
