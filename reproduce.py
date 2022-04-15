import boto3

boto3.client("s3") 
# import numpy


def app(environ, start_response):

    """Simplest possible application object"""
    data = b"Hello, World!\n"
    status = "200 OK"
    response_headers = [
        ("Content-type", "text/plain"),
        ("Content-Length", str(len(data))),
    ]
    start_response(status, response_headers)
    return iter([data])


def create_app():
    return app
