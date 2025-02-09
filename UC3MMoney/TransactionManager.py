import json
from TransactionManagementException import TransactionManagementException
from TransactionRequest import TransactionRequest

class TransactionManager:
    def __init__(self):
        pass

    def ValidateIBAN(self, IbAn):
        # Step 1: Check if IBAN starts with 'ES' and is 24 characters long (2 for country code + 2 for check digits + 20 for account number)
        if len(IbAn) != 24 or not IbAn.startswith("ES"):
            return False

        # Step 2: Separate the parts of the IBAN
        country_code = IbAn[:2]
        check_digits = IbAn[2:4]
        account_number = IbAn[4:]

        # Step 3: Ensure account number is all digits
        if not account_number.isdigit():
            return False

        # Step 4: Create a string by moving the country code and check digits to the end
        rearranged_iban = account_number + country_code + check_digits

        # Step 5: Replace country code with their numeric equivalents (E=14, S=28)
        rearranged_iban = rearranged_iban.replace('E', '14').replace('S', '28')

        # Step 6: Perform the modulus operation (mod 97)
        iban_number = int(rearranged_iban)  # Convert to integer
        if iban_number % 97 == 1:
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