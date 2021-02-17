from pysnmplib.packet import snmp_requests, response


# User with authPriv settings
user = {
    "username": "Jorge",
    "authKey": "ABCDEFGHIJK",
    "authAlg": "usmHMACMD5AuthProtocol",
    "privKey": "ABCDEFGHIJK",
    "privAlg": "usmDESPrivProtocol"
}

# Create the requests engine
req = snmp_requests('v3', user, '192.168.1.200', 161)


# Use the engine to make a couple of requests
resp = req.snmpget([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
resp.pretty_print()

resp = req.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
resp.pretty_print()

resp = req.snmpset([['1.3.6.1.4.1.28308.1.0', ('STRING', 'test_comm')]])
resp.pretty_print()



user = {
    "username": "Jorge2"
}
req = snmp_requests('v3', user, '192.168.1.200', 161)