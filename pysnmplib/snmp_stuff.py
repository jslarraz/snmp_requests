#from pysnmp.hlapi.asyncore import *
#from scapy.all import *

class ASN1_object(object):

    # Class migth be:
    # UNIVERSAL (0)
    # APPLICATION (1)
    # PRIVATE (2)
    # CONTEXT-SPECIFIC (3)
    class_number = 0

    # Build-in types mighth by:
    # Simple (0)
    # Constructed (1)
    kind_of_type = 0

    # Universal types are:
    # Reserved for BER (0)
    # BOOLEAN (1)
    # INTEGER (2)
    # BIT STRING (3)
    # OCTET STRING (4)
    # NULL (5)
    # OBJECT IDENTIFIER (6)
    # ObjectDescriptor (7)
    # INTANCE OF, EXTERNAL (8)
    # REAL (9)

    # ENUMERATED (10)
    # EMBEDDED PDV (11)
    # UTF8String (12)
    # RELATIVE-OID (13)
    # SEQUENCE, SEQUENCE OF (16)
    # SET, SET OF (17)
    # NumericString (18)
    # PrintableString (19)
    type = 0

    # Represent the length in octets of the value
    length = 0

    # The value it self if a simple type or other ASN.1 objects when constructed
    value = 0

    def __init__(self, class_number, kind_of_type, type, length, value):
        self.class_number = class_number
        self.kind_of_type = kind_of_type
        self.type = type
        self.length = length
        self.value = value


    def __print__(self):
        return self.value




    def get_ber(self):


        return None



class INTEGER(ASN1_object):

    def __init__(self, value):
        self.class_number = 0   # Universal
        self.kind_of_type = 0   # Simple
        self.type = 2           # Integer

        # Calc length
        self.length = (value / 255) + 1
        self.value = value



print(INTEGER(2).get_ber())

