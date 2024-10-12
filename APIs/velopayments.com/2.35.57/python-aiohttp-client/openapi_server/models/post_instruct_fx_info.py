# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PostInstructFxInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fx_mode: str=None, fx_status: str=None, fx_status_updated_at: datetime=None, fx_transaction_reference: str=None):
        """PostInstructFxInfo - a model defined in OpenAPI

        :param fx_mode: The fx_mode of this PostInstructFxInfo.
        :param fx_status: The fx_status of this PostInstructFxInfo.
        :param fx_status_updated_at: The fx_status_updated_at of this PostInstructFxInfo.
        :param fx_transaction_reference: The fx_transaction_reference of this PostInstructFxInfo.
        """
        self.openapi_types = {
            'fx_mode': str,
            'fx_status': str,
            'fx_status_updated_at': datetime,
            'fx_transaction_reference': str
        }

        self.attribute_map = {
            'fx_mode': 'fxMode',
            'fx_status': 'fxStatus',
            'fx_status_updated_at': 'fxStatusUpdatedAt',
            'fx_transaction_reference': 'fxTransactionReference'
        }

        self._fx_mode = fx_mode
        self._fx_status = fx_status
        self._fx_status_updated_at = fx_status_updated_at
        self._fx_transaction_reference = fx_transaction_reference

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PostInstructFxInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PostInstructFxInfo of this PostInstructFxInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fx_mode(self):
        """Gets the fx_mode of this PostInstructFxInfo.

        The mode by which the FX rate is to be determined (MANUAL or AUTO)

        :return: The fx_mode of this PostInstructFxInfo.
        :rtype: str
        """
        return self._fx_mode

    @fx_mode.setter
    def fx_mode(self, fx_mode):
        """Sets the fx_mode of this PostInstructFxInfo.

        The mode by which the FX rate is to be determined (MANUAL or AUTO)

        :param fx_mode: The fx_mode of this PostInstructFxInfo.
        :type fx_mode: str
        """
        if fx_mode is None:
            raise ValueError("Invalid value for `fx_mode`, must not be `None`")

        self._fx_mode = fx_mode

    @property
    def fx_status(self):
        """Gets the fx_status of this PostInstructFxInfo.

        The state to which the Post-Instruct FX process has reached (INITIATED or COMPLETED)

        :return: The fx_status of this PostInstructFxInfo.
        :rtype: str
        """
        return self._fx_status

    @fx_status.setter
    def fx_status(self, fx_status):
        """Sets the fx_status of this PostInstructFxInfo.

        The state to which the Post-Instruct FX process has reached (INITIATED or COMPLETED)

        :param fx_status: The fx_status of this PostInstructFxInfo.
        :type fx_status: str
        """
        if fx_status is None:
            raise ValueError("Invalid value for `fx_status`, must not be `None`")

        self._fx_status = fx_status

    @property
    def fx_status_updated_at(self):
        """Gets the fx_status_updated_at of this PostInstructFxInfo.

        The date-time at which the most recent fxStatus was determined.

        :return: The fx_status_updated_at of this PostInstructFxInfo.
        :rtype: datetime
        """
        return self._fx_status_updated_at

    @fx_status_updated_at.setter
    def fx_status_updated_at(self, fx_status_updated_at):
        """Sets the fx_status_updated_at of this PostInstructFxInfo.

        The date-time at which the most recent fxStatus was determined.

        :param fx_status_updated_at: The fx_status_updated_at of this PostInstructFxInfo.
        :type fx_status_updated_at: datetime
        """
        if fx_status_updated_at is None:
            raise ValueError("Invalid value for `fx_status_updated_at`, must not be `None`")

        self._fx_status_updated_at = fx_status_updated_at

    @property
    def fx_transaction_reference(self):
        """Gets the fx_transaction_reference of this PostInstructFxInfo.

        The reference assigned to the FX funding that will fulfil this payment.

        :return: The fx_transaction_reference of this PostInstructFxInfo.
        :rtype: str
        """
        return self._fx_transaction_reference

    @fx_transaction_reference.setter
    def fx_transaction_reference(self, fx_transaction_reference):
        """Sets the fx_transaction_reference of this PostInstructFxInfo.

        The reference assigned to the FX funding that will fulfil this payment.

        :param fx_transaction_reference: The fx_transaction_reference of this PostInstructFxInfo.
        :type fx_transaction_reference: str
        """

        self._fx_transaction_reference = fx_transaction_reference
