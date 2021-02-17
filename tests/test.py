from pysnmplib.packet import snmp_requests, response

# req = snmp_requests('v2c', 'public', '192.168.1.200', 161)

# authAlg:
# USM_AUTH_HMAC96_MD5, USM_AUTH_HMAC96_SHA, USM_AUTH_HMAC128_SHA224, USM_AUTH_HMAC192_SHA256, USM_AUTH_HMAC256_SHA384
# USM_AUTH_HMAC384_SHA512, USM_AUTH_NONE

# privAlg:
# USM_AUTH_HMAC96_MD5, USM_AUTH_HMAC96_SHA, USM_AUTH_HMAC128_SHA224, USM_AUTH_HMAC192_SHA256, USM_AUTH_HMAC256_SHA384
# USM_AUTH_HMAC384_SHA512, USM_AUTH_NONE


user = {
    "username": "Jorge2"
}

user = {
    "username": "Jorge",
    "authKey": "ABCDEFGHIJK",
    "authAlg": "usmHMACMD5AuthProtocol",
    "privKey": "ABCDEFGHIJK",
    "privAlg": "usmDESPrivProtocol"
}



req = snmp_requests('v3', user, '192.168.1.200', 161)


resp = req.snmpget([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
resp.pretty_print()

resp = req.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
resp.pretty_print()
