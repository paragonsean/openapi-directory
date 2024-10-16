# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.assets_prices_adjusted_post200_response_assets_inner_asset_adjusted_prices_inner import AssetsPricesAdjustedPost200ResponseAssetsInnerAssetAdjustedPricesInner
from openapi_server import util


class AssetsPricesAdjustedPost200ResponseAssetsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, asset_adjusted_prices: List[AssetsPricesAdjustedPost200ResponseAssetsInnerAssetAdjustedPricesInner]=None):
        """AssetsPricesAdjustedPost200ResponseAssetsInner - a model defined in OpenAPI

        :param asset_adjusted_prices: The asset_adjusted_prices of this AssetsPricesAdjustedPost200ResponseAssetsInner.
        """
        self.openapi_types = {
            'asset_adjusted_prices': List[AssetsPricesAdjustedPost200ResponseAssetsInnerAssetAdjustedPricesInner]
        }

        self.attribute_map = {
            'asset_adjusted_prices': 'assetAdjustedPrices'
        }

        self._asset_adjusted_prices = asset_adjusted_prices

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsPricesAdjustedPost200ResponseAssetsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_prices_adjusted_post_200_response_assets_inner of this AssetsPricesAdjustedPost200ResponseAssetsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def asset_adjusted_prices(self):
        """Gets the asset_adjusted_prices of this AssetsPricesAdjustedPost200ResponseAssetsInner.

        assetAdjustedPrices[t] contains adjusted price information for the asset at the date t

        :return: The asset_adjusted_prices of this AssetsPricesAdjustedPost200ResponseAssetsInner.
        :rtype: List[AssetsPricesAdjustedPost200ResponseAssetsInnerAssetAdjustedPricesInner]
        """
        return self._asset_adjusted_prices

    @asset_adjusted_prices.setter
    def asset_adjusted_prices(self, asset_adjusted_prices):
        """Sets the asset_adjusted_prices of this AssetsPricesAdjustedPost200ResponseAssetsInner.

        assetAdjustedPrices[t] contains adjusted price information for the asset at the date t

        :param asset_adjusted_prices: The asset_adjusted_prices of this AssetsPricesAdjustedPost200ResponseAssetsInner.
        :type asset_adjusted_prices: List[AssetsPricesAdjustedPost200ResponseAssetsInnerAssetAdjustedPricesInner]
        """
        if asset_adjusted_prices is None:
            raise ValueError("Invalid value for `asset_adjusted_prices`, must not be `None`")
        if asset_adjusted_prices is not None and len(asset_adjusted_prices) < 1:
            raise ValueError("Invalid value for `asset_adjusted_prices`, number of items must be greater than or equal to `1`")

        self._asset_adjusted_prices = asset_adjusted_prices
