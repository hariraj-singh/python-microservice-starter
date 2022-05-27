"""
This module contains the various exception handlers
"""

from flask import jsonify


def not_found_handler(error):
    return {
        "detail": str(error),
    }, 404



def bad_request_handler(error):
    return {
        "detail": str(error),
    }, 400


def internal_server_handler(error):
    return {
        "error_code": 'SRVX400',
        "message": "BadRequest",
    }, 400

  