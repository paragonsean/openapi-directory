# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.legacy_code_push_acquisition_update_check200_response_update_info import LegacyCodePushAcquisitionUpdateCheck200ResponseUpdateInfo
from openapi_server import util


class LegacyCodePushAcquisitionUpdateCheck200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, update_info: LegacyCodePushAcquisitionUpdateCheck200ResponseUpdateInfo=None):
        """LegacyCodePushAcquisitionUpdateCheck200Response - a model defined in OpenAPI

        :param update_info: The update_info of this LegacyCodePushAcquisitionUpdateCheck200Response.
        """
        self.openapi_types = {
            'update_info': LegacyCodePushAcquisitionUpdateCheck200ResponseUpdateInfo
        }

        self.attribute_map = {
            'update_info': 'updateInfo'
        }

        self._update_info = update_info

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LegacyCodePushAcquisitionUpdateCheck200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The legacyCodePushAcquisition_updateCheck_200_response of this LegacyCodePushAcquisitionUpdateCheck200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def update_info(self):
        """Gets the update_info of this LegacyCodePushAcquisitionUpdateCheck200Response.


        :return: The update_info of this LegacyCodePushAcquisitionUpdateCheck200Response.
        :rtype: LegacyCodePushAcquisitionUpdateCheck200ResponseUpdateInfo
        """
        return self._update_info

    @update_info.setter
    def update_info(self, update_info):
        """Sets the update_info of this LegacyCodePushAcquisitionUpdateCheck200Response.


        :param update_info: The update_info of this LegacyCodePushAcquisitionUpdateCheck200Response.
        :type update_info: LegacyCodePushAcquisitionUpdateCheck200ResponseUpdateInfo
        """
        if update_info is None:
            raise ValueError("Invalid value for `update_info`, must not be `None`")

        self._update_info = update_info
