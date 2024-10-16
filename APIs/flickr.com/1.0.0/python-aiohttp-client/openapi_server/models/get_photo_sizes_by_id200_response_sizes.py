# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.size import Size
from openapi_server import util


class GetPhotoSizesByID200ResponseSizes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, canblog: float=None, candownload: float=None, canprint: float=None, sizes: List[Size]=None):
        """GetPhotoSizesByID200ResponseSizes - a model defined in OpenAPI

        :param canblog: The canblog of this GetPhotoSizesByID200ResponseSizes.
        :param candownload: The candownload of this GetPhotoSizesByID200ResponseSizes.
        :param canprint: The canprint of this GetPhotoSizesByID200ResponseSizes.
        :param sizes: The sizes of this GetPhotoSizesByID200ResponseSizes.
        """
        self.openapi_types = {
            'canblog': float,
            'candownload': float,
            'canprint': float,
            'sizes': List[Size]
        }

        self.attribute_map = {
            'canblog': 'canblog',
            'candownload': 'candownload',
            'canprint': 'canprint',
            'sizes': 'sizes'
        }

        self._canblog = canblog
        self._candownload = candownload
        self._canprint = canprint
        self._sizes = sizes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetPhotoSizesByID200ResponseSizes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getPhotoSizesByID_200_response_sizes of this GetPhotoSizesByID200ResponseSizes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def canblog(self):
        """Gets the canblog of this GetPhotoSizesByID200ResponseSizes.


        :return: The canblog of this GetPhotoSizesByID200ResponseSizes.
        :rtype: float
        """
        return self._canblog

    @canblog.setter
    def canblog(self, canblog):
        """Sets the canblog of this GetPhotoSizesByID200ResponseSizes.


        :param canblog: The canblog of this GetPhotoSizesByID200ResponseSizes.
        :type canblog: float
        """

        self._canblog = canblog

    @property
    def candownload(self):
        """Gets the candownload of this GetPhotoSizesByID200ResponseSizes.


        :return: The candownload of this GetPhotoSizesByID200ResponseSizes.
        :rtype: float
        """
        return self._candownload

    @candownload.setter
    def candownload(self, candownload):
        """Sets the candownload of this GetPhotoSizesByID200ResponseSizes.


        :param candownload: The candownload of this GetPhotoSizesByID200ResponseSizes.
        :type candownload: float
        """

        self._candownload = candownload

    @property
    def canprint(self):
        """Gets the canprint of this GetPhotoSizesByID200ResponseSizes.


        :return: The canprint of this GetPhotoSizesByID200ResponseSizes.
        :rtype: float
        """
        return self._canprint

    @canprint.setter
    def canprint(self, canprint):
        """Sets the canprint of this GetPhotoSizesByID200ResponseSizes.


        :param canprint: The canprint of this GetPhotoSizesByID200ResponseSizes.
        :type canprint: float
        """

        self._canprint = canprint

    @property
    def sizes(self):
        """Gets the sizes of this GetPhotoSizesByID200ResponseSizes.


        :return: The sizes of this GetPhotoSizesByID200ResponseSizes.
        :rtype: List[Size]
        """
        return self._sizes

    @sizes.setter
    def sizes(self, sizes):
        """Sets the sizes of this GetPhotoSizesByID200ResponseSizes.


        :param sizes: The sizes of this GetPhotoSizesByID200ResponseSizes.
        :type sizes: List[Size]
        """

        self._sizes = sizes
