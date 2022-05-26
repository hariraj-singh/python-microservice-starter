"""
This is the model for random number
"""
from models.base import base_model, dataclass


@dataclass
class random_num_response(base_model):
    """
    This class represents the random number response
    """
    number : int = 0

    def __init__(self, **kwargs) -> None:
        super().__init__()

        self.number = kwargs.get("number", 0)

@dataclass
class otp_request(base_model):
    """
    This class reps the otp request
    """
    operationType : str = ''

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.operationType = kwargs.get("opertaionType")


@dataclass
class otp_response(base_model):
    """
    This class reps the otp response
    """
    count : str = ''
    countRemaining : str = ''

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.count = kwargs.get("count")
        self.countRemaining = kwargs.get("countRemaining")

 