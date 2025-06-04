import json
import logging
import azure.functions as func

def main(changes):
    logging.info(changes)
    logging.info("SQL Changes: %s", json.loads(changes))
