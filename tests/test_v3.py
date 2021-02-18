from snmp_requests import snmp_engine, response


# User with authPriv settings
user = {
    "username": "Jorge",
    "authKey": "ABCDEFGHIJK",
    "authAlg": "usmHMACMD5AuthProtocol",
    "privKey": "ABCDEFGHIJK",
    "privAlg": "usmDESPrivProtocol"
}

# Create the requests engine
eng = snmp_engine('v3', user, '192.168.1.200', 161)


# Use the engine to make a couple of requests
# resp = eng.snmpget([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
# resp.pretty_print()
#
# resp = eng.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
# resp.pretty_print()
#
# resp = eng.snmpset([['1.3.6.1.4.1.28308.1.0', ('STRING', 'test_comm')]])
# resp.pretty_print()

eng.snmpwalk('1.3')

# resp = eng.snmpgetnext([['1.3.6.1.4.1.28308.1.0', None]])
# resp.pretty_print()





user = {
    "username": "Jorge2"
}
eng = snmp_engine('v3', user, '192.168.1.200', 161)