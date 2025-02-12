"""
This module imports the necessary classes for transaction management.

It includes:
- `TransactionRequest`: Represents a transaction request with IBAN details.
- `TransactionManager`: Handles transaction processing, including IBAN validation
  and JSON data extraction.
- `TransactionManagementException`: Custom exception class for handling transaction errors.
"""

from uc3m_money.transaction_request import TransactionRequest
from uc3m_money.transaction_management_exception import TransactionManagementException
from uc3m_money.transaction_manager import TransactionManager
