# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CashPayment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: float=None, appointment: int=None, created_at: str=None, created_by: str=None, doctor: int=None, id: int=None, line_item: int=None, notes: str=None, patient: int=None, payment_method: str=None, payment_transaction_type: str=None, posted_date: str=None, received_date: str=None, trace_number: str=None, updated_at: str=None):
        """CashPayment - a model defined in OpenAPI

        :param amount: The amount of this CashPayment.
        :param appointment: The appointment of this CashPayment.
        :param created_at: The created_at of this CashPayment.
        :param created_by: The created_by of this CashPayment.
        :param doctor: The doctor of this CashPayment.
        :param id: The id of this CashPayment.
        :param line_item: The line_item of this CashPayment.
        :param notes: The notes of this CashPayment.
        :param patient: The patient of this CashPayment.
        :param payment_method: The payment_method of this CashPayment.
        :param payment_transaction_type: The payment_transaction_type of this CashPayment.
        :param posted_date: The posted_date of this CashPayment.
        :param received_date: The received_date of this CashPayment.
        :param trace_number: The trace_number of this CashPayment.
        :param updated_at: The updated_at of this CashPayment.
        """
        self.openapi_types = {
            'amount': float,
            'appointment': int,
            'created_at': str,
            'created_by': str,
            'doctor': int,
            'id': int,
            'line_item': int,
            'notes': str,
            'patient': int,
            'payment_method': str,
            'payment_transaction_type': str,
            'posted_date': str,
            'received_date': str,
            'trace_number': str,
            'updated_at': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'appointment': 'appointment',
            'created_at': 'created_at',
            'created_by': 'created_by',
            'doctor': 'doctor',
            'id': 'id',
            'line_item': 'line_item',
            'notes': 'notes',
            'patient': 'patient',
            'payment_method': 'payment_method',
            'payment_transaction_type': 'payment_transaction_type',
            'posted_date': 'posted_date',
            'received_date': 'received_date',
            'trace_number': 'trace_number',
            'updated_at': 'updated_at'
        }

        self._amount = amount
        self._appointment = appointment
        self._created_at = created_at
        self._created_by = created_by
        self._doctor = doctor
        self._id = id
        self._line_item = line_item
        self._notes = notes
        self._patient = patient
        self._payment_method = payment_method
        self._payment_transaction_type = payment_transaction_type
        self._posted_date = posted_date
        self._received_date = received_date
        self._trace_number = trace_number
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CashPayment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CashPayment of this CashPayment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this CashPayment.

        Amount of cash for this payment, cannot be zero

        :return: The amount of this CashPayment.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CashPayment.

        Amount of cash for this payment, cannot be zero

        :param amount: The amount of this CashPayment.
        :type amount: float
        """

        self._amount = amount

    @property
    def appointment(self):
        """Gets the appointment of this CashPayment.

        If this is absent, the apponitment will be inferred from line item

        :return: The appointment of this CashPayment.
        :rtype: int
        """
        return self._appointment

    @appointment.setter
    def appointment(self, appointment):
        """Sets the appointment of this CashPayment.

        If this is absent, the apponitment will be inferred from line item

        :param appointment: The appointment of this CashPayment.
        :type appointment: int
        """

        self._appointment = appointment

    @property
    def created_at(self):
        """Gets the created_at of this CashPayment.

        

        :return: The created_at of this CashPayment.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CashPayment.

        

        :param created_at: The created_at of this CashPayment.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this CashPayment.

        

        :return: The created_by of this CashPayment.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CashPayment.

        

        :param created_by: The created_by of this CashPayment.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def doctor(self):
        """Gets the doctor of this CashPayment.

        

        :return: The doctor of this CashPayment.
        :rtype: int
        """
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        """Sets the doctor of this CashPayment.

        

        :param doctor: The doctor of this CashPayment.
        :type doctor: int
        """

        self._doctor = doctor

    @property
    def id(self):
        """Gets the id of this CashPayment.

        

        :return: The id of this CashPayment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CashPayment.

        

        :param id: The id of this CashPayment.
        :type id: int
        """

        self._id = id

    @property
    def line_item(self):
        """Gets the line_item of this CashPayment.

        

        :return: The line_item of this CashPayment.
        :rtype: int
        """
        return self._line_item

    @line_item.setter
    def line_item(self, line_item):
        """Sets the line_item of this CashPayment.

        

        :param line_item: The line_item of this CashPayment.
        :type line_item: int
        """

        self._line_item = line_item

    @property
    def notes(self):
        """Gets the notes of this CashPayment.

        

        :return: The notes of this CashPayment.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CashPayment.

        

        :param notes: The notes of this CashPayment.
        :type notes: str
        """

        self._notes = notes

    @property
    def patient(self):
        """Gets the patient of this CashPayment.

        

        :return: The patient of this CashPayment.
        :rtype: int
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this CashPayment.

        

        :param patient: The patient of this CashPayment.
        :type patient: int
        """
        if patient is None:
            raise ValueError("Invalid value for `patient`, must not be `None`")

        self._patient = patient

    @property
    def payment_method(self):
        """Gets the payment_method of this CashPayment.

        `\"CASH\", \"CHCK\" for Check, \"DBIT\" for Debit, \"CRDT\" for Credit Card, \"AMEX\" for American Express, \"VISA\", \"MSTR\" for Mastercard, \"DISC\" for Discover, \"SQR1\" for Square (legacy), \"SQRE\" for Square, \"PTPA\" for Patient Payments, \"ONPT\" for onpatient, \"OTHR\" for Other`

        :return: The payment_method of this CashPayment.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this CashPayment.

        `\"CASH\", \"CHCK\" for Check, \"DBIT\" for Debit, \"CRDT\" for Credit Card, \"AMEX\" for American Express, \"VISA\", \"MSTR\" for Mastercard, \"DISC\" for Discover, \"SQR1\" for Square (legacy), \"SQRE\" for Square, \"PTPA\" for Patient Payments, \"ONPT\" for onpatient, \"OTHR\" for Other`

        :param payment_method: The payment_method of this CashPayment.
        :type payment_method: str
        """
        allowed_values = ["CASH", "CHCK", "DBIT", "CRDT", "AMEX", "VISA", "MSTR", "DISC", "SQR1", "SQRE", "PTPA", "ONPT", "OTHR"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def payment_transaction_type(self):
        """Gets the payment_transaction_type of this CashPayment.

        `\"\" for Credit, \"REF\" for Refund, \"COR\" for Correction, \"COPAY\" for Copay, \"COINSR\" for Coinsurance, \"OTHR\" for Other`

        :return: The payment_transaction_type of this CashPayment.
        :rtype: str
        """
        return self._payment_transaction_type

    @payment_transaction_type.setter
    def payment_transaction_type(self, payment_transaction_type):
        """Sets the payment_transaction_type of this CashPayment.

        `\"\" for Credit, \"REF\" for Refund, \"COR\" for Correction, \"COPAY\" for Copay, \"COINSR\" for Coinsurance, \"OTHR\" for Other`

        :param payment_transaction_type: The payment_transaction_type of this CashPayment.
        :type payment_transaction_type: str
        """
        allowed_values = ["", "REF", "COR", "COPAY", "COINSR", "OTHR"]  # noqa: E501
        if payment_transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_transaction_type` ({0}), must be one of {1}"
                .format(payment_transaction_type, allowed_values)
            )

        self._payment_transaction_type = payment_transaction_type

    @property
    def posted_date(self):
        """Gets the posted_date of this CashPayment.

        

        :return: The posted_date of this CashPayment.
        :rtype: str
        """
        return self._posted_date

    @posted_date.setter
    def posted_date(self, posted_date):
        """Sets the posted_date of this CashPayment.

        

        :param posted_date: The posted_date of this CashPayment.
        :type posted_date: str
        """

        self._posted_date = posted_date

    @property
    def received_date(self):
        """Gets the received_date of this CashPayment.

        

        :return: The received_date of this CashPayment.
        :rtype: str
        """
        return self._received_date

    @received_date.setter
    def received_date(self, received_date):
        """Sets the received_date of this CashPayment.

        

        :param received_date: The received_date of this CashPayment.
        :type received_date: str
        """

        self._received_date = received_date

    @property
    def trace_number(self):
        """Gets the trace_number of this CashPayment.

        

        :return: The trace_number of this CashPayment.
        :rtype: str
        """
        return self._trace_number

    @trace_number.setter
    def trace_number(self, trace_number):
        """Sets the trace_number of this CashPayment.

        

        :param trace_number: The trace_number of this CashPayment.
        :type trace_number: str
        """

        self._trace_number = trace_number

    @property
    def updated_at(self):
        """Gets the updated_at of this CashPayment.

        

        :return: The updated_at of this CashPayment.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CashPayment.

        

        :param updated_at: The updated_at of this CashPayment.
        :type updated_at: str
        """

        self._updated_at = updated_at
