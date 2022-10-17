# API with Python
# install requests
# pip install requests

import requests

# Get
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

if request_bbc_status_code.status_code == 200:

    # Check the outcome of our API call
    print(request_bbc_status_code.status_code)
    print("*****Headers*****")
    for item, value in request_bbc_status_code.headers.items():
        print(item + " - " + value)

    print("*****Content*****")
    print(request_bbc_status_code.content)
else:
    print("Website Couldn't be located. Status Code:" + str(request_bbc_status_code.status_code))
