import json
import logging

def main(changes):
    for change in changes:
        logging.info("method: %s", getattr(change, 'operation', None))
    logging.info("SQL Changes: %s", json.loads(changes))
