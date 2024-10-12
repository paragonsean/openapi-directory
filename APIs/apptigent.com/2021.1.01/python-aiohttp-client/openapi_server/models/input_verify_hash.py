# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InputVerifyHash(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, algorithm: str=None, hash: str=None, input: str=None):
        """InputVerifyHash - a model defined in OpenAPI

        :param algorithm: The algorithm of this InputVerifyHash.
        :param hash: The hash of this InputVerifyHash.
        :param input: The input of this InputVerifyHash.
        """
        self.openapi_types = {
            'algorithm': str,
            'hash': str,
            'input': str
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'hash': 'hash',
            'input': 'input'
        }

        self._algorithm = algorithm
        self._hash = hash
        self._input = input

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InputVerifyHash':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inputVerifyHash of this InputVerifyHash.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def algorithm(self):
        """Gets the algorithm of this InputVerifyHash.

        Hash algorithm

        :return: The algorithm of this InputVerifyHash.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this InputVerifyHash.

        Hash algorithm

        :param algorithm: The algorithm of this InputVerifyHash.
        :type algorithm: str
        """
        allowed_values = ["MD5", "SHA1", "SHA256", "SHA384", "SHA512"]  # noqa: E501
        if algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `algorithm` ({0}), must be one of {1}"
                .format(algorithm, allowed_values)
            )

        self._algorithm = algorithm

    @property
    def hash(self):
        """Gets the hash of this InputVerifyHash.

        Hashed result

        :return: The hash of this InputVerifyHash.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this InputVerifyHash.

        Hashed result

        :param hash: The hash of this InputVerifyHash.
        :type hash: str
        """
        if hash is None:
            raise ValueError("Invalid value for `hash`, must not be `None`")

        self._hash = hash

    @property
    def input(self):
        """Gets the input of this InputVerifyHash.

        Original source string

        :return: The input of this InputVerifyHash.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InputVerifyHash.

        Original source string

        :param input: The input of this InputVerifyHash.
        :type input: str
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")

        self._input = input
