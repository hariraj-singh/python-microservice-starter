"""
Rnd Controller - This is a random controller which will generate
a random number.

The routing for this controller is handled by the OpenAPI sepecification file.
"""

import logging
from models.random_model import random_num_response, otp_request, otp_response
from services.random_service import random_service


async def generate_random_number() -> random_num_response:
    """
    This calls the serivce layer to generate random numbers
    """
    logging.info("A new call was made")
    number = random_service.gen_random_number()

    return number


async def get_otp_count(operationType : str) -> otp_response:
    """
    This calls the service layer for otp counters
    """
    logging.info(operationType)
    resp = random_service.get_otp_count(operationType)
    logging.info(otp_response)
    return resp
