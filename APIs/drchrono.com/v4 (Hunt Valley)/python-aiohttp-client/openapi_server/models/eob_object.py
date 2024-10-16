# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EOBObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, check_date: str=None, deposit_date: str=None, doctor: int=None, id: int=None, insurance_payer_id: str=None, insurance_payer_name: str=None, insurance_payer_trace_number: str=None, payment_method: str=None, posted_date: str=None, scanned_eob: str=None, total_paid: float=None, updated_at: str=None):
        """EOBObject - a model defined in OpenAPI

        :param check_date: The check_date of this EOBObject.
        :param deposit_date: The deposit_date of this EOBObject.
        :param doctor: The doctor of this EOBObject.
        :param id: The id of this EOBObject.
        :param insurance_payer_id: The insurance_payer_id of this EOBObject.
        :param insurance_payer_name: The insurance_payer_name of this EOBObject.
        :param insurance_payer_trace_number: The insurance_payer_trace_number of this EOBObject.
        :param payment_method: The payment_method of this EOBObject.
        :param posted_date: The posted_date of this EOBObject.
        :param scanned_eob: The scanned_eob of this EOBObject.
        :param total_paid: The total_paid of this EOBObject.
        :param updated_at: The updated_at of this EOBObject.
        """
        self.openapi_types = {
            'check_date': str,
            'deposit_date': str,
            'doctor': int,
            'id': int,
            'insurance_payer_id': str,
            'insurance_payer_name': str,
            'insurance_payer_trace_number': str,
            'payment_method': str,
            'posted_date': str,
            'scanned_eob': str,
            'total_paid': float,
            'updated_at': str
        }

        self.attribute_map = {
            'check_date': 'check_date',
            'deposit_date': 'deposit_date',
            'doctor': 'doctor',
            'id': 'id',
            'insurance_payer_id': 'insurance_payer_id',
            'insurance_payer_name': 'insurance_payer_name',
            'insurance_payer_trace_number': 'insurance_payer_trace_number',
            'payment_method': 'payment_method',
            'posted_date': 'posted_date',
            'scanned_eob': 'scanned_eob',
            'total_paid': 'total_paid',
            'updated_at': 'updated_at'
        }

        self._check_date = check_date
        self._deposit_date = deposit_date
        self._doctor = doctor
        self._id = id
        self._insurance_payer_id = insurance_payer_id
        self._insurance_payer_name = insurance_payer_name
        self._insurance_payer_trace_number = insurance_payer_trace_number
        self._payment_method = payment_method
        self._posted_date = posted_date
        self._scanned_eob = scanned_eob
        self._total_paid = total_paid
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EOBObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EOBObject of this EOBObject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def check_date(self):
        """Gets the check_date of this EOBObject.

        Date of check. If missing, default to the date when the request is made

        :return: The check_date of this EOBObject.
        :rtype: str
        """
        return self._check_date

    @check_date.setter
    def check_date(self, check_date):
        """Sets the check_date of this EOBObject.

        Date of check. If missing, default to the date when the request is made

        :param check_date: The check_date of this EOBObject.
        :type check_date: str
        """

        self._check_date = check_date

    @property
    def deposit_date(self):
        """Gets the deposit_date of this EOBObject.

        Date when EOB gets deposited.

        :return: The deposit_date of this EOBObject.
        :rtype: str
        """
        return self._deposit_date

    @deposit_date.setter
    def deposit_date(self, deposit_date):
        """Sets the deposit_date of this EOBObject.

        Date when EOB gets deposited.

        :param deposit_date: The deposit_date of this EOBObject.
        :type deposit_date: str
        """

        self._deposit_date = deposit_date

    @property
    def doctor(self):
        """Gets the doctor of this EOBObject.

        

        :return: The doctor of this EOBObject.
        :rtype: int
        """
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        """Sets the doctor of this EOBObject.

        

        :param doctor: The doctor of this EOBObject.
        :type doctor: int
        """
        if doctor is None:
            raise ValueError("Invalid value for `doctor`, must not be `None`")

        self._doctor = doctor

    @property
    def id(self):
        """Gets the id of this EOBObject.

        

        :return: The id of this EOBObject.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EOBObject.

        

        :param id: The id of this EOBObject.
        :type id: int
        """

        self._id = id

    @property
    def insurance_payer_id(self):
        """Gets the insurance_payer_id of this EOBObject.

        

        :return: The insurance_payer_id of this EOBObject.
        :rtype: str
        """
        return self._insurance_payer_id

    @insurance_payer_id.setter
    def insurance_payer_id(self, insurance_payer_id):
        """Sets the insurance_payer_id of this EOBObject.

        

        :param insurance_payer_id: The insurance_payer_id of this EOBObject.
        :type insurance_payer_id: str
        """
        if insurance_payer_id is None:
            raise ValueError("Invalid value for `insurance_payer_id`, must not be `None`")

        self._insurance_payer_id = insurance_payer_id

    @property
    def insurance_payer_name(self):
        """Gets the insurance_payer_name of this EOBObject.

        

        :return: The insurance_payer_name of this EOBObject.
        :rtype: str
        """
        return self._insurance_payer_name

    @insurance_payer_name.setter
    def insurance_payer_name(self, insurance_payer_name):
        """Sets the insurance_payer_name of this EOBObject.

        

        :param insurance_payer_name: The insurance_payer_name of this EOBObject.
        :type insurance_payer_name: str
        """
        if insurance_payer_name is None:
            raise ValueError("Invalid value for `insurance_payer_name`, must not be `None`")

        self._insurance_payer_name = insurance_payer_name

    @property
    def insurance_payer_trace_number(self):
        """Gets the insurance_payer_trace_number of this EOBObject.

        

        :return: The insurance_payer_trace_number of this EOBObject.
        :rtype: str
        """
        return self._insurance_payer_trace_number

    @insurance_payer_trace_number.setter
    def insurance_payer_trace_number(self, insurance_payer_trace_number):
        """Sets the insurance_payer_trace_number of this EOBObject.

        

        :param insurance_payer_trace_number: The insurance_payer_trace_number of this EOBObject.
        :type insurance_payer_trace_number: str
        """
        if insurance_payer_trace_number is None:
            raise ValueError("Invalid value for `insurance_payer_trace_number`, must not be `None`")

        self._insurance_payer_trace_number = insurance_payer_trace_number

    @property
    def payment_method(self):
        """Gets the payment_method of this EOBObject.

        `\"\"` - Unknown, `\"ACH\"` - Automated Clearing House (ACH), `\"BOPCCP\"` - Cash Concentration/Disbursement plus Addenda (CCD+) (ACH), `\"BOPCTX\"` - Corporate Trade Exchange (CTX) (ACH), `\"CHK\"` - Check, `\"FWT\"` - Federal Reserve Funds/Wire Transfer - Nonrepetitive, `\"VPAY\"` - vPayment, `\"NON\"` - Non-Payment Data

        :return: The payment_method of this EOBObject.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this EOBObject.

        `\"\"` - Unknown, `\"ACH\"` - Automated Clearing House (ACH), `\"BOPCCP\"` - Cash Concentration/Disbursement plus Addenda (CCD+) (ACH), `\"BOPCTX\"` - Corporate Trade Exchange (CTX) (ACH), `\"CHK\"` - Check, `\"FWT\"` - Federal Reserve Funds/Wire Transfer - Nonrepetitive, `\"VPAY\"` - vPayment, `\"NON\"` - Non-Payment Data

        :param payment_method: The payment_method of this EOBObject.
        :type payment_method: str
        """
        allowed_values = ["", "ACH", "BOPCCP", "BOPCTX", "CHK", "FWT", "VPAY", "NON"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def posted_date(self):
        """Gets the posted_date of this EOBObject.

        

        :return: The posted_date of this EOBObject.
        :rtype: str
        """
        return self._posted_date

    @posted_date.setter
    def posted_date(self, posted_date):
        """Sets the posted_date of this EOBObject.

        

        :param posted_date: The posted_date of this EOBObject.
        :type posted_date: str
        """

        self._posted_date = posted_date

    @property
    def scanned_eob(self):
        """Gets the scanned_eob of this EOBObject.

        

        :return: The scanned_eob of this EOBObject.
        :rtype: str
        """
        return self._scanned_eob

    @scanned_eob.setter
    def scanned_eob(self, scanned_eob):
        """Sets the scanned_eob of this EOBObject.

        

        :param scanned_eob: The scanned_eob of this EOBObject.
        :type scanned_eob: str
        """

        self._scanned_eob = scanned_eob

    @property
    def total_paid(self):
        """Gets the total_paid of this EOBObject.

        Total amount paid. If missing, default to 0.00

        :return: The total_paid of this EOBObject.
        :rtype: float
        """
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        """Sets the total_paid of this EOBObject.

        Total amount paid. If missing, default to 0.00

        :param total_paid: The total_paid of this EOBObject.
        :type total_paid: float
        """

        self._total_paid = total_paid

    @property
    def updated_at(self):
        """Gets the updated_at of this EOBObject.

        

        :return: The updated_at of this EOBObject.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EOBObject.

        

        :param updated_at: The updated_at of this EOBObject.
        :type updated_at: str
        """

        self._updated_at = updated_at
