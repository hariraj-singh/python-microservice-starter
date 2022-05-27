"""
This module will contain the various exceptions.
"""

import logging
import werkzeug.exceptions as e

class NotFoundException(RuntimeError):
    """Not found."""

class MyDataNotFound(NotFoundException):
    def __init__(self, error_code, message, detail):
        res = {
            "error_code" : error_code,
            "message" : message,
            "detail" : detail
        }
        logging.info(f"response : {res}")
        super().__init__(res)


class BadRequestException(RuntimeError):
    """Bad Request"""

class MyBadRequest(BadRequestException):
    def __init__(self, error_code, message, detail):
        response = {
            "error_code" : error_code,
            "message" : message,
            "detail" : detail
        }
        logging.info(f"response : {response}")
        super().__init__(response)
    

class InternalServerError(RuntimeError):
    """Internal server error"""

class MyInternalServerError(e.InternalServerError):
    def __init__(self, id):
        super().__init__(f"ID '{id}' something went worng.")
