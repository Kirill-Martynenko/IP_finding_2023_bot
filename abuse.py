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
	return response.text
