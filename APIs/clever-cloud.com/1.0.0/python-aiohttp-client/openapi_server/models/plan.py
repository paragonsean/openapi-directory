# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.feature import Feature
from openapi_server import util


class Plan(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, features: List[Feature]=None, id: str=None, name: str=None, price: int=None, slug: str=None):
        """Plan - a model defined in OpenAPI

        :param features: The features of this Plan.
        :param id: The id of this Plan.
        :param name: The name of this Plan.
        :param price: The price of this Plan.
        :param slug: The slug of this Plan.
        """
        self.openapi_types = {
            'features': List[Feature],
            'id': str,
            'name': str,
            'price': int,
            'slug': str
        }

        self.attribute_map = {
            'features': 'features',
            'id': 'id',
            'name': 'name',
            'price': 'price',
            'slug': 'slug'
        }

        self._features = features
        self._id = id
        self._name = name
        self._price = price
        self._slug = slug

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Plan':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Plan of this Plan.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def features(self):
        """Gets the features of this Plan.

        The list of the feature in the addon

        :return: The features of this Plan.
        :rtype: List[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Plan.

        The list of the feature in the addon

        :param features: The features of this Plan.
        :type features: List[Feature]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")

        self._features = features

    @property
    def id(self):
        """Gets the id of this Plan.

        `plan_${uuid}`

        :return: The id of this Plan.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Plan.

        `plan_${uuid}`

        :param id: The id of this Plan.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this Plan.

        Name of the pan

        :return: The name of this Plan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plan.

        Name of the pan

        :param name: The name of this Plan.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def price(self):
        """Gets the price of this Plan.


        :return: The price of this Plan.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Plan.


        :param price: The price of this Plan.
        :type price: int
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def slug(self):
        """Gets the slug of this Plan.


        :return: The slug of this Plan.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Plan.


        :param slug: The slug of this Plan.
        :type slug: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")

        self._slug = slug
