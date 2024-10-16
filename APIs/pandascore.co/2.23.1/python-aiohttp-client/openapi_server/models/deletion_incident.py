# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.deletion_incident_change_type import DeletionIncidentChangeType
from openapi_server.models.deletion_object import DeletionObject
from openapi_server.models.incident_id import IncidentID
from openapi_server.models.incident_type import IncidentType
from openapi_server import util


class DeletionIncident(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, change_type: DeletionIncidentChangeType=None, id: IncidentID=None, modified_at: datetime=None, object: DeletionObject=None, type: IncidentType=None):
        """DeletionIncident - a model defined in OpenAPI

        :param change_type: The change_type of this DeletionIncident.
        :param id: The id of this DeletionIncident.
        :param modified_at: The modified_at of this DeletionIncident.
        :param object: The object of this DeletionIncident.
        :param type: The type of this DeletionIncident.
        """
        self.openapi_types = {
            'change_type': DeletionIncidentChangeType,
            'id': IncidentID,
            'modified_at': datetime,
            'object': DeletionObject,
            'type': IncidentType
        }

        self.attribute_map = {
            'change_type': 'change_type',
            'id': 'id',
            'modified_at': 'modified_at',
            'object': 'object',
            'type': 'type'
        }

        self._change_type = change_type
        self._id = id
        self._modified_at = modified_at
        self._object = object
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeletionIncident':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeletionIncident of this DeletionIncident.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def change_type(self):
        """Gets the change_type of this DeletionIncident.


        :return: The change_type of this DeletionIncident.
        :rtype: DeletionIncidentChangeType
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this DeletionIncident.


        :param change_type: The change_type of this DeletionIncident.
        :type change_type: DeletionIncidentChangeType
        """
        if change_type is None:
            raise ValueError("Invalid value for `change_type`, must not be `None`")

        self._change_type = change_type

    @property
    def id(self):
        """Gets the id of this DeletionIncident.


        :return: The id of this DeletionIncident.
        :rtype: IncidentID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeletionIncident.


        :param id: The id of this DeletionIncident.
        :type id: IncidentID
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def modified_at(self):
        """Gets the modified_at of this DeletionIncident.


        :return: The modified_at of this DeletionIncident.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this DeletionIncident.


        :param modified_at: The modified_at of this DeletionIncident.
        :type modified_at: datetime
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")
        if modified_at is not None and len(modified_at) < 1:
            raise ValueError("Invalid value for `modified_at`, length must be greater than or equal to `1`")

        self._modified_at = modified_at

    @property
    def object(self):
        """Gets the object of this DeletionIncident.


        :return: The object of this DeletionIncident.
        :rtype: DeletionObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this DeletionIncident.


        :param object: The object of this DeletionIncident.
        :type object: DeletionObject
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")

        self._object = object

    @property
    def type(self):
        """Gets the type of this DeletionIncident.


        :return: The type of this DeletionIncident.
        :rtype: IncidentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeletionIncident.


        :param type: The type of this DeletionIncident.
        :type type: IncidentType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
