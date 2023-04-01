from vtapi3 import VirusTotalAPIIPAddresses, VirusTotalAPIError
import json

def getVirusTotal(ip_addr, api_key):
    result = "Network: %s\nCountry: %s\nOwner: %s\nLast analysis stats:\n\t\t\t\tharmless: %s\n\t\t\t\tmalicious: %s" \
           "\n\t\t\t\tsuspicious: %s\n\t\t\t\tundetected: %s\n\t\t\t\ttimeout: %s\nasn: %s\nid: %s"
    vt_api_ip_addresses = VirusTotalAPIIPAddresses(api_key)
    try:
        output = vt_api_ip_addresses.get_report(ip_addr)
    except VirusTotalAPIError as err:
        return(err + err.err_code)
    else:
        if vt_api_ip_addresses.get_last_http_error() == vt_api_ip_addresses.HTTP_OK:
            output = json.loads(output)
            d = []
            try:
                d.append(output["data"]["attributes"]["network"])
            except KeyError:
                d.append("unknown")
            try:
                d.append(output["data"]["attributes"]["country"])
            except KeyError:
                d.append("unknown")
            try:
                d.append(output["data"]["attributes"]["as_owner"])
            except KeyError:
                d.append("unknown")
            d.append(str(output["data"]["attributes"]["last_analysis_stats"]["harmless"]))
            d.append(str(output["data"]["attributes"]["last_analysis_stats"]["malicious"]))
            d.append(str(output["data"]["attributes"]["last_analysis_stats"]["suspicious"]))
            d.append(str(output["data"]["attributes"]["last_analysis_stats"]["undetected"]))
            d.append(str(output["data"]["attributes"]["last_analysis_stats"]["timeout"]))
            try:
                d.append(str(output["data"]["attributes"]["asn"]))
            except KeyError:
                d.append("unknown")
            d.append(output["data"]["id"])
            result = result % (d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9])
            return(result)
        else:
            return('HTTP Error [' + str(vt_api_ip_addresses.get_last_http_error()) + ']')