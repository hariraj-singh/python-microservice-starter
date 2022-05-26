
def not_found_handler(error):
    return {
        "message": "Not Found",
        "code": 404,

    }, 404



def bad_request_handler(error):
    return {
        "detail": str(error),
        "status": 400,
        "title": "Bad Request",
    }, 400


def internal_Sv(error):
    return {
        "detail": str(error),
        "status": 500,
        "title": "SWW",
    }, 500

  