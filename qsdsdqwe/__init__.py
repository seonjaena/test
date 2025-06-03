import logging
import azure.functions as func
import pyodbc
import os

def main(changes: str, context: func.Context):
    logging.warning('hello world')  # will print a message to the console
    logging.info('hello world')  # will not print anything
    print("hello world")