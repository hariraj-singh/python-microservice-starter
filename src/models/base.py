"""
This is the base class for models
"""

from dataclasses import dataclass


@dataclass
class base_model():
    """Base class for the models
    """

    def equal(self, __o: object) -> bool:
        """Equal check based on object

        Args:
            object (obj): Object to compare with.

        Returns:
            True if type are the same
        """
        return __o.__class__ is self.__class__
