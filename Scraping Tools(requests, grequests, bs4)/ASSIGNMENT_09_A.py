import requests

url = 'https://www.programiz.org/'

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    # Print an error message if the request was not successful
    print('Error:', response.status_code)

