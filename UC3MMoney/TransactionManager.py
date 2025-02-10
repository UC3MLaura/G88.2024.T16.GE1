import json
from TransactionManagementException import TransactionManagementException
from TransactionRequest import TransactionRequest

class TransactionManager:
    def __init__(self):
        self.number_to_letters = {
            "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16,
            "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23,
            "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30,
            "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
        }
        pass

    def convert_letters_to_num(self, letters: str) -> str:
        result = ""
        for letter in letters:
            result = result + str(self.number_to_letters[letter])

        return result

    def ValidateIBAN(self, IbAn):
        # making sure the IBAN is correctly written
        iban = IbAn.replace(" ", "").upper()
        # separating iban in 3 parts
        country_code = iban[:2]
        digits = iban[2:4]
        account_number = iban[4:]
        # another verification to see if all are numbers, and country code
        # is correct
        if (not account_number.isdigit() or country_code[0] not in
                self.number_to_letters and country_code[1] not in
                self.number_to_letters):
            return False
        # executes function created to convert letters to numbers
        country_code_num = self.convert_letters_to_num(country_code)
        print(country_code_num)
        # rearranging the iban with new number country code
        rearranged_first = str(account_number) + country_code_num + str(digits)
        # perform mod 97
        rearranged_final = int(rearranged_first)  # convert to int
        if rearranged_final % 97 == 1:
            print(rearranged_final)
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
valid_iban1 = "ES9121000418450200051332"
valid_iban2 = "DE44500105175407324931"
invalid_iban = "ES0021000418450200051332"
# testing
print("Valid IBAN Test Result:", iban_validating.ValidateIBAN(valid_iban1))
print("Valid IBAN Test Result:", iban_validating.ValidateIBAN(valid_iban2))
print("Invalid IBAN Test Result:", iban_validating.ValidateIBAN(invalid_iban))