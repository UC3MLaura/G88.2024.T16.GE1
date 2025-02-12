"""
Main module for transaction processing.
"""

import string
from uc3m_money import TransactionManager

# Global constants
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3

def encode(word):
  """
    Encodes a word using a simple shift cipher.

    Args:
        word (str): The input string.

    Returns:
        str: The encoded string.
  """
  encoded = ""
  for letter in word:
    if letter == " ":
      encoded += " "
    else:
      index = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
      encoded += LETTERS[index]
  return encoded

def decode(word):
  """
    Decodes a word using a simple shift cipher.

    Args:
        word (str): The encoded string.

    Returns:
        str: The decoded string.
  """
  decoded = ""
  for letter in word:
    if letter == " ":
      decoded += " "
    else:
      index = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
      decoded += LETTERS[index]
  return decoded

def main():
  """Main function for handling transaction processing."""
  manager = TransactionManager()
  result = manager.read_product_code_from_json("test.json")

  result_str = str(result)
  print(result_str)

  encoded_result = encode(result_str)
  print("Encoded Result:", encoded_result)

  decoded_result = decode(encoded_result)
  print("Decoded Result:", decoded_result)

  print("IBAN_FROM:", result.iban_from)
  print("IBAN_TO:", result.iban_to)

if __name__ == "__main__":
  main()
