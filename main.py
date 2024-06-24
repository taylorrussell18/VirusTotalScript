import requests

# Define a function to check if a URL is malicious
def is_malicious(url, api_key):
    url = url.strip()
    params = {'apikey': api_key, 'resource': url}
    # Make a GET request to the URL
    response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
    # Turn the response into a JSON object
    json_response = response.json()
    # If the link is greater than zero return true if not return false
    if json_response.get('positives', 0) > 0:
        return True
    else:
        return False

# Get API key manually from user
api_key = '199f0ee652f9f1adb623dd2fec42d1720614303397a9ef3ea244d538f31c9f81'

# Define a function to get user input for URLs
def get_urls():
    urls = input("Enter the URLs (separated by commas): ")
    return urls.split(',')

# Get URLs from user
urls = get_urls()

# Check each URL in a for loop and print if it's malicious
for url in urls:
    if is_malicious(url, api_key):
        print(f"{url} is malicious.")
    else:
        print(f"{url} is not malicious.")
