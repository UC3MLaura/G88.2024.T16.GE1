"""
Module for handling transaction requests.
"""

import json
from datetime import datetime

class TransactionRequest:
  """Represents a transaction request with IBAN details and timestamps."""

  def __init__(self, iban_from, iban_to, receptor_name):
    """
        Initializes a transaction request.

        Args:
            iban_from (str): The sender's IBAN.
            iban_to (str): The receiver's IBAN.
            receptor_name (str): The receiver's name.
    """
    self._receptor_name = receptor_name
    self._iban_from = iban_from
    self._iban_to = iban_to
    self._timestamp = datetime.timestamp(datetime.utcnow())

  def __str__(self):
    """Returns a string representation of the transaction request."""
    return "TransactionRequest: " + json.dumps(self.__dict__)

  @property
  def receptor_name(self):
    """Getter for receptor name."""
    return self._receptor_name

  @receptor_name.setter
  def receptor_name(self, value):
    """Setter for receptor name."""
    self._receptor_name = value

  @property
  def iban_from(self):
    """Getter for sender's IBAN."""
    return self._iban_from

  @iban_from.setter
  def iban_from(self, value):
    """Setter for sender's IBAN."""
    self._iban_from = value

  @property
  def iban_to(self):
    """Getter for receiver's IBAN."""
    return self._iban_to

  @iban_to.setter
  def iban_to(self, value):
    """Setter for receiver's IBAN."""
    self._iban_to = value
