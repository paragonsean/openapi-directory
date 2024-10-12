# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ConsentRequestConsentHip(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None):
        """ConsentRequestConsentHip - a model defined in OpenAPI

        :param id: The id of this ConsentRequestConsentHip.
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConsentRequestConsentHip':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ConsentRequest_consent_hip of this ConsentRequestConsentHip.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ConsentRequestConsentHip.


        :return: The id of this ConsentRequestConsentHip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsentRequestConsentHip.


        :param id: The id of this ConsentRequestConsentHip.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
