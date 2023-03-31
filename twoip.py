import requests
import abuse

def twoip(ip):
	url = 'http://ip-api.com/json/'+ip
	querystring = {
	    'ipAddress': ip,
	    'maxAgeInDays': '90'
	}
	headers = {
	    'Accept': 'http://ip-api.com/json',
	}
	response = requests.request(method='GET', url=url, headers=headers, params=querystring)
	res = abuse.add_newlines(response.text)
	res = res[1:-1]
	return res
