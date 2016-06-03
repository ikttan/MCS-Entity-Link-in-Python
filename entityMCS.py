# Ian Tan, Copyright (c) 2016
# Data Science Institute, Multimedia University

# Sample code taken from MCS site and simplified
import httplib
import json

text = 'Jln Cheras, expect delays from Taman Connaught - the Billion roundabout'

headers = {
    # Request headers
    'Content-Type': 'text/plain',
    'Ocp-Apim-Subscription-Key': 'add_your_subscription_key_here',
}

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/entitylinking/v1.0/link?%s", text, headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    print json.dumps(data, sort_keys=True, indent=2)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
