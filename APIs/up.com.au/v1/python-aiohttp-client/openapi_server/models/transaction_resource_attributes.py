# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.cashback_object import CashbackObject
from openapi_server.models.hold_info_object import HoldInfoObject
from openapi_server.models.money_object import MoneyObject
from openapi_server.models.round_up_object import RoundUpObject
from openapi_server.models.transaction_status_enum import TransactionStatusEnum
from openapi_server import util


class TransactionResourceAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: MoneyObject=None, cashback: CashbackObject=None, created_at: datetime=None, description: str=None, foreign_amount: MoneyObject=None, hold_info: HoldInfoObject=None, is_categorizable: bool=None, message: str=None, raw_text: str=None, round_up: RoundUpObject=None, settled_at: datetime=None, status: TransactionStatusEnum=None):
        """TransactionResourceAttributes - a model defined in OpenAPI

        :param amount: The amount of this TransactionResourceAttributes.
        :param cashback: The cashback of this TransactionResourceAttributes.
        :param created_at: The created_at of this TransactionResourceAttributes.
        :param description: The description of this TransactionResourceAttributes.
        :param foreign_amount: The foreign_amount of this TransactionResourceAttributes.
        :param hold_info: The hold_info of this TransactionResourceAttributes.
        :param is_categorizable: The is_categorizable of this TransactionResourceAttributes.
        :param message: The message of this TransactionResourceAttributes.
        :param raw_text: The raw_text of this TransactionResourceAttributes.
        :param round_up: The round_up of this TransactionResourceAttributes.
        :param settled_at: The settled_at of this TransactionResourceAttributes.
        :param status: The status of this TransactionResourceAttributes.
        """
        self.openapi_types = {
            'amount': MoneyObject,
            'cashback': CashbackObject,
            'created_at': datetime,
            'description': str,
            'foreign_amount': MoneyObject,
            'hold_info': HoldInfoObject,
            'is_categorizable': bool,
            'message': str,
            'raw_text': str,
            'round_up': RoundUpObject,
            'settled_at': datetime,
            'status': TransactionStatusEnum
        }

        self.attribute_map = {
            'amount': 'amount',
            'cashback': 'cashback',
            'created_at': 'createdAt',
            'description': 'description',
            'foreign_amount': 'foreignAmount',
            'hold_info': 'holdInfo',
            'is_categorizable': 'isCategorizable',
            'message': 'message',
            'raw_text': 'rawText',
            'round_up': 'roundUp',
            'settled_at': 'settledAt',
            'status': 'status'
        }

        self._amount = amount
        self._cashback = cashback
        self._created_at = created_at
        self._description = description
        self._foreign_amount = foreign_amount
        self._hold_info = hold_info
        self._is_categorizable = is_categorizable
        self._message = message
        self._raw_text = raw_text
        self._round_up = round_up
        self._settled_at = settled_at
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TransactionResourceAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TransactionResource_attributes of this TransactionResourceAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this TransactionResourceAttributes.

        The amount of this transaction in Australian dollars. For transactions that were once `HELD` but are now `SETTLED`, refer to the `holdInfo` field for the original `amount` the transaction was `HELD` at. 

        :return: The amount of this TransactionResourceAttributes.
        :rtype: MoneyObject
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionResourceAttributes.

        The amount of this transaction in Australian dollars. For transactions that were once `HELD` but are now `SETTLED`, refer to the `holdInfo` field for the original `amount` the transaction was `HELD` at. 

        :param amount: The amount of this TransactionResourceAttributes.
        :type amount: MoneyObject
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")

        self._amount = amount

    @property
    def cashback(self):
        """Gets the cashback of this TransactionResourceAttributes.

        If all or part of this transaction was instantly reimbursed in the form of cashback, details of the reimbursement. 

        :return: The cashback of this TransactionResourceAttributes.
        :rtype: CashbackObject
        """
        return self._cashback

    @cashback.setter
    def cashback(self, cashback):
        """Sets the cashback of this TransactionResourceAttributes.

        If all or part of this transaction was instantly reimbursed in the form of cashback, details of the reimbursement. 

        :param cashback: The cashback of this TransactionResourceAttributes.
        :type cashback: CashbackObject
        """
        if cashback is None:
            raise ValueError("Invalid value for `cashback`, must not be `None`")

        self._cashback = cashback

    @property
    def created_at(self):
        """Gets the created_at of this TransactionResourceAttributes.

        The date-time at which this transaction was first encountered. 

        :return: The created_at of this TransactionResourceAttributes.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransactionResourceAttributes.

        The date-time at which this transaction was first encountered. 

        :param created_at: The created_at of this TransactionResourceAttributes.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this TransactionResourceAttributes.

        A short description for this transaction. Usually the merchant name for purchases. 

        :return: The description of this TransactionResourceAttributes.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionResourceAttributes.

        A short description for this transaction. Usually the merchant name for purchases. 

        :param description: The description of this TransactionResourceAttributes.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def foreign_amount(self):
        """Gets the foreign_amount of this TransactionResourceAttributes.

        The foreign currency amount of this transaction. This field will be `null` for domestic transactions. The amount was converted to the AUD amount reflected in the `amount` of this transaction. Refer to the `holdInfo` field for the original `foreignAmount` the transaction was `HELD` at. 

        :return: The foreign_amount of this TransactionResourceAttributes.
        :rtype: MoneyObject
        """
        return self._foreign_amount

    @foreign_amount.setter
    def foreign_amount(self, foreign_amount):
        """Sets the foreign_amount of this TransactionResourceAttributes.

        The foreign currency amount of this transaction. This field will be `null` for domestic transactions. The amount was converted to the AUD amount reflected in the `amount` of this transaction. Refer to the `holdInfo` field for the original `foreignAmount` the transaction was `HELD` at. 

        :param foreign_amount: The foreign_amount of this TransactionResourceAttributes.
        :type foreign_amount: MoneyObject
        """
        if foreign_amount is None:
            raise ValueError("Invalid value for `foreign_amount`, must not be `None`")

        self._foreign_amount = foreign_amount

    @property
    def hold_info(self):
        """Gets the hold_info of this TransactionResourceAttributes.

        If this transaction is currently in the `HELD` status, or was ever in the `HELD` status, the `amount` and `foreignAmount` of the transaction while `HELD`. 

        :return: The hold_info of this TransactionResourceAttributes.
        :rtype: HoldInfoObject
        """
        return self._hold_info

    @hold_info.setter
    def hold_info(self, hold_info):
        """Sets the hold_info of this TransactionResourceAttributes.

        If this transaction is currently in the `HELD` status, or was ever in the `HELD` status, the `amount` and `foreignAmount` of the transaction while `HELD`. 

        :param hold_info: The hold_info of this TransactionResourceAttributes.
        :type hold_info: HoldInfoObject
        """
        if hold_info is None:
            raise ValueError("Invalid value for `hold_info`, must not be `None`")

        self._hold_info = hold_info

    @property
    def is_categorizable(self):
        """Gets the is_categorizable of this TransactionResourceAttributes.

        Boolean flag set to true on transactions that support the use of categories. 

        :return: The is_categorizable of this TransactionResourceAttributes.
        :rtype: bool
        """
        return self._is_categorizable

    @is_categorizable.setter
    def is_categorizable(self, is_categorizable):
        """Sets the is_categorizable of this TransactionResourceAttributes.

        Boolean flag set to true on transactions that support the use of categories. 

        :param is_categorizable: The is_categorizable of this TransactionResourceAttributes.
        :type is_categorizable: bool
        """
        if is_categorizable is None:
            raise ValueError("Invalid value for `is_categorizable`, must not be `None`")

        self._is_categorizable = is_categorizable

    @property
    def message(self):
        """Gets the message of this TransactionResourceAttributes.

        Attached message for this transaction, such as a payment message, or a transfer note. 

        :return: The message of this TransactionResourceAttributes.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TransactionResourceAttributes.

        Attached message for this transaction, such as a payment message, or a transfer note. 

        :param message: The message of this TransactionResourceAttributes.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def raw_text(self):
        """Gets the raw_text of this TransactionResourceAttributes.

        The original, unprocessed text of the transaction. This is often not a perfect indicator of the actual merchant, but it is useful for reconciliation purposes in some cases. 

        :return: The raw_text of this TransactionResourceAttributes.
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this TransactionResourceAttributes.

        The original, unprocessed text of the transaction. This is often not a perfect indicator of the actual merchant, but it is useful for reconciliation purposes in some cases. 

        :param raw_text: The raw_text of this TransactionResourceAttributes.
        :type raw_text: str
        """
        if raw_text is None:
            raise ValueError("Invalid value for `raw_text`, must not be `None`")

        self._raw_text = raw_text

    @property
    def round_up(self):
        """Gets the round_up of this TransactionResourceAttributes.

        Details of how this transaction was rounded-up. If no Round Up was applied this field will be `null`. 

        :return: The round_up of this TransactionResourceAttributes.
        :rtype: RoundUpObject
        """
        return self._round_up

    @round_up.setter
    def round_up(self, round_up):
        """Sets the round_up of this TransactionResourceAttributes.

        Details of how this transaction was rounded-up. If no Round Up was applied this field will be `null`. 

        :param round_up: The round_up of this TransactionResourceAttributes.
        :type round_up: RoundUpObject
        """
        if round_up is None:
            raise ValueError("Invalid value for `round_up`, must not be `None`")

        self._round_up = round_up

    @property
    def settled_at(self):
        """Gets the settled_at of this TransactionResourceAttributes.

        The date-time at which this transaction settled. This field will be `null` for transactions that are currently in the `HELD` status. 

        :return: The settled_at of this TransactionResourceAttributes.
        :rtype: datetime
        """
        return self._settled_at

    @settled_at.setter
    def settled_at(self, settled_at):
        """Sets the settled_at of this TransactionResourceAttributes.

        The date-time at which this transaction settled. This field will be `null` for transactions that are currently in the `HELD` status. 

        :param settled_at: The settled_at of this TransactionResourceAttributes.
        :type settled_at: datetime
        """
        if settled_at is None:
            raise ValueError("Invalid value for `settled_at`, must not be `None`")

        self._settled_at = settled_at

    @property
    def status(self):
        """Gets the status of this TransactionResourceAttributes.

        The current processing status of this transaction, according to whether or not this transaction has settled or is still held. 

        :return: The status of this TransactionResourceAttributes.
        :rtype: TransactionStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransactionResourceAttributes.

        The current processing status of this transaction, according to whether or not this transaction has settled or is still held. 

        :param status: The status of this TransactionResourceAttributes.
        :type status: TransactionStatusEnum
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status
