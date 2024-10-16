# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SetLiveOnGoogleRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, live_on_google: bool=None, partner_hotel_ids: List[str]=None):
        """SetLiveOnGoogleRequest - a model defined in OpenAPI

        :param live_on_google: The live_on_google of this SetLiveOnGoogleRequest.
        :param partner_hotel_ids: The partner_hotel_ids of this SetLiveOnGoogleRequest.
        """
        self.openapi_types = {
            'live_on_google': bool,
            'partner_hotel_ids': List[str]
        }

        self.attribute_map = {
            'live_on_google': 'liveOnGoogle',
            'partner_hotel_ids': 'partnerHotelIds'
        }

        self._live_on_google = live_on_google
        self._partner_hotel_ids = partner_hotel_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SetLiveOnGoogleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SetLiveOnGoogleRequest of this SetLiveOnGoogleRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def live_on_google(self):
        """Gets the live_on_google of this SetLiveOnGoogleRequest.

        Required. Whether the property will show on Google. When true, Google will show the properties if their integration is complete and the property is available. When false, Google will never show the properties.

        :return: The live_on_google of this SetLiveOnGoogleRequest.
        :rtype: bool
        """
        return self._live_on_google

    @live_on_google.setter
    def live_on_google(self, live_on_google):
        """Sets the live_on_google of this SetLiveOnGoogleRequest.

        Required. Whether the property will show on Google. When true, Google will show the properties if their integration is complete and the property is available. When false, Google will never show the properties.

        :param live_on_google: The live_on_google of this SetLiveOnGoogleRequest.
        :type live_on_google: bool
        """

        self._live_on_google = live_on_google

    @property
    def partner_hotel_ids(self):
        """Gets the partner_hotel_ids of this SetLiveOnGoogleRequest.

        Required. Identifies the properties to update with the liveOnGoogle setting.

        :return: The partner_hotel_ids of this SetLiveOnGoogleRequest.
        :rtype: List[str]
        """
        return self._partner_hotel_ids

    @partner_hotel_ids.setter
    def partner_hotel_ids(self, partner_hotel_ids):
        """Sets the partner_hotel_ids of this SetLiveOnGoogleRequest.

        Required. Identifies the properties to update with the liveOnGoogle setting.

        :param partner_hotel_ids: The partner_hotel_ids of this SetLiveOnGoogleRequest.
        :type partner_hotel_ids: List[str]
        """

        self._partner_hotel_ids = partner_hotel_ids
