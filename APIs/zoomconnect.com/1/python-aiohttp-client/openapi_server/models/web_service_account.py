# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.link import Link
from openapi_server import util


class WebServiceAccount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, credit_balance: float=None, links: List[Link]=None):
        """WebServiceAccount - a model defined in OpenAPI

        :param credit_balance: The credit_balance of this WebServiceAccount.
        :param links: The links of this WebServiceAccount.
        """
        self.openapi_types = {
            'credit_balance': float,
            'links': List[Link]
        }

        self.attribute_map = {
            'credit_balance': 'creditBalance',
            'links': 'links'
        }

        self._credit_balance = credit_balance
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebServiceAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebServiceAccount of this WebServiceAccount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def credit_balance(self):
        """Gets the credit_balance of this WebServiceAccount.


        :return: The credit_balance of this WebServiceAccount.
        :rtype: float
        """
        return self._credit_balance

    @credit_balance.setter
    def credit_balance(self, credit_balance):
        """Sets the credit_balance of this WebServiceAccount.


        :param credit_balance: The credit_balance of this WebServiceAccount.
        :type credit_balance: float
        """

        self._credit_balance = credit_balance

    @property
    def links(self):
        """Gets the links of this WebServiceAccount.


        :return: The links of this WebServiceAccount.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this WebServiceAccount.


        :param links: The links of this WebServiceAccount.
        :type links: List[Link]
        """

        self._links = links
