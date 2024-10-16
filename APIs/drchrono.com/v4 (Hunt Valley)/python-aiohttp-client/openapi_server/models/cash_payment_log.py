# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CashPaymentLog(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action: str=None, amount: float=None, appointment: str=None, created_by: str=None, doctor: str=None, id: int=None, patient: str=None, payment_method: str=None, source: str=None, updated_at: str=None):
        """CashPaymentLog - a model defined in OpenAPI

        :param action: The action of this CashPaymentLog.
        :param amount: The amount of this CashPaymentLog.
        :param appointment: The appointment of this CashPaymentLog.
        :param created_by: The created_by of this CashPaymentLog.
        :param doctor: The doctor of this CashPaymentLog.
        :param id: The id of this CashPaymentLog.
        :param patient: The patient of this CashPaymentLog.
        :param payment_method: The payment_method of this CashPaymentLog.
        :param source: The source of this CashPaymentLog.
        :param updated_at: The updated_at of this CashPaymentLog.
        """
        self.openapi_types = {
            'action': str,
            'amount': float,
            'appointment': str,
            'created_by': str,
            'doctor': str,
            'id': int,
            'patient': str,
            'payment_method': str,
            'source': str,
            'updated_at': str
        }

        self.attribute_map = {
            'action': 'action',
            'amount': 'amount',
            'appointment': 'appointment',
            'created_by': 'created_by',
            'doctor': 'doctor',
            'id': 'id',
            'patient': 'patient',
            'payment_method': 'payment_method',
            'source': 'source',
            'updated_at': 'updated_at'
        }

        self._action = action
        self._amount = amount
        self._appointment = appointment
        self._created_by = created_by
        self._doctor = doctor
        self._id = id
        self._patient = patient
        self._payment_method = payment_method
        self._source = source
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CashPaymentLog':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CashPaymentLog of this CashPaymentLog.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self):
        """Gets the action of this CashPaymentLog.

        `C`(Create), `U`(Update), `D`(Delete), `F`(Fill), `A`(Autofill)

        :return: The action of this CashPaymentLog.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CashPaymentLog.

        `C`(Create), `U`(Update), `D`(Delete), `F`(Fill), `A`(Autofill)

        :param action: The action of this CashPaymentLog.
        :type action: str
        """
        allowed_values = ["C", "U", "D", "F", "A"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def amount(self):
        """Gets the amount of this CashPaymentLog.

        

        :return: The amount of this CashPaymentLog.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CashPaymentLog.

        

        :param amount: The amount of this CashPaymentLog.
        :type amount: float
        """

        self._amount = amount

    @property
    def appointment(self):
        """Gets the appointment of this CashPaymentLog.

        ID of appointment associated with the payment

        :return: The appointment of this CashPaymentLog.
        :rtype: str
        """
        return self._appointment

    @appointment.setter
    def appointment(self, appointment):
        """Sets the appointment of this CashPaymentLog.

        ID of appointment associated with the payment

        :param appointment: The appointment of this CashPaymentLog.
        :type appointment: str
        """

        self._appointment = appointment

    @property
    def created_by(self):
        """Gets the created_by of this CashPaymentLog.

        ID of user who created the payment

        :return: The created_by of this CashPaymentLog.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CashPaymentLog.

        ID of user who created the payment

        :param created_by: The created_by of this CashPaymentLog.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def doctor(self):
        """Gets the doctor of this CashPaymentLog.

        

        :return: The doctor of this CashPaymentLog.
        :rtype: str
        """
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        """Sets the doctor of this CashPaymentLog.

        

        :param doctor: The doctor of this CashPaymentLog.
        :type doctor: str
        """

        self._doctor = doctor

    @property
    def id(self):
        """Gets the id of this CashPaymentLog.

        

        :return: The id of this CashPaymentLog.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CashPaymentLog.

        

        :param id: The id of this CashPaymentLog.
        :type id: int
        """

        self._id = id

    @property
    def patient(self):
        """Gets the patient of this CashPaymentLog.

        

        :return: The patient of this CashPaymentLog.
        :rtype: str
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this CashPaymentLog.

        

        :param patient: The patient of this CashPaymentLog.
        :type patient: str
        """

        self._patient = patient

    @property
    def payment_method(self):
        """Gets the payment_method of this CashPaymentLog.

        `\"CASH\", \"CHCK\" for Check, \"DBIT\" for Debit, \"CRDT\" for Credit Card, \"AMEX\" for American Express, \"VISA\", \"MSTR\" for Mastercard, \"DISC\" for Discover, \"SQR1\" for Square (legacy), \"SQRE\" for Square, \"PTPA\" for Patient Payments, \"ONPT\" for onpatient, \"OTHR\" for Other`

        :return: The payment_method of this CashPaymentLog.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this CashPaymentLog.

        `\"CASH\", \"CHCK\" for Check, \"DBIT\" for Debit, \"CRDT\" for Credit Card, \"AMEX\" for American Express, \"VISA\", \"MSTR\" for Mastercard, \"DISC\" for Discover, \"SQR1\" for Square (legacy), \"SQRE\" for Square, \"PTPA\" for Patient Payments, \"ONPT\" for onpatient, \"OTHR\" for Other`

        :param payment_method: The payment_method of this CashPaymentLog.
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
    def source(self):
        """Gets the source of this CashPaymentLog.

        

        :return: The source of this CashPaymentLog.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CashPaymentLog.

        

        :param source: The source of this CashPaymentLog.
        :type source: str
        """

        self._source = source

    @property
    def updated_at(self):
        """Gets the updated_at of this CashPaymentLog.

        

        :return: The updated_at of this CashPaymentLog.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CashPaymentLog.

        

        :param updated_at: The updated_at of this CashPaymentLog.
        :type updated_at: str
        """

        self._updated_at = updated_at
