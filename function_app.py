import logging
import azure.functions as func
import pyodbc
import os

def main(changes: func.SqlRowList) -> None:
    print("hello world");
