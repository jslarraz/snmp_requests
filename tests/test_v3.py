from snmp_requests import snmp_engine

# User with authPriv settings
user = {
    "username": "Jorge",
    "level": "authPriv",
    "authKey": "ABCDEFGHIJK",
    "authAlg": "MD5",
    "privKey": "ABCDEFGHIJK",
    "privAlg": "DES"
}

# Read config
import os

ip_addr = os.environ.get('ip_addr', 'localhost')            # Direccion IP
port = os.environ.get('port', 161)                          # Puerto
eng = snmp_engine('3', user, ip_addr, port)                 # Create engine


# Use the engine to make a couple of requests

print("---------------------------------------GET------------------------------------------")
print("")

# Make a get request with one valid varBinds
print("Make a get request with one valid varBind, .1.3.6.1.2.1.1.1.0")
resp = eng.snmpget([['.1.3.6.1.2.1.1.1.0', None]])
print(resp)
print("")

# Make a get request with a couple of valid varBinds
print("Make a get request of 2 valid varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.2.1.2.1.0")
resp = eng.snmpget([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
print(resp)
print("")

# Make a get request with one erroneous varBind
print("Make a get request with one erroneous varBind, .1.3.6.1.2")
resp = eng.snmpget([['.1.3.6.1.2', None]])
print(resp)
print("")

# Make a get request with one valid and one erroneous varBinds
print("Make a get request with one valid and one erroneous varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.2")
resp = eng.snmpget([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2', None]])
print(resp)
print("")


print("-----------------------------------GETNEXT------------------------------------------")
print("")

# Make a getnext request with one valid varBinds
print("Make a getnext request with one valid varBind, .1.3.6.1.2.1.1.1.0")
resp = eng.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None]])
print(resp)
print("")

# Make a getnext request with a couple of valid varBinds
print("Make a getnext request of 2 valid varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.2.1.2.1.0")
resp = eng.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
print(resp)
print("")

# Make a getnext request with one erroneous varBind
print("Make a getnext request with one erroneous varBind, .1.3.6.1.7")
resp = eng.snmpgetnext([['.1.3.6.1.7', None]])
print(resp)
print("")

# Make a getnext request with one valid and one erroneous varBinds
print("Make a getnext request with one valid and one erroneous varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.7")
resp = eng.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.7', None]])
print(resp)
print("")


print("---------------------------------------SET------------------------------------------")
print("")

# Make a set request with one valid varBinds
print("Make a set request with one valid varBinds")
resp = eng.snmpset([['1.3.6.1.2.1.1.5.0', ('STRING', 'test_comm')]])
print(resp)
print("")


print("---------------------------------------WALK-----------------------------------------")
print("")

# Make a set request with one valid varBinds
print("Make a walk from the root of the mib")
r = eng.snmpwalk('1.3')
print(r)
print("")


print("---------------------------------------NO ACCESS------------------------------------------")
print("")

user = {
    "username": "Jorge2"
}
eng = snmp_engine('3', user, '192.168.1.200', 161)