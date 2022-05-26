"""
This module represents a service layer for random controller
"""

import logging
from models.random_model import random_num_response, otp_response
import random
import exception_handler.exceptions as ex


class random_service():
    """
    This class represent a random service
    """

    def __init__(self) -> None:
        pass

    def gen_random_number() -> random_num_response:
        """
        This method is used to generate a random number
        """
        num = random.random()
        num *= 100
        rnd_num = random.randint(0, int(num))

        return_object = random_num_response(
            number = rnd_num
        )

        return return_object


    def get_otp_count(operationType) -> otp_response:
        opType = operationType 
        counter = {}

        # call data layer
        # counter = datalayer.....
        
        # counter['otpSend'] =  2
        # counter['otpValidate'] = 1
        try:    
            if len(counter) == 0:
                raise ex.NotFoundException('123456789')

            if opType == 'SendOTP':
                return_object = otp_response(
                    count = counter.get('otpSend'),
                    countRemaining = 3 - counter.get('otpSend')
                )
            elif opType == 'ValidateOTP':
                return_object = otp_response(
                    count = counter.get('otpValidate'),
                    countRemaining = 3 - counter.get('otpValidate')
                )
            else:
                raise ex.BadRequestException(opType)
        except(ex.NotFoundException, ex.BadRequestException) as e:
            raise e

        return return_object

