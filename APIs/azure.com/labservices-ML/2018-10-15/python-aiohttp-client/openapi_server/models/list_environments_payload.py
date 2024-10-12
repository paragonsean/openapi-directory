# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ListEnvironmentsPayload(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lab_id: str=None):
        """ListEnvironmentsPayload - a model defined in OpenAPI

        :param lab_id: The lab_id of this ListEnvironmentsPayload.
        """
        self.openapi_types = {
            'lab_id': str
        }

        self.attribute_map = {
            'lab_id': 'labId'
        }

        self._lab_id = lab_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListEnvironmentsPayload':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ListEnvironmentsPayload of this ListEnvironmentsPayload.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lab_id(self):
        """Gets the lab_id of this ListEnvironmentsPayload.

        The resource Id of the lab

        :return: The lab_id of this ListEnvironmentsPayload.
        :rtype: str
        """
        return self._lab_id

    @lab_id.setter
    def lab_id(self, lab_id):
        """Sets the lab_id of this ListEnvironmentsPayload.

        The resource Id of the lab

        :param lab_id: The lab_id of this ListEnvironmentsPayload.
        :type lab_id: str
        """

        self._lab_id = lab_id
