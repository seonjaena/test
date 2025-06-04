import json
import logging
import azure.functions as func

def main(changes: func.SqlRowList):
    for change in changes:
        logging.info("method: %s", json.loads(change))
    logging.info("SQL Changes: %s", json.loads(changes))
