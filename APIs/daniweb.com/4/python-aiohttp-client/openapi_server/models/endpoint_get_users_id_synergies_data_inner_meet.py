# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.endpoint_get_users_id_synergies_data_inner_meet_payment import EndpointGetUsersIDSynergiesDataInnerMeetPayment
from openapi_server import util


class EndpointGetUsersIDSynergiesDataInnerMeet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payment: EndpointGetUsersIDSynergiesDataInnerMeetPayment=None, price_usd: float=None):
        """EndpointGetUsersIDSynergiesDataInnerMeet - a model defined in OpenAPI

        :param payment: The payment of this EndpointGetUsersIDSynergiesDataInnerMeet.
        :param price_usd: The price_usd of this EndpointGetUsersIDSynergiesDataInnerMeet.
        """
        self.openapi_types = {
            'payment': EndpointGetUsersIDSynergiesDataInnerMeetPayment,
            'price_usd': float
        }

        self.attribute_map = {
            'payment': 'payment',
            'price_usd': 'price_usd'
        }

        self._payment = payment
        self._price_usd = price_usd

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EndpointGetUsersIDSynergiesDataInnerMeet':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Endpoint_get_users_ID_synergies_data_inner_meet of this EndpointGetUsersIDSynergiesDataInnerMeet.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment(self):
        """Gets the payment of this EndpointGetUsersIDSynergiesDataInnerMeet.


        :return: The payment of this EndpointGetUsersIDSynergiesDataInnerMeet.
        :rtype: EndpointGetUsersIDSynergiesDataInnerMeetPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this EndpointGetUsersIDSynergiesDataInnerMeet.


        :param payment: The payment of this EndpointGetUsersIDSynergiesDataInnerMeet.
        :type payment: EndpointGetUsersIDSynergiesDataInnerMeetPayment
        """

        self._payment = payment

    @property
    def price_usd(self):
        """Gets the price_usd of this EndpointGetUsersIDSynergiesDataInnerMeet.


        :return: The price_usd of this EndpointGetUsersIDSynergiesDataInnerMeet.
        :rtype: float
        """
        return self._price_usd

    @price_usd.setter
    def price_usd(self, price_usd):
        """Sets the price_usd of this EndpointGetUsersIDSynergiesDataInnerMeet.


        :param price_usd: The price_usd of this EndpointGetUsersIDSynergiesDataInnerMeet.
        :type price_usd: float
        """

        self._price_usd = price_usd
