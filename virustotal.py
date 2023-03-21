import requests

def getVirusTotal(ip, api_key):

	url = 'https://www.virustotal.com/api/v3/ip_addresses/ip'
	params = {'ip':ip}
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
