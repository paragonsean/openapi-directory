# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.client_details_api_model import ClientDetailsApiModel
from openapi_server.models.currency_details_api_model import CurrencyDetailsApiModel
from openapi_server import util


class EstimationDetailsApiModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_token: str=None, client: ClientDetailsApiModel=None, cloned_from_id: int=None, currency: CurrencyDetailsApiModel=None, discount_amount: float=None, expires_on: datetime=None, id: int=None, issued_on: datetime=None, notes: str=None, number: str=None, po_number: str=None, status: str=None, sub_total_amount: float=None, tax_amount: float=None, terms: str=None, total_amount: float=None):
        """EstimationDetailsApiModel - a model defined in OpenAPI

        :param access_token: The access_token of this EstimationDetailsApiModel.
        :param client: The client of this EstimationDetailsApiModel.
        :param cloned_from_id: The cloned_from_id of this EstimationDetailsApiModel.
        :param currency: The currency of this EstimationDetailsApiModel.
        :param discount_amount: The discount_amount of this EstimationDetailsApiModel.
        :param expires_on: The expires_on of this EstimationDetailsApiModel.
        :param id: The id of this EstimationDetailsApiModel.
        :param issued_on: The issued_on of this EstimationDetailsApiModel.
        :param notes: The notes of this EstimationDetailsApiModel.
        :param number: The number of this EstimationDetailsApiModel.
        :param po_number: The po_number of this EstimationDetailsApiModel.
        :param status: The status of this EstimationDetailsApiModel.
        :param sub_total_amount: The sub_total_amount of this EstimationDetailsApiModel.
        :param tax_amount: The tax_amount of this EstimationDetailsApiModel.
        :param terms: The terms of this EstimationDetailsApiModel.
        :param total_amount: The total_amount of this EstimationDetailsApiModel.
        """
        self.openapi_types = {
            'access_token': str,
            'client': ClientDetailsApiModel,
            'cloned_from_id': int,
            'currency': CurrencyDetailsApiModel,
            'discount_amount': float,
            'expires_on': datetime,
            'id': int,
            'issued_on': datetime,
            'notes': str,
            'number': str,
            'po_number': str,
            'status': str,
            'sub_total_amount': float,
            'tax_amount': float,
            'terms': str,
            'total_amount': float
        }

        self.attribute_map = {
            'access_token': 'AccessToken',
            'client': 'Client',
            'cloned_from_id': 'ClonedFromId',
            'currency': 'Currency',
            'discount_amount': 'DiscountAmount',
            'expires_on': 'ExpiresOn',
            'id': 'Id',
            'issued_on': 'IssuedOn',
            'notes': 'Notes',
            'number': 'Number',
            'po_number': 'PoNumber',
            'status': 'Status',
            'sub_total_amount': 'SubTotalAmount',
            'tax_amount': 'TaxAmount',
            'terms': 'Terms',
            'total_amount': 'TotalAmount'
        }

        self._access_token = access_token
        self._client = client
        self._cloned_from_id = cloned_from_id
        self._currency = currency
        self._discount_amount = discount_amount
        self._expires_on = expires_on
        self._id = id
        self._issued_on = issued_on
        self._notes = notes
        self._number = number
        self._po_number = po_number
        self._status = status
        self._sub_total_amount = sub_total_amount
        self._tax_amount = tax_amount
        self._terms = terms
        self._total_amount = total_amount

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EstimationDetailsApiModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EstimationDetailsApiModel of this EstimationDetailsApiModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_token(self):
        """Gets the access_token of this EstimationDetailsApiModel.

        Security access token used for accessing the estimation anonymously

        :return: The access_token of this EstimationDetailsApiModel.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this EstimationDetailsApiModel.

        Security access token used for accessing the estimation anonymously

        :param access_token: The access_token of this EstimationDetailsApiModel.
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def client(self):
        """Gets the client of this EstimationDetailsApiModel.


        :return: The client of this EstimationDetailsApiModel.
        :rtype: ClientDetailsApiModel
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this EstimationDetailsApiModel.


        :param client: The client of this EstimationDetailsApiModel.
        :type client: ClientDetailsApiModel
        """

        self._client = client

    @property
    def cloned_from_id(self):
        """Gets the cloned_from_id of this EstimationDetailsApiModel.

        Indicate from which estimation this estimation has been cloned from

        :return: The cloned_from_id of this EstimationDetailsApiModel.
        :rtype: int
        """
        return self._cloned_from_id

    @cloned_from_id.setter
    def cloned_from_id(self, cloned_from_id):
        """Sets the cloned_from_id of this EstimationDetailsApiModel.

        Indicate from which estimation this estimation has been cloned from

        :param cloned_from_id: The cloned_from_id of this EstimationDetailsApiModel.
        :type cloned_from_id: int
        """

        self._cloned_from_id = cloned_from_id

    @property
    def currency(self):
        """Gets the currency of this EstimationDetailsApiModel.


        :return: The currency of this EstimationDetailsApiModel.
        :rtype: CurrencyDetailsApiModel
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EstimationDetailsApiModel.


        :param currency: The currency of this EstimationDetailsApiModel.
        :type currency: CurrencyDetailsApiModel
        """

        self._currency = currency

    @property
    def discount_amount(self):
        """Gets the discount_amount of this EstimationDetailsApiModel.

        Amount that goes as a discount

        :return: The discount_amount of this EstimationDetailsApiModel.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this EstimationDetailsApiModel.

        Amount that goes as a discount

        :param discount_amount: The discount_amount of this EstimationDetailsApiModel.
        :type discount_amount: float
        """

        self._discount_amount = discount_amount

    @property
    def expires_on(self):
        """Gets the expires_on of this EstimationDetailsApiModel.

        Indicates when the estimation will be proclamed as due

        :return: The expires_on of this EstimationDetailsApiModel.
        :rtype: datetime
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """Sets the expires_on of this EstimationDetailsApiModel.

        Indicates when the estimation will be proclamed as due

        :param expires_on: The expires_on of this EstimationDetailsApiModel.
        :type expires_on: datetime
        """

        self._expires_on = expires_on

    @property
    def id(self):
        """Gets the id of this EstimationDetailsApiModel.

        Estimation id

        :return: The id of this EstimationDetailsApiModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EstimationDetailsApiModel.

        Estimation id

        :param id: The id of this EstimationDetailsApiModel.
        :type id: int
        """

        self._id = id

    @property
    def issued_on(self):
        """Gets the issued_on of this EstimationDetailsApiModel.

        Indicates when the estimation was issued

        :return: The issued_on of this EstimationDetailsApiModel.
        :rtype: datetime
        """
        return self._issued_on

    @issued_on.setter
    def issued_on(self, issued_on):
        """Sets the issued_on of this EstimationDetailsApiModel.

        Indicates when the estimation was issued

        :param issued_on: The issued_on of this EstimationDetailsApiModel.
        :type issued_on: datetime
        """

        self._issued_on = issued_on

    @property
    def notes(self):
        """Gets the notes of this EstimationDetailsApiModel.

        Internal note regarding the estimation

        :return: The notes of this EstimationDetailsApiModel.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EstimationDetailsApiModel.

        Internal note regarding the estimation

        :param notes: The notes of this EstimationDetailsApiModel.
        :type notes: str
        """

        self._notes = notes

    @property
    def number(self):
        """Gets the number of this EstimationDetailsApiModel.

        Unique estimation number

        :return: The number of this EstimationDetailsApiModel.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this EstimationDetailsApiModel.

        Unique estimation number

        :param number: The number of this EstimationDetailsApiModel.
        :type number: str
        """

        self._number = number

    @property
    def po_number(self):
        """Gets the po_number of this EstimationDetailsApiModel.

        Unique number generated by the buyer

        :return: The po_number of this EstimationDetailsApiModel.
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this EstimationDetailsApiModel.

        Unique number generated by the buyer

        :param po_number: The po_number of this EstimationDetailsApiModel.
        :type po_number: str
        """

        self._po_number = po_number

    @property
    def status(self):
        """Gets the status of this EstimationDetailsApiModel.

        Indicate the status of the estimation (paid/unpaid/overdue)

        :return: The status of this EstimationDetailsApiModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EstimationDetailsApiModel.

        Indicate the status of the estimation (paid/unpaid/overdue)

        :param status: The status of this EstimationDetailsApiModel.
        :type status: str
        """
        allowed_values = ["Draft", "Accepted", "Rejected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def sub_total_amount(self):
        """Gets the sub_total_amount of this EstimationDetailsApiModel.

        Total amount of the estimation without tax

        :return: The sub_total_amount of this EstimationDetailsApiModel.
        :rtype: float
        """
        return self._sub_total_amount

    @sub_total_amount.setter
    def sub_total_amount(self, sub_total_amount):
        """Sets the sub_total_amount of this EstimationDetailsApiModel.

        Total amount of the estimation without tax

        :param sub_total_amount: The sub_total_amount of this EstimationDetailsApiModel.
        :type sub_total_amount: float
        """

        self._sub_total_amount = sub_total_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this EstimationDetailsApiModel.

        Amount that goes to the tax

        :return: The tax_amount of this EstimationDetailsApiModel.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this EstimationDetailsApiModel.

        Amount that goes to the tax

        :param tax_amount: The tax_amount of this EstimationDetailsApiModel.
        :type tax_amount: float
        """

        self._tax_amount = tax_amount

    @property
    def terms(self):
        """Gets the terms of this EstimationDetailsApiModel.

        Terms of agreement

        :return: The terms of this EstimationDetailsApiModel.
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this EstimationDetailsApiModel.

        Terms of agreement

        :param terms: The terms of this EstimationDetailsApiModel.
        :type terms: str
        """

        self._terms = terms

    @property
    def total_amount(self):
        """Gets the total_amount of this EstimationDetailsApiModel.

        Total amount of the estimation with tax

        :return: The total_amount of this EstimationDetailsApiModel.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this EstimationDetailsApiModel.

        Total amount of the estimation with tax

        :param total_amount: The total_amount of this EstimationDetailsApiModel.
        :type total_amount: float
        """

        self._total_amount = total_amount
