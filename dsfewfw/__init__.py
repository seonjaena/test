import json
import logging
import azure.functions as func

def main(req: func.HttpRequest, product: func.Out[func.SqlRow]) -> func.HttpResponse:
    try:
        body = json.loads(req.get_body())
        row = func.SqlRow.from_dict(body)
        product.set(row)

        return func.HttpResponse(
            body=req.get_body(),
            status_code=201,
            mimetype="application/json"
        )
    except Exception as e: 
        logger.error(e)

#    logging.info(json.dumps(changes.__dict__, default=lambda o: o.to_json()))
#    logging.info("SQL Changes: %s", json.loads(changes))
