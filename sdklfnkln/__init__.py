import json
import logging
import azure.functions as func

def main(changes):
    change_li = json.loads(changes)
    for change in change_li: 
        print(change)
        if change['Operation'] == 0: 
            logging.info("THIS IS INSERT")
            logging.info("SQL Change: %s", change)
        else:
            logging.info("THIS IS NOT INSERT")
