from snmp_requests import snmp_engine, response


# Create the requests engine
eng = snmp_engine('v2c', 'public', '192.168.1.200', 161)


# Use the engine to make a couple of requests

print("---------------------------------------GET------------------------------------------")
print("")

# Make a get request with one valid varBinds
print("Make a get request with one valid varBind, .1.3.6.1.2.1.1.1.0")
resp = eng.snmpget([['.1.3.6.1.2.1.1.1.0', None]])
resp.pretty_print()
print("")

# Make a get request with a couple of valid varBinds
print("Make a get request of 2 valid varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.2.1.2.1.0")
resp = eng.snmpget([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
resp.pretty_print()
print("")

# Make a get request with one erroneous varBind
print("Make a get request with one erroneous varBind, .1.3.6.1.2")
resp = eng.snmpget([['.1.3.6.1.2', None]])
resp.pretty_print()
print("")

# Make a get request with one valid and one erroneous varBinds
print("Make a get request with one valid and one erroneous varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.2")
resp = eng.snmpget([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2', None]])
resp.pretty_print()
print("")


print("-----------------------------------GETNEXT------------------------------------------")
print("")

# Make a getnext request with one valid varBinds
print("Make a getnext request with one valid varBind, .1.3.6.1.2.1.1.1.0")
resp = eng.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None]])
resp.pretty_print()
print("")

# Make a getnext request with a couple of valid varBinds
print("Make a getnext request of 2 valid varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.2.1.2.1.0")
resp = eng.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.2.1.2.1.0', None]])
resp.pretty_print()
print("")

# Make a getnext request with one erroneous varBind
print("Make a getnext request with one erroneous varBind, .1.3.6.1.7")
resp = eng.snmpgetnext([['.1.3.6.1.7', None]])
resp.pretty_print()
print("")

# Make a getnext request with one valid and one erroneous varBinds
print("Make a getnext request with one valid and one erroneous varBinds, .1.3.6.1.2.1.1.1.0 and .1.3.6.1.7")
resp = eng.snmpgetnext([['.1.3.6.1.2.1.1.1.0', None], ['.1.3.6.1.7', None]])
resp.pretty_print()
print("")


print("---------------------------------------SET------------------------------------------")
print("")

# Make a set request with one valid varBinds
print("Make a set request with one valid varBinds")
resp = eng.snmpset([['1.3.6.1.4.1.28308.1.0', ('STRING', 'test_comm')]])
resp.pretty_print()
print("")


print("---------------------------------------WALK-----------------------------------------")
print("")

# Make a set request with one valid varBinds
print("Make a walk from the root of the mib")
r = eng.snmpwalk('1.3')
print(r)
print("")

