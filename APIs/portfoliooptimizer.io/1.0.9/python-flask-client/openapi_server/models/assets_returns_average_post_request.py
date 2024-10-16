from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.assets_returns_average_post_request_assets_inner import AssetsReturnsAveragePostRequestAssetsInner
from openapi_server import util

from openapi_server.models.assets_returns_average_post_request_assets_inner import AssetsReturnsAveragePostRequestAssetsInner  # noqa: E501

class AssetsReturnsAveragePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets=None):  # noqa: E501
        """AssetsReturnsAveragePostRequest - a model defined in OpenAPI

        :param assets: The assets of this AssetsReturnsAveragePostRequest.  # noqa: E501
        :type assets: List[AssetsReturnsAveragePostRequestAssetsInner]
        """
        self.openapi_types = {
            'assets': List[AssetsReturnsAveragePostRequestAssetsInner]
        }

        self.attribute_map = {
            'assets': 'assets'
        }

        self._assets = assets

    @classmethod
    def from_dict(cls, dikt) -> 'AssetsReturnsAveragePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _assets_returns_average_post_request of this AssetsReturnsAveragePostRequest.  # noqa: E501
        :rtype: AssetsReturnsAveragePostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self) -> List[AssetsReturnsAveragePostRequestAssetsInner]:
        """Gets the assets of this AssetsReturnsAveragePostRequest.


        :return: The assets of this AssetsReturnsAveragePostRequest.
        :rtype: List[AssetsReturnsAveragePostRequestAssetsInner]
        """
        return self._assets

    @assets.setter
    def assets(self, assets: List[AssetsReturnsAveragePostRequestAssetsInner]):
        """Sets the assets of this AssetsReturnsAveragePostRequest.


        :param assets: The assets of this AssetsReturnsAveragePostRequest.
        :type assets: List[AssetsReturnsAveragePostRequestAssetsInner]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")  # noqa: E501
        if assets is not None and len(assets) < 1:
            raise ValueError("Invalid value for `assets`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._assets = assets
