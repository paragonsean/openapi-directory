# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.size_info import SizeInfo
from openapi_server import util


class EnvironmentSize(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, max_price: float=None, min_memory: float=None, min_number_of_cores: int=None, name: str=None, vm_sizes: List[SizeInfo]=None):
        """EnvironmentSize - a model defined in OpenAPI

        :param max_price: The max_price of this EnvironmentSize.
        :param min_memory: The min_memory of this EnvironmentSize.
        :param min_number_of_cores: The min_number_of_cores of this EnvironmentSize.
        :param name: The name of this EnvironmentSize.
        :param vm_sizes: The vm_sizes of this EnvironmentSize.
        """
        self.openapi_types = {
            'max_price': float,
            'min_memory': float,
            'min_number_of_cores': int,
            'name': str,
            'vm_sizes': List[SizeInfo]
        }

        self.attribute_map = {
            'max_price': 'maxPrice',
            'min_memory': 'minMemory',
            'min_number_of_cores': 'minNumberOfCores',
            'name': 'name',
            'vm_sizes': 'vmSizes'
        }

        self._max_price = max_price
        self._min_memory = min_memory
        self._min_number_of_cores = min_number_of_cores
        self._name = name
        self._vm_sizes = vm_sizes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EnvironmentSize':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EnvironmentSize of this EnvironmentSize.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max_price(self):
        """Gets the max_price of this EnvironmentSize.

        The pay-as-you-go dollar price per hour this size will cost. It does not include discounts and may not reflect the actual price the size will cost. This is the maximum price of all prices within this tier.

        :return: The max_price of this EnvironmentSize.
        :rtype: float
        """
        return self._max_price

    @max_price.setter
    def max_price(self, max_price):
        """Sets the max_price of this EnvironmentSize.

        The pay-as-you-go dollar price per hour this size will cost. It does not include discounts and may not reflect the actual price the size will cost. This is the maximum price of all prices within this tier.

        :param max_price: The max_price of this EnvironmentSize.
        :type max_price: float
        """

        self._max_price = max_price

    @property
    def min_memory(self):
        """Gets the min_memory of this EnvironmentSize.

        The amount of memory available (in GB). This is the minimum amount of memory within this tier.

        :return: The min_memory of this EnvironmentSize.
        :rtype: float
        """
        return self._min_memory

    @min_memory.setter
    def min_memory(self, min_memory):
        """Sets the min_memory of this EnvironmentSize.

        The amount of memory available (in GB). This is the minimum amount of memory within this tier.

        :param min_memory: The min_memory of this EnvironmentSize.
        :type min_memory: float
        """

        self._min_memory = min_memory

    @property
    def min_number_of_cores(self):
        """Gets the min_number_of_cores of this EnvironmentSize.

        The number of cores a VM of this size has. This is the minimum number of cores within this tier.

        :return: The min_number_of_cores of this EnvironmentSize.
        :rtype: int
        """
        return self._min_number_of_cores

    @min_number_of_cores.setter
    def min_number_of_cores(self, min_number_of_cores):
        """Sets the min_number_of_cores of this EnvironmentSize.

        The number of cores a VM of this size has. This is the minimum number of cores within this tier.

        :param min_number_of_cores: The min_number_of_cores of this EnvironmentSize.
        :type min_number_of_cores: int
        """

        self._min_number_of_cores = min_number_of_cores

    @property
    def name(self):
        """Gets the name of this EnvironmentSize.

        The size category

        :return: The name of this EnvironmentSize.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentSize.

        The size category

        :param name: The name of this EnvironmentSize.
        :type name: str
        """
        allowed_values = ["Basic", "Standard", "Performance"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def vm_sizes(self):
        """Gets the vm_sizes of this EnvironmentSize.

        Represents a set of compute sizes that can serve this given size type

        :return: The vm_sizes of this EnvironmentSize.
        :rtype: List[SizeInfo]
        """
        return self._vm_sizes

    @vm_sizes.setter
    def vm_sizes(self, vm_sizes):
        """Sets the vm_sizes of this EnvironmentSize.

        Represents a set of compute sizes that can serve this given size type

        :param vm_sizes: The vm_sizes of this EnvironmentSize.
        :type vm_sizes: List[SizeInfo]
        """

        self._vm_sizes = vm_sizes
