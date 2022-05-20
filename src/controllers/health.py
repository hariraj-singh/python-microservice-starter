"""
This module represents the Helth-Check controller end-point.

This end-point is not part of the specification and is configured
directly with Flask

Example:
    To open the end-point 'http://<host>:<port>/health'
"""

def health():
    """
    Get the health of the service.

    Returns:
        Ok response
    """
    return {'msg': 'ok'}, 200