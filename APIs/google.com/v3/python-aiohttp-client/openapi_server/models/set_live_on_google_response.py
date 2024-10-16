# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SetLiveOnGoogleResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, failed_hotel_ids: List[str]=None, updated_hotel_ids: List[str]=None):
        """SetLiveOnGoogleResponse - a model defined in OpenAPI

        :param failed_hotel_ids: The failed_hotel_ids of this SetLiveOnGoogleResponse.
        :param updated_hotel_ids: The updated_hotel_ids of this SetLiveOnGoogleResponse.
        """
        self.openapi_types = {
            'failed_hotel_ids': List[str],
            'updated_hotel_ids': List[str]
        }

        self.attribute_map = {
            'failed_hotel_ids': 'failedHotelIds',
            'updated_hotel_ids': 'updatedHotelIds'
        }

        self._failed_hotel_ids = failed_hotel_ids
        self._updated_hotel_ids = updated_hotel_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SetLiveOnGoogleResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SetLiveOnGoogleResponse of this SetLiveOnGoogleResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def failed_hotel_ids(self):
        """Gets the failed_hotel_ids of this SetLiveOnGoogleResponse.

        Identifies properties that Google could not update.

        :return: The failed_hotel_ids of this SetLiveOnGoogleResponse.
        :rtype: List[str]
        """
        return self._failed_hotel_ids

    @failed_hotel_ids.setter
    def failed_hotel_ids(self, failed_hotel_ids):
        """Sets the failed_hotel_ids of this SetLiveOnGoogleResponse.

        Identifies properties that Google could not update.

        :param failed_hotel_ids: The failed_hotel_ids of this SetLiveOnGoogleResponse.
        :type failed_hotel_ids: List[str]
        """

        self._failed_hotel_ids = failed_hotel_ids

    @property
    def updated_hotel_ids(self):
        """Gets the updated_hotel_ids of this SetLiveOnGoogleResponse.

        Identifies the updated properties.

        :return: The updated_hotel_ids of this SetLiveOnGoogleResponse.
        :rtype: List[str]
        """
        return self._updated_hotel_ids

    @updated_hotel_ids.setter
    def updated_hotel_ids(self, updated_hotel_ids):
        """Sets the updated_hotel_ids of this SetLiveOnGoogleResponse.

        Identifies the updated properties.

        :param updated_hotel_ids: The updated_hotel_ids of this SetLiveOnGoogleResponse.
        :type updated_hotel_ids: List[str]
        """

        self._updated_hotel_ids = updated_hotel_ids
