import json
import logging
import azure.functions as func
from azure.functions.decorators.core import DataType

app = func.FunctionApp()

@app.function_name(name="werqwe")
@app.sql_trigger(arg_name="change",
                        table_name="test_nato2",
                        connection_string_setting="SqlConnectionString")
def todo_trigger(change: str) -> None:
    logging.info("SQL Changes: %s", json.loads(change))