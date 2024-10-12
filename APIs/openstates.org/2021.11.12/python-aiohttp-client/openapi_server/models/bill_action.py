# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.organization import Organization
from openapi_server import util


class BillAction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, classification: List[str]=None, _date: str=None, description: str=None, order: int=None, organization: Organization=None):
        """BillAction - a model defined in OpenAPI

        :param classification: The classification of this BillAction.
        :param _date: The _date of this BillAction.
        :param description: The description of this BillAction.
        :param order: The order of this BillAction.
        :param organization: The organization of this BillAction.
        """
        self.openapi_types = {
            'classification': List[str],
            '_date': str,
            'description': str,
            'order': int,
            'organization': Organization
        }

        self.attribute_map = {
            'classification': 'classification',
            '_date': 'date',
            'description': 'description',
            'order': 'order',
            'organization': 'organization'
        }

        self._classification = classification
        self.__date = _date
        self._description = description
        self._order = order
        self._organization = organization

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BillAction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BillAction of this BillAction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def classification(self):
        """Gets the classification of this BillAction.


        :return: The classification of this BillAction.
        :rtype: List[str]
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this BillAction.


        :param classification: The classification of this BillAction.
        :type classification: List[str]
        """
        if classification is None:
            raise ValueError("Invalid value for `classification`, must not be `None`")

        self._classification = classification

    @property
    def _date(self):
        """Gets the _date of this BillAction.


        :return: The _date of this BillAction.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this BillAction.


        :param _date: The _date of this BillAction.
        :type _date: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")

        self.__date = _date

    @property
    def description(self):
        """Gets the description of this BillAction.


        :return: The description of this BillAction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BillAction.


        :param description: The description of this BillAction.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def order(self):
        """Gets the order of this BillAction.


        :return: The order of this BillAction.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this BillAction.


        :param order: The order of this BillAction.
        :type order: int
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")

        self._order = order

    @property
    def organization(self):
        """Gets the organization of this BillAction.


        :return: The organization of this BillAction.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this BillAction.


        :param organization: The organization of this BillAction.
        :type organization: Organization
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")

        self._organization = organization
