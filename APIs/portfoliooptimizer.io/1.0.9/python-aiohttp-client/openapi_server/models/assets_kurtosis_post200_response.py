# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.assets_kurtosis_post200_response_assets_inner import AssetsKurtosisPost200ResponseAssetsInner
from openapi_server import util


class AssetsKurtosisPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: List[AssetsKurtosisPost200ResponseAssetsInner]=None):
        """AssetsKurtosisPost200Response - a model defined in OpenAPI

        :param assets: The assets of this AssetsKurtosisPost200Response.
        """
        self.openapi_types = {
            'assets': List[AssetsKurtosisPost200ResponseAssetsInner]
        }

        self.attribute_map = {
            'assets': 'assets'
        }

        self._assets = assets

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsKurtosisPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_kurtosis_post_200_response of this AssetsKurtosisPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this AssetsKurtosisPost200Response.


        :return: The assets of this AssetsKurtosisPost200Response.
        :rtype: List[AssetsKurtosisPost200ResponseAssetsInner]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this AssetsKurtosisPost200Response.


        :param assets: The assets of this AssetsKurtosisPost200Response.
        :type assets: List[AssetsKurtosisPost200ResponseAssetsInner]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")

        self._assets = assets
