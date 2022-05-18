import connexion
import logging

logging.basicConfig(level=logging.DEBUG)
PORT = 5001


def health():
    return {'msg': 'ok'}, 200


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='../openapi')
    app.add_api('spec.yaml')
    app.run(port=PORT)
    logging.INFO(f"Application is running on port:{PORT}")