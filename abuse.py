import requests

def abuse(ip, api_key):
	url = 'https://api.abuseipdb.com/api/v2/check'
	querystring = {
	    'ipAddress': ip,
	    'maxAgeInDays': '90'
	}
	headers = {
	    'Accept': 'application/json',
    'Key': api_key
	}
	response = requests.request(method='GET', url=url, headers=headers, params=querystring)
	res = add_newlines(response.text)
	res = res[9:-2]
	return res

def add_newlines(text):
    new_text = ""
    for char in text:
        if char == ",":
            new_text += "\n"
        else:
            new_text += char
    return new_text
