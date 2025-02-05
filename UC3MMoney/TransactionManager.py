import json
from .TransactionManagementException import TransactionManagementException
from .TransactionRequest import TransactionRequest

class TransactionManager:
    def __init__(self):
        pass

    def ValidateIBAN( self, IbAn ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise TransactionManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise TransactionManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            T_FROM = DATA["from"]
            T_TO = DATA["to"]
            TO_NAME = DATA["receptor_name"]
            req = TransactionRequest(T_FROM, T_TO,TO_NAME)
        except KeyError as e:
            raise TransactionManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateIBAN(T_FROM) :
            raise TransactionManagementException("Invalid FROM IBAN")
        else:
            if not self.ValidateIBAN(T_TO):
                raise TransactionManagementException("Invalid TO IBAN")
        return req