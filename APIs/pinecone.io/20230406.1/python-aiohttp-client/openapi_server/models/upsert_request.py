# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.upsert_vector import UpsertVector
from openapi_server import util


class UpsertRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, namespace: str=None, vectors: List[UpsertVector]=None):
        """UpsertRequest - a model defined in OpenAPI

        :param namespace: The namespace of this UpsertRequest.
        :param vectors: The vectors of this UpsertRequest.
        """
        self.openapi_types = {
            'namespace': str,
            'vectors': List[UpsertVector]
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'vectors': 'vectors'
        }

        self._namespace = namespace
        self._vectors = vectors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpsertRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpsertRequest of this UpsertRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def namespace(self):
        """Gets the namespace of this UpsertRequest.

        An index namespace name

        :return: The namespace of this UpsertRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UpsertRequest.

        An index namespace name

        :param namespace: The namespace of this UpsertRequest.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def vectors(self):
        """Gets the vectors of this UpsertRequest.


        :return: The vectors of this UpsertRequest.
        :rtype: List[UpsertVector]
        """
        return self._vectors

    @vectors.setter
    def vectors(self, vectors):
        """Sets the vectors of this UpsertRequest.


        :param vectors: The vectors of this UpsertRequest.
        :type vectors: List[UpsertVector]
        """
        if vectors is None:
            raise ValueError("Invalid value for `vectors`, must not be `None`")

        self._vectors = vectors
