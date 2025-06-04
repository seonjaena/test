import json
import logging

def main(changes):
    for change in changes:
        logging.info("method: %s", json.loads(change))
    logging.info("SQL Changes: %s", json.loads(changes))
