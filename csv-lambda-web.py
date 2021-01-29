import csv 

import boto3

from secrets import url 

from botocore.vendored import requests

web = url # use this link as an example to test >> "https://people.sc.fsu.edu/~jburkardt/data/csv/hurricanes.csv"

def lambda_handler(event, context):

    session = requests.Session()
    data = session.get(web)

    parse = data.content.decode("utf-8")

    read = csv.reader(parse.splitlines(), delimiter = ",") #if seperated by tabs replace delimiter value with "\t"

    rows = list(read)
    for row in rows:
        print(row)