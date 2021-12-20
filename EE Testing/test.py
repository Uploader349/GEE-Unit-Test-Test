import ee
import os
import json

credentials_json = "ee-credentials.json"

if os.path.exists(credentials_json):
  with open(credentials_json) as f:
    data = json.load(f)
  service_account = data["client_email"]
  credentials = ee.ServiceAccountCredentials(service_account, credentials_json)
  ee.Initialize(credentials)
