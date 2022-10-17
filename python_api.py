# API with Python
# install requests
# pip install requests

import requests

url = "http://api.postcodes.io/postcodes/"

# Asking the user to input the post code
post_code = input("Enter Your Post Code: ")

# Appending the Post Code provided by the user to the URL
url_arg = url + post_code

# display the outcome
response = requests.get(url_arg)

# Checking the type of response received
print(type(response.content))

# Converting the received response of type <bytes> to <dict>
response_dict = response.json()  # json() is an in-build method to convert it to dict

# We only need the 'result'
result_dict = response_dict['result']

for key in result_dict.keys():
    if key == "postcode":
        print(f"Confirm Post Code {key}")
    #print(key)

# BBC Exercise
# # Get
# request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
#
# if request_bbc_status_code.status_code == 200:
#
#     # Check the outcome of our API call
#     print(request_bbc_status_code.status_code)
#     print("*****Headers*****")
#     for item, value in request_bbc_status_code.headers.items():
#         print(item + " - " + value)
#
#     print("*****Content*****")
#     print(request_bbc_status_code.content)
# else:
#     print("Website Couldn't be located. Status Code:" + str(request_bbc_status_code.status_code))
