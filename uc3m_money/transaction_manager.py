"""
Module for managing financial transactions.

This module provides:
- IBAN validation logic
- Reading transaction details from JSON
- Handling financial transaction processing

Classes:
- TransactionManager: Handles IBAN validation and transaction JSON parsing.
"""

import json
from uc3m_money.transaction_management_exception import TransactionManagementException
from uc3m_money.transaction_request import TransactionRequest


class TransactionManager:
  """Handles IBAN validation and transaction processing."""

  def __init__(self):
    """Initializes number-to-letter mappings for IBAN conversion."""
    self.number_to_letters = {
      "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16,
      "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23,
      "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30,
      "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
    }

  def convert_letters_to_num(self, letters: str) -> str:
    """
    Converts country code letters to their corresponding numeric values.

        Args:
            letters (str): Country code (first two letters of IBAN).

        Returns:
            str: Numeric representation of country code.
        """
    return "".join(str(self.number_to_letters[letter]) for letter in letters)

  def validate_iban(self, iban: str) -> bool:
    """
        Validates an IBAN using the ISO 13616-1 standard.

        Args:
            iban (str): The IBAN string to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
    iban = iban.replace(" ", "").upper()
    if len(iban) < 4:
      return False

    country_code = iban[:2]
    check_digits = iban[2:4]
    account_number = iban[4:]

    # Ensure valid characters
    if not account_number.isdigit() or country_code[0] not in self.number_to_letters or country_code[1] not in self.number_to_letters:
      return False

    # Convert country code to numbers
    country_code_num = self.convert_letters_to_num(country_code)

    # Rearrange IBAN and check modulo 97
    rearranged_iban = int(account_number + country_code_num + check_digits)
    return rearranged_iban % 97 == 1

  def read_product_code_from_json(self, file_path: str) -> TransactionRequest:
    """
        Reads transaction details from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            TransactionRequest: A TransactionRequest object.

        Raises:
            TransactionManagementException: If JSON file is invalid or missing required keys.
        """
    try:
      with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
    except FileNotFoundError as error:
      raise TransactionManagementException("Wrong file or file path") from error
    except json.JSONDecodeError as error:
      raise TransactionManagementException("JSON Decode Error - Wrong JSON Format") from error

    try:
      t_from = data["from"]
      t_to = data["to"]
      to_name = data["receptor_name"]
      request = TransactionRequest(t_from, t_to, to_name)
    except KeyError as error:
      raise TransactionManagementException("JSON Decode Error - Invalid JSON Key") from error

    if not self.validate_iban(t_from):
      print("Invalid FROM IBAN")
    else:
      if not self.validate_iban(t_to):
        print("Invalid TO IBAN")

    return request


# IBAN validation testing
if __name__ == "__main__":
  transaction_manager = TransactionManager()

  VALID_IBAN_1 = "ES9121000418450200051332"
  VALID_IBAN_2 = "DE44500105175407324931"
  INVALID_IBAN = "ES0021000418450200051332"

  print("Valid IBAN Test Result:", transaction_manager.validate_iban(VALID_IBAN_1))
  print("Valid IBAN Test Result:", transaction_manager.validate_iban(VALID_IBAN_2))
  print("Invalid IBAN Test Result:", transaction_manager.validate_iban(INVALID_IBAN))
