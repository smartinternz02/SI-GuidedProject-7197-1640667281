# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:26:36 2022

@author: shiv taneja
"""


import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Dnr8pZzKw-pKWsc_zxaS_5HCs9oslwvd5cFfdGrMriYE"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [["year", "month"]], "values": [[1997,11]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7715ff2d-922c-4d1a-8baf-181460ee4fae/predictions?version=2022-01-21', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
pred=response_scoring.json()
output= pred['predictions'][0]['values'][0][0]
print(output)