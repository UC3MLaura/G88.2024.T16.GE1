"""
Module for handling transaction management exceptions.
"""

class TransactionManagementException(Exception):
  """Custom exception for transaction management errors."""

  def __init__(self, message):
    self._message = message
    super().__init__(self.message)

  @property
  def message(self):
    """Getter for the exception message."""
    return self._message

  @message.setter
  def message(self, value):
    """Setter for the exception message."""
    self._message = value
