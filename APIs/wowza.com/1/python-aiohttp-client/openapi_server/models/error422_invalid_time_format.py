# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.meta import Meta
from openapi_server import util


class Error422InvalidTimeFormat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, meta: Meta=None):
        """Error422InvalidTimeFormat - a model defined in OpenAPI

        :param meta: The meta of this Error422InvalidTimeFormat.
        """
        self.openapi_types = {
            'meta': Meta
        }

        self.attribute_map = {
            'meta': 'meta'
        }

        self._meta = meta

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error422InvalidTimeFormat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Error422InvalidTimeFormat of this Error422InvalidTimeFormat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self):
        """Gets the meta of this Error422InvalidTimeFormat.


        :return: The meta of this Error422InvalidTimeFormat.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Error422InvalidTimeFormat.


        :param meta: The meta of this Error422InvalidTimeFormat.
        :type meta: Meta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")

        self._meta = meta
