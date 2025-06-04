import json
import logging
import azure.functions as func

def main(changes: func.SqlRowList): 
    for change in changes:
        logging.info(change)

#    logging.info(json.dumps(changes.__dict__, default=lambda o: o.to_json()))
#    logging.info("SQL Changes: %s", json.loads(changes))
