# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CategoryInsertVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, samples: List[str]=None, weight: float=None):
        """CategoryInsertVersion - a model defined in OpenAPI

        :param name: The name of this CategoryInsertVersion.
        :param samples: The samples of this CategoryInsertVersion.
        :param weight: The weight of this CategoryInsertVersion.
        """
        self.openapi_types = {
            'name': str,
            'samples': List[str],
            'weight': float
        }

        self.attribute_map = {
            'name': 'name',
            'samples': 'samples',
            'weight': 'weight'
        }

        self._name = name
        self._samples = samples
        self._weight = weight

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CategoryInsertVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Category_InsertVersion of this CategoryInsertVersion.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CategoryInsertVersion.

        Category name

        :return: The name of this CategoryInsertVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CategoryInsertVersion.

        Category name

        :param name: The name of this CategoryInsertVersion.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def samples(self):
        """Gets the samples of this CategoryInsertVersion.

        Category samples

        :return: The samples of this CategoryInsertVersion.
        :rtype: List[str]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this CategoryInsertVersion.

        Category samples

        :param samples: The samples of this CategoryInsertVersion.
        :type samples: List[str]
        """
        if samples is None:
            raise ValueError("Invalid value for `samples`, must not be `None`")

        self._samples = samples

    @property
    def weight(self):
        """Gets the weight of this CategoryInsertVersion.

        Category weight

        :return: The weight of this CategoryInsertVersion.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CategoryInsertVersion.

        Category weight

        :param weight: The weight of this CategoryInsertVersion.
        :type weight: float
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")

        self._weight = weight
