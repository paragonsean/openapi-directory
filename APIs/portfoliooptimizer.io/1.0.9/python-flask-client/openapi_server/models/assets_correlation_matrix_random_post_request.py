from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class AssetsCorrelationMatrixRandomPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets=None):  # noqa: E501
        """AssetsCorrelationMatrixRandomPostRequest - a model defined in OpenAPI

        :param assets: The assets of this AssetsCorrelationMatrixRandomPostRequest.  # noqa: E501
        :type assets: int
        """
        self.openapi_types = {
            'assets': int
        }

        self.attribute_map = {
            'assets': 'assets'
        }

        self._assets = assets

    @classmethod
    def from_dict(cls, dikt) -> 'AssetsCorrelationMatrixRandomPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _assets_correlation_matrix_random_post_request of this AssetsCorrelationMatrixRandomPostRequest.  # noqa: E501
        :rtype: AssetsCorrelationMatrixRandomPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self) -> int:
        """Gets the assets of this AssetsCorrelationMatrixRandomPostRequest.

        The number of assets  # noqa: E501

        :return: The assets of this AssetsCorrelationMatrixRandomPostRequest.
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets: int):
        """Sets the assets of this AssetsCorrelationMatrixRandomPostRequest.

        The number of assets  # noqa: E501

        :param assets: The assets of this AssetsCorrelationMatrixRandomPostRequest.
        :type assets: int
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")  # noqa: E501
        if assets is not None and assets < 2:  # noqa: E501
            raise ValueError("Invalid value for `assets`, must be a value greater than or equal to `2`")  # noqa: E501

        self._assets = assets
