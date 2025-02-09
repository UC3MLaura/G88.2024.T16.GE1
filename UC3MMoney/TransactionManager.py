import json
from TransactionManagementException import TransactionManagementException
from TransactionRequest import TransactionRequest

class TransactionManager:
    def __init__(self):
        pass

    def ValidateIBAN(self, IbAn):
        # Check if it is correct length. If it is, make sure it is written
        # with the correct format.
        if not IbAn.startswith("ES") or len(IbAn) != 24:
            return False
        else:
            iban = IbAn.replace(" ", "").upper()
        # separating iban
        country_code = iban[:2]
        check_digits = iban[2:4]
        account_number = iban[4:]
        # another verification to see if all are numbers
        if not account_number.isdigit():
            return False
        # rearranging the iban
        rearranged_first = account_number + country_code + check_digits
        # replace country code with their numeric equivalents (E=14, S=28)
        rearranged_second = rearranged_first.replace("E", "14").replace("S", "28")
        # perform mod 97
        rearranged_final = int(rearranged_second)  # convert to int
        if rearranged_final % 97 == 1:
            return True
        else:
            return False

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


# validating IBAN
iban_validating = TransactionManager()
valid_iban = "ES9121000418450200051332"
invalid_iban = "ES9121000418450200051333"
# testing
print("Valid IBAN Test Result:", iban_validating.ValidateIBAN(valid_iban))
print("Invalid IBAN Test Result:", iban_validating.ValidateIBAN(invalid_iban))