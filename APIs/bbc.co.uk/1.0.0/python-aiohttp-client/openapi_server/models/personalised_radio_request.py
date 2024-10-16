# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.personalised_radio_meta_data import PersonalisedRadioMetaData
from openapi_server import util


class PersonalisedRadioRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action: str=None, added_at: str=None, context: str=None, metadata: PersonalisedRadioMetaData=None):
        """PersonalisedRadioRequest - a model defined in OpenAPI

        :param action: The action of this PersonalisedRadioRequest.
        :param added_at: The added_at of this PersonalisedRadioRequest.
        :param context: The context of this PersonalisedRadioRequest.
        :param metadata: The metadata of this PersonalisedRadioRequest.
        """
        self.openapi_types = {
            'action': str,
            'added_at': str,
            'context': str,
            'metadata': PersonalisedRadioMetaData
        }

        self.attribute_map = {
            'action': 'action',
            'added_at': 'added_at',
            'context': 'context',
            'metadata': 'metadata'
        }

        self._action = action
        self._added_at = added_at
        self._context = context
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PersonalisedRadioRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PersonalisedRadioRequest of this PersonalisedRadioRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self):
        """Gets the action of this PersonalisedRadioRequest.


        :return: The action of this PersonalisedRadioRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PersonalisedRadioRequest.


        :param action: The action of this PersonalisedRadioRequest.
        :type action: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")

        self._action = action

    @property
    def added_at(self):
        """Gets the added_at of this PersonalisedRadioRequest.


        :return: The added_at of this PersonalisedRadioRequest.
        :rtype: str
        """
        return self._added_at

    @added_at.setter
    def added_at(self, added_at):
        """Sets the added_at of this PersonalisedRadioRequest.


        :param added_at: The added_at of this PersonalisedRadioRequest.
        :type added_at: str
        """

        self._added_at = added_at

    @property
    def context(self):
        """Gets the context of this PersonalisedRadioRequest.


        :return: The context of this PersonalisedRadioRequest.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PersonalisedRadioRequest.


        :param context: The context of this PersonalisedRadioRequest.
        :type context: str
        """

        self._context = context

    @property
    def metadata(self):
        """Gets the metadata of this PersonalisedRadioRequest.


        :return: The metadata of this PersonalisedRadioRequest.
        :rtype: PersonalisedRadioMetaData
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PersonalisedRadioRequest.


        :param metadata: The metadata of this PersonalisedRadioRequest.
        :type metadata: PersonalisedRadioMetaData
        """

        self._metadata = metadata
