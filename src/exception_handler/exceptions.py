"""
This module will contain the various exception handlers.
"""

# from werkzeug import exceptions
# from __main__ import app
# from flask import json


# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     status_code = 500
#     detail = 'Something went wrong in the server'

# app.register_error_handler(400, handle_exception)


# @app.errorhandler(exceptions.InternalServerError)
# def handle_ISR(e):
#     return 'Something went wrong', 400


# @app.errorhandler(exceptions.MethodNotAllowed)
# def handle_method_not_allowed(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response


import logging

import werkzeug.exceptions as e


class NotFoundException(RuntimeError):
    """Not found."""

class MyDataNotFound(NotFoundException):
    def __init__(self, id):
        super().__init__(f"ID '{id}' not found.")

class BadRequestException(RuntimeError):
    """Bad Request"""

class MyBadRequest(NotFoundException):
    def __init__(self, id):
        super().__init__(f"ID '{id}' bad request.")

class InternalServerError(RuntimeError):
    """Internal server error"""

class MyInternalServerError(e.InternalServerError):
    def __init__(self, id):
        super().__init__(f"ID '{id}' something went worng.")
