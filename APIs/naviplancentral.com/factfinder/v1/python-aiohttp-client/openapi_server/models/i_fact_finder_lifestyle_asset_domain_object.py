# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IFactFinderLifestyleAssetDomainObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, external_destination_id: str=None, fact_finder_id: int=None, lifestyle_asset_id: int=None, market_value: float=None, owner: str=None, purchase_amount: float=None, purchase_date: datetime=None, type: int=None):
        """IFactFinderLifestyleAssetDomainObject - a model defined in OpenAPI

        :param description: The description of this IFactFinderLifestyleAssetDomainObject.
        :param external_destination_id: The external_destination_id of this IFactFinderLifestyleAssetDomainObject.
        :param fact_finder_id: The fact_finder_id of this IFactFinderLifestyleAssetDomainObject.
        :param lifestyle_asset_id: The lifestyle_asset_id of this IFactFinderLifestyleAssetDomainObject.
        :param market_value: The market_value of this IFactFinderLifestyleAssetDomainObject.
        :param owner: The owner of this IFactFinderLifestyleAssetDomainObject.
        :param purchase_amount: The purchase_amount of this IFactFinderLifestyleAssetDomainObject.
        :param purchase_date: The purchase_date of this IFactFinderLifestyleAssetDomainObject.
        :param type: The type of this IFactFinderLifestyleAssetDomainObject.
        """
        self.openapi_types = {
            'description': str,
            'external_destination_id': str,
            'fact_finder_id': int,
            'lifestyle_asset_id': int,
            'market_value': float,
            'owner': str,
            'purchase_amount': float,
            'purchase_date': datetime,
            'type': int
        }

        self.attribute_map = {
            'description': 'description',
            'external_destination_id': 'externalDestinationId',
            'fact_finder_id': 'factFinderId',
            'lifestyle_asset_id': 'lifestyleAssetId',
            'market_value': 'marketValue',
            'owner': 'owner',
            'purchase_amount': 'purchaseAmount',
            'purchase_date': 'purchaseDate',
            'type': 'type'
        }

        self._description = description
        self._external_destination_id = external_destination_id
        self._fact_finder_id = fact_finder_id
        self._lifestyle_asset_id = lifestyle_asset_id
        self._market_value = market_value
        self._owner = owner
        self._purchase_amount = purchase_amount
        self._purchase_date = purchase_date
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IFactFinderLifestyleAssetDomainObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IFactFinderLifestyleAssetDomainObject of this IFactFinderLifestyleAssetDomainObject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this IFactFinderLifestyleAssetDomainObject.


        :return: The description of this IFactFinderLifestyleAssetDomainObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IFactFinderLifestyleAssetDomainObject.


        :param description: The description of this IFactFinderLifestyleAssetDomainObject.
        :type description: str
        """

        self._description = description

    @property
    def external_destination_id(self):
        """Gets the external_destination_id of this IFactFinderLifestyleAssetDomainObject.


        :return: The external_destination_id of this IFactFinderLifestyleAssetDomainObject.
        :rtype: str
        """
        return self._external_destination_id

    @external_destination_id.setter
    def external_destination_id(self, external_destination_id):
        """Sets the external_destination_id of this IFactFinderLifestyleAssetDomainObject.


        :param external_destination_id: The external_destination_id of this IFactFinderLifestyleAssetDomainObject.
        :type external_destination_id: str
        """

        self._external_destination_id = external_destination_id

    @property
    def fact_finder_id(self):
        """Gets the fact_finder_id of this IFactFinderLifestyleAssetDomainObject.


        :return: The fact_finder_id of this IFactFinderLifestyleAssetDomainObject.
        :rtype: int
        """
        return self._fact_finder_id

    @fact_finder_id.setter
    def fact_finder_id(self, fact_finder_id):
        """Sets the fact_finder_id of this IFactFinderLifestyleAssetDomainObject.


        :param fact_finder_id: The fact_finder_id of this IFactFinderLifestyleAssetDomainObject.
        :type fact_finder_id: int
        """

        self._fact_finder_id = fact_finder_id

    @property
    def lifestyle_asset_id(self):
        """Gets the lifestyle_asset_id of this IFactFinderLifestyleAssetDomainObject.


        :return: The lifestyle_asset_id of this IFactFinderLifestyleAssetDomainObject.
        :rtype: int
        """
        return self._lifestyle_asset_id

    @lifestyle_asset_id.setter
    def lifestyle_asset_id(self, lifestyle_asset_id):
        """Sets the lifestyle_asset_id of this IFactFinderLifestyleAssetDomainObject.


        :param lifestyle_asset_id: The lifestyle_asset_id of this IFactFinderLifestyleAssetDomainObject.
        :type lifestyle_asset_id: int
        """

        self._lifestyle_asset_id = lifestyle_asset_id

    @property
    def market_value(self):
        """Gets the market_value of this IFactFinderLifestyleAssetDomainObject.


        :return: The market_value of this IFactFinderLifestyleAssetDomainObject.
        :rtype: float
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value):
        """Sets the market_value of this IFactFinderLifestyleAssetDomainObject.


        :param market_value: The market_value of this IFactFinderLifestyleAssetDomainObject.
        :type market_value: float
        """

        self._market_value = market_value

    @property
    def owner(self):
        """Gets the owner of this IFactFinderLifestyleAssetDomainObject.


        :return: The owner of this IFactFinderLifestyleAssetDomainObject.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this IFactFinderLifestyleAssetDomainObject.


        :param owner: The owner of this IFactFinderLifestyleAssetDomainObject.
        :type owner: str
        """
        allowed_values = ["Client", "CoClient", "Joint"]  # noqa: E501
        if owner not in allowed_values:
            raise ValueError(
                "Invalid value for `owner` ({0}), must be one of {1}"
                .format(owner, allowed_values)
            )

        self._owner = owner

    @property
    def purchase_amount(self):
        """Gets the purchase_amount of this IFactFinderLifestyleAssetDomainObject.


        :return: The purchase_amount of this IFactFinderLifestyleAssetDomainObject.
        :rtype: float
        """
        return self._purchase_amount

    @purchase_amount.setter
    def purchase_amount(self, purchase_amount):
        """Sets the purchase_amount of this IFactFinderLifestyleAssetDomainObject.


        :param purchase_amount: The purchase_amount of this IFactFinderLifestyleAssetDomainObject.
        :type purchase_amount: float
        """

        self._purchase_amount = purchase_amount

    @property
    def purchase_date(self):
        """Gets the purchase_date of this IFactFinderLifestyleAssetDomainObject.


        :return: The purchase_date of this IFactFinderLifestyleAssetDomainObject.
        :rtype: datetime
        """
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        """Sets the purchase_date of this IFactFinderLifestyleAssetDomainObject.


        :param purchase_date: The purchase_date of this IFactFinderLifestyleAssetDomainObject.
        :type purchase_date: datetime
        """

        self._purchase_date = purchase_date

    @property
    def type(self):
        """Gets the type of this IFactFinderLifestyleAssetDomainObject.


        :return: The type of this IFactFinderLifestyleAssetDomainObject.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IFactFinderLifestyleAssetDomainObject.


        :param type: The type of this IFactFinderLifestyleAssetDomainObject.
        :type type: int
        """

        self._type = type
