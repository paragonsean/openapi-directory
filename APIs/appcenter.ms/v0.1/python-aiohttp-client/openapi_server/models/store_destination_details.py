# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class StoreDestinationDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_id: str=None, dest_publish_id: str=None, store_type: str=None):
        """StoreDestinationDetails - a model defined in OpenAPI

        :param app_id: The app_id of this StoreDestinationDetails.
        :param dest_publish_id: The dest_publish_id of this StoreDestinationDetails.
        :param store_type: The store_type of this StoreDestinationDetails.
        """
        self.openapi_types = {
            'app_id': str,
            'dest_publish_id': str,
            'store_type': str
        }

        self.attribute_map = {
            'app_id': 'appId',
            'dest_publish_id': 'dest_publish_id',
            'store_type': 'store_type'
        }

        self._app_id = app_id
        self._dest_publish_id = dest_publish_id
        self._store_type = store_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StoreDestinationDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The StoreDestinationDetails of this StoreDestinationDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self):
        """Gets the app_id of this StoreDestinationDetails.

        app id of application.

        :return: The app_id of this StoreDestinationDetails.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this StoreDestinationDetails.

        app id of application.

        :param app_id: The app_id of this StoreDestinationDetails.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def dest_publish_id(self):
        """Gets the dest_publish_id of this StoreDestinationDetails.

        destination ID identifying a unique id in distribution store.

        :return: The dest_publish_id of this StoreDestinationDetails.
        :rtype: str
        """
        return self._dest_publish_id

    @dest_publish_id.setter
    def dest_publish_id(self, dest_publish_id):
        """Sets the dest_publish_id of this StoreDestinationDetails.

        destination ID identifying a unique id in distribution store.

        :param dest_publish_id: The dest_publish_id of this StoreDestinationDetails.
        :type dest_publish_id: str
        """

        self._dest_publish_id = dest_publish_id

    @property
    def store_type(self):
        """Gets the store_type of this StoreDestinationDetails.

        type of store.

        :return: The store_type of this StoreDestinationDetails.
        :rtype: str
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        """Sets the store_type of this StoreDestinationDetails.

        type of store.

        :param store_type: The store_type of this StoreDestinationDetails.
        :type store_type: str
        """
        allowed_values = ["intune"]  # noqa: E501
        if store_type not in allowed_values:
            raise ValueError(
                "Invalid value for `store_type` ({0}), must be one of {1}"
                .format(store_type, allowed_values)
            )

        self._store_type = store_type
