import urllib.parse
import requests 

num = input("Enter Number":)  # Replace with the actual mobile number
msg = input("Enter Massage")# Replace with the actual message

base_url = "https://mojibrsm.com/sms-api/sms-api.php?key=FREE"
params = {
    "num": number,
    "msg": message
}
api_url = base_url + "?" + urllib.parse.urlencode(params)

# Make the API request
response = requests.get(api_url)

# Handle the API response
if response.status_code == 200:
    print("SMS sent successfully.")
else:
    print("Failed to send the SMS.")
