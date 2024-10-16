# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.assets_returns_post200_response_assets_inner import AssetsReturnsPost200ResponseAssetsInner
from openapi_server import util


class AssetsReturnsPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: List[AssetsReturnsPost200ResponseAssetsInner]=None):
        """AssetsReturnsPost200Response - a model defined in OpenAPI

        :param assets: The assets of this AssetsReturnsPost200Response.
        """
        self.openapi_types = {
            'assets': List[AssetsReturnsPost200ResponseAssetsInner]
        }

        self.attribute_map = {
            'assets': 'assets'
        }

        self._assets = assets

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsReturnsPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_returns_post_200_response of this AssetsReturnsPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this AssetsReturnsPost200Response.


        :return: The assets of this AssetsReturnsPost200Response.
        :rtype: List[AssetsReturnsPost200ResponseAssetsInner]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this AssetsReturnsPost200Response.


        :param assets: The assets of this AssetsReturnsPost200Response.
        :type assets: List[AssetsReturnsPost200ResponseAssetsInner]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")

        self._assets = assets
