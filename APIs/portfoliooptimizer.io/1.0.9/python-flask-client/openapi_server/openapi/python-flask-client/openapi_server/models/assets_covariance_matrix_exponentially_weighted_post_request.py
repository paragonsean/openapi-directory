from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.assets_correlation_matrix_post_request_one_of_assets_inner import AssetsCorrelationMatrixPostRequestOneOfAssetsInner
from openapi_server import util

from openapi_server.models.assets_correlation_matrix_post_request_one_of_assets_inner import AssetsCorrelationMatrixPostRequestOneOfAssetsInner  # noqa: E501

class AssetsCovarianceMatrixExponentiallyWeightedPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets=None, decay_factor=0.94):  # noqa: E501
        """AssetsCovarianceMatrixExponentiallyWeightedPostRequest - a model defined in OpenAPI

        :param assets: The assets of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.  # noqa: E501
        :type assets: List[AssetsCorrelationMatrixPostRequestOneOfAssetsInner]
        :param decay_factor: The decay_factor of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.  # noqa: E501
        :type decay_factor: float
        """
        self.openapi_types = {
            'assets': List[AssetsCorrelationMatrixPostRequestOneOfAssetsInner],
            'decay_factor': float
        }

        self.attribute_map = {
            'assets': 'assets',
            'decay_factor': 'decayFactor'
        }

        self._assets = assets
        self._decay_factor = decay_factor

    @classmethod
    def from_dict(cls, dikt) -> 'AssetsCovarianceMatrixExponentiallyWeightedPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _assets_covariance_matrix_exponentially_weighted_post_request of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.  # noqa: E501
        :rtype: AssetsCovarianceMatrixExponentiallyWeightedPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self) -> List[AssetsCorrelationMatrixPostRequestOneOfAssetsInner]:
        """Gets the assets of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.


        :return: The assets of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.
        :rtype: List[AssetsCorrelationMatrixPostRequestOneOfAssetsInner]
        """
        return self._assets

    @assets.setter
    def assets(self, assets: List[AssetsCorrelationMatrixPostRequestOneOfAssetsInner]):
        """Sets the assets of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.


        :param assets: The assets of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.
        :type assets: List[AssetsCorrelationMatrixPostRequestOneOfAssetsInner]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")  # noqa: E501
        if assets is not None and len(assets) < 2:
            raise ValueError("Invalid value for `assets`, number of items must be greater than or equal to `2`")  # noqa: E501

        self._assets = assets

    @property
    def decay_factor(self) -> float:
        """Gets the decay_factor of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.

        The exponential decay factor  # noqa: E501

        :return: The decay_factor of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.
        :rtype: float
        """
        return self._decay_factor

    @decay_factor.setter
    def decay_factor(self, decay_factor: float):
        """Sets the decay_factor of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.

        The exponential decay factor  # noqa: E501

        :param decay_factor: The decay_factor of this AssetsCovarianceMatrixExponentiallyWeightedPostRequest.
        :type decay_factor: float
        """
        if decay_factor is not None and decay_factor >= 1:  # noqa: E501
            raise ValueError("Invalid value for `decay_factor`, must be a value less than `1`")  # noqa: E501
        if decay_factor is not None and decay_factor <= 0:  # noqa: E501
            raise ValueError("Invalid value for `decay_factor`, must be a value greater than `0`")  # noqa: E501

        self._decay_factor = decay_factor
