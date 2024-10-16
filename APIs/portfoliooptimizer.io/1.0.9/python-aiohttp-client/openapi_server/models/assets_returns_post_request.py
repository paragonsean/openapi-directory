# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.assets_returns_post_request_assets_inner import AssetsReturnsPostRequestAssetsInner
from openapi_server import util


class AssetsReturnsPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: List[AssetsReturnsPostRequestAssetsInner]=None):
        """AssetsReturnsPostRequest - a model defined in OpenAPI

        :param assets: The assets of this AssetsReturnsPostRequest.
        """
        self.openapi_types = {
            'assets': List[AssetsReturnsPostRequestAssetsInner]
        }

        self.attribute_map = {
            'assets': 'assets'
        }

        self._assets = assets

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsReturnsPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_returns_post_request of this AssetsReturnsPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this AssetsReturnsPostRequest.


        :return: The assets of this AssetsReturnsPostRequest.
        :rtype: List[AssetsReturnsPostRequestAssetsInner]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this AssetsReturnsPostRequest.


        :param assets: The assets of this AssetsReturnsPostRequest.
        :type assets: List[AssetsReturnsPostRequestAssetsInner]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")
        if assets is not None and len(assets) < 1:
            raise ValueError("Invalid value for `assets`, number of items must be greater than or equal to `1`")

        self._assets = assets
