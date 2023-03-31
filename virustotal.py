from vtapi3 import VirusTotalAPIIPAddresses, VirusTotalAPIError
import json

import abuse

def getVirusTotal(ip_addr, api_key):
    result = ""
    vt_api_ip_addresses = VirusTotalAPIIPAddresses(api_key)
    try:
        output = vt_api_ip_addresses.get_report(ip_addr)
    except VirusTotalAPIError as err:
        return(err + err.err_code)
    else:
        if vt_api_ip_addresses.get_last_http_error() == vt_api_ip_addresses.HTTP_OK:
            output = json.loads(output)
            result += "Network: " + output["data"]["attributes"]["network"] + "\n"
            result += "Country: " + output["data"]["attributes"]["country"] + "\n"
            result += "Owner: " + output["data"]["attributes"]["as_owner"] + "\n"
            result += "Last analysis stats:\n"
            result += "\t\t\t\t"
            result += "harmless: " + str(output["data"]["attributes"]["last_analysis_stats"]["harmless"]) + "\n"
            result += "\t\t\t\t"
            result += "malicious: " + str(output["data"]["attributes"]["last_analysis_stats"]["malicious"]) + "\n"
            result += "\t\t\t\t"
            result += "suspicious: " + str(output["data"]["attributes"]["last_analysis_stats"]["suspicious"]) + "\n"
            result += "\t\t\t\t"
            result += "undetected: " + str(output["data"]["attributes"]["last_analysis_stats"]["undetected"]) + "\n"
            result += "\t\t\t\t"
            result += "timeout: " + str(output["data"]["attributes"]["last_analysis_stats"]["timeout"]) + "\n"
            result += "asn: " + str(output["data"]["attributes"]["asn"]) + "\n"
            result += "id: " + output["data"]["id"]
            return(result)
        else:
            return('HTTP Error [' + str(vt_api_ip_addresses.get_last_http_error()) + ']')