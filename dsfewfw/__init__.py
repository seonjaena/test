import json
import logging
import azure.functions as func

def main(req: func.HttpRequest, avsd: func.Out[func.SqlRow]) -> func.HttpResponse:
    body = json.loads(req.get_body())
    row = func.SqlRow.from_dict(body)
    logging.info(body)
    logging.info(row)
    logging.info(avsd)


#    logging.info(json.dumps(changes.__dict__, default=lambda o: o.to_json()))
#    logging.info("SQL Changes: %s", json.loads(changes))
