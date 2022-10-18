import requests
from ukpostcodeutils import validation


class PythonApi:
    def __init__(self, postcode):
        self.url = "http://api.postcodes.io/postcodes/"
        self.post_code = postcode

    def get_response(self):
        # Appending the Post Code provided by the user to the URL
        url_arg = self.url + self.post_code
        response = requests.get(url_arg)
        return response

    def get_post_code(self, results):
        for key in results:
            if key == "postcode":
                return results[key]

    def get_longitude(self, results):
        for key in results:
            if key == "longitude":
                return results[key]

    def get_latitude(self, results):
        for key in results:
            if key == "latitude":
                return results[key]


# Function to check if post code is valid or not
def get_valid_post_code():
    valid = True
    while valid:
        postcode = input("Enter Your Post Code without spaces: ")
        if validation.is_valid_postcode(postcode.upper()):
            valid = False

    return postcode

# Asking the user to input the post code
post_code = get_valid_post_code()

# Initializing the class object
checker = PythonApi(post_code)

# Getting the response
response = checker.get_response()

if response.status_code == 200:

    # Checking the type of response received
    print(f"Type of Response received: {type(response.content)}")

    # Converting the received response of type <bytes> to <dict>
    response_dict = response.json()  # json() is an in-build method to convert it to dict

    # We only need the 'result'
    result_dict = response_dict['result']
    print(f"Post Code: {checker.get_post_code(result_dict)}")
    print(f"Longitude: {checker.get_longitude(result_dict)}")
    print(f"Latitude: {checker.get_latitude(result_dict)}")
else:
    print(f"We Encountered some error: {response.status_code}")
