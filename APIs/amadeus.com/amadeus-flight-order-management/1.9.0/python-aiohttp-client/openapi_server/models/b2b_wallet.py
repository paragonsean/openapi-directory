# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.reporting_data import ReportingData
from openapi_server.models.virtual_credit_card_details import VirtualCreditCardDetails
import re
from openapi_server import util


class B2bWallet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, card_friendly_name: str=None, card_id: str=None, card_usage_name: str=None, flight_offer_ids: List[str]=None, reporting_data: List[ReportingData]=None, virtual_credit_card_details: VirtualCreditCardDetails=None):
        """B2bWallet - a model defined in OpenAPI

        :param card_friendly_name: The card_friendly_name of this B2bWallet.
        :param card_id: The card_id of this B2bWallet.
        :param card_usage_name: The card_usage_name of this B2bWallet.
        :param flight_offer_ids: The flight_offer_ids of this B2bWallet.
        :param reporting_data: The reporting_data of this B2bWallet.
        :param virtual_credit_card_details: The virtual_credit_card_details of this B2bWallet.
        """
        self.openapi_types = {
            'card_friendly_name': str,
            'card_id': str,
            'card_usage_name': str,
            'flight_offer_ids': List[str],
            'reporting_data': List[ReportingData],
            'virtual_credit_card_details': VirtualCreditCardDetails
        }

        self.attribute_map = {
            'card_friendly_name': 'cardFriendlyName',
            'card_id': 'cardId',
            'card_usage_name': 'cardUsageName',
            'flight_offer_ids': 'flightOfferIds',
            'reporting_data': 'reportingData',
            'virtual_credit_card_details': 'virtualCreditCardDetails'
        }

        self._card_friendly_name = card_friendly_name
        self._card_id = card_id
        self._card_usage_name = card_usage_name
        self._flight_offer_ids = flight_offer_ids
        self._reporting_data = reporting_data
        self._virtual_credit_card_details = virtual_credit_card_details

    @classmethod
    def from_dict(cls, dikt: dict) -> 'B2bWallet':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The B2bWallet of this B2bWallet.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def card_friendly_name(self):
        """Gets the card_friendly_name of this B2bWallet.

        card name

        :return: The card_friendly_name of this B2bWallet.
        :rtype: str
        """
        return self._card_friendly_name

    @card_friendly_name.setter
    def card_friendly_name(self, card_friendly_name):
        """Sets the card_friendly_name of this B2bWallet.

        card name

        :param card_friendly_name: The card_friendly_name of this B2bWallet.
        :type card_friendly_name: str
        """
        if card_friendly_name is not None and not re.search(r'[a-zA-Z0-9]{1,35}', card_friendly_name):
            raise ValueError("Invalid value for `card_friendly_name`, must be a follow pattern or equal to `/[a-zA-Z0-9]{1,35}/`")

        self._card_friendly_name = card_friendly_name

    @property
    def card_id(self):
        """Gets the card_id of this B2bWallet.

        card identifier

        :return: The card_id of this B2bWallet.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this B2bWallet.

        card identifier

        :param card_id: The card_id of this B2bWallet.
        :type card_id: str
        """

        self._card_id = card_id

    @property
    def card_usage_name(self):
        """Gets the card_usage_name of this B2bWallet.

        card usage name

        :return: The card_usage_name of this B2bWallet.
        :rtype: str
        """
        return self._card_usage_name

    @card_usage_name.setter
    def card_usage_name(self, card_usage_name):
        """Sets the card_usage_name of this B2bWallet.

        card usage name

        :param card_usage_name: The card_usage_name of this B2bWallet.
        :type card_usage_name: str
        """

        self._card_usage_name = card_usage_name

    @property
    def flight_offer_ids(self):
        """Gets the flight_offer_ids of this B2bWallet.

        Id of the concern flightOffers

        :return: The flight_offer_ids of this B2bWallet.
        :rtype: List[str]
        """
        return self._flight_offer_ids

    @flight_offer_ids.setter
    def flight_offer_ids(self, flight_offer_ids):
        """Sets the flight_offer_ids of this B2bWallet.

        Id of the concern flightOffers

        :param flight_offer_ids: The flight_offer_ids of this B2bWallet.
        :type flight_offer_ids: List[str]
        """
        if flight_offer_ids is not None and len(flight_offer_ids) > 6:
            raise ValueError("Invalid value for `flight_offer_ids`, number of items must be less than or equal to `6`")
        if flight_offer_ids is not None and len(flight_offer_ids) < 1:
            raise ValueError("Invalid value for `flight_offer_ids`, number of items must be greater than or equal to `1`")

        self._flight_offer_ids = flight_offer_ids

    @property
    def reporting_data(self):
        """Gets the reporting_data of this B2bWallet.


        :return: The reporting_data of this B2bWallet.
        :rtype: List[ReportingData]
        """
        return self._reporting_data

    @reporting_data.setter
    def reporting_data(self, reporting_data):
        """Sets the reporting_data of this B2bWallet.


        :param reporting_data: The reporting_data of this B2bWallet.
        :type reporting_data: List[ReportingData]
        """

        self._reporting_data = reporting_data

    @property
    def virtual_credit_card_details(self):
        """Gets the virtual_credit_card_details of this B2bWallet.


        :return: The virtual_credit_card_details of this B2bWallet.
        :rtype: VirtualCreditCardDetails
        """
        return self._virtual_credit_card_details

    @virtual_credit_card_details.setter
    def virtual_credit_card_details(self, virtual_credit_card_details):
        """Sets the virtual_credit_card_details of this B2bWallet.


        :param virtual_credit_card_details: The virtual_credit_card_details of this B2bWallet.
        :type virtual_credit_card_details: VirtualCreditCardDetails
        """

        self._virtual_credit_card_details = virtual_credit_card_details
