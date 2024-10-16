# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AssetsReturnsPostRequestAssetsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, asset_prices: List[float]=None):
        """AssetsReturnsPostRequestAssetsInner - a model defined in OpenAPI

        :param asset_prices: The asset_prices of this AssetsReturnsPostRequestAssetsInner.
        """
        self.openapi_types = {
            'asset_prices': List[float]
        }

        self.attribute_map = {
            'asset_prices': 'assetPrices'
        }

        self._asset_prices = asset_prices

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsReturnsPostRequestAssetsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_returns_post_request_assets_inner of this AssetsReturnsPostRequestAssetsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def asset_prices(self):
        """Gets the asset_prices of this AssetsReturnsPostRequestAssetsInner.

        assetPrices[t] is the price of the asset at the time t

        :return: The asset_prices of this AssetsReturnsPostRequestAssetsInner.
        :rtype: List[float]
        """
        return self._asset_prices

    @asset_prices.setter
    def asset_prices(self, asset_prices):
        """Sets the asset_prices of this AssetsReturnsPostRequestAssetsInner.

        assetPrices[t] is the price of the asset at the time t

        :param asset_prices: The asset_prices of this AssetsReturnsPostRequestAssetsInner.
        :type asset_prices: List[float]
        """
        if asset_prices is None:
            raise ValueError("Invalid value for `asset_prices`, must not be `None`")
        if asset_prices is not None and len(asset_prices) < 2:
            raise ValueError("Invalid value for `asset_prices`, number of items must be greater than or equal to `2`")

        self._asset_prices = asset_prices
