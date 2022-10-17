# API with Python
# install requests
# pip install requests

import requests
from ukpostcodeutils import validation


# Function to check for validity of post code input by user
def get_valid_post_code():
    valid = True
    while valid:
        postcode = input("Enter Your Post Code without spaces: ")
        if validation.is_valid_postcode(postcode.upper()):
            valid = False

    return postcode


url = "http://api.postcodes.io/postcodes/"

# Asking the user to input the post code
post_code = get_valid_post_code()

# Appending the Post Code provided by the user to the URL
url_arg = url + post_code

# display the outcome
response = requests.get(url_arg)


def get_post_code(results):
    for key in results:
        if key == "postcode":
            return results[key]


def get_longitude(results):
    for key in results:
        if key == "longitude":
            return results[key]


def get_latitude(results):
    for key in results:
        if key == "latitude":
            return results[key]


if response.status_code == 200:

    # Checking the type of response received
    print(f"Type of Response received: {type(response.content)}")

    # Converting the received response of type <bytes> to <dict>
    response_dict = response.json()  # json() is an in-build method to convert it to dict

    # We only need the 'result'
    result_dict = response_dict['result']
    print(f"Post Code: {get_post_code(result_dict)}")
    print(f"Longitude: {get_longitude(result_dict)}")
    print(f"Latitude: {get_latitude(result_dict)}")
else:
    print(f"We Encountered some error: {response.status_code}")


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
