# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.assets_returns_simulation_bootstrap_post_request_assets_inner import AssetsReturnsSimulationBootstrapPostRequestAssetsInner
from openapi_server import util


class AssetsReturnsSimulationBootstrapPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assets: List[AssetsReturnsSimulationBootstrapPostRequestAssetsInner]=None, bootstrap_average_block_length: float=None, bootstrap_block_length: int=None, bootstrap_method: str='stationaryBlock', simulations: int=1, simulations_length: int=None):
        """AssetsReturnsSimulationBootstrapPostRequest - a model defined in OpenAPI

        :param assets: The assets of this AssetsReturnsSimulationBootstrapPostRequest.
        :param bootstrap_average_block_length: The bootstrap_average_block_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :param bootstrap_block_length: The bootstrap_block_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :param bootstrap_method: The bootstrap_method of this AssetsReturnsSimulationBootstrapPostRequest.
        :param simulations: The simulations of this AssetsReturnsSimulationBootstrapPostRequest.
        :param simulations_length: The simulations_length of this AssetsReturnsSimulationBootstrapPostRequest.
        """
        self.openapi_types = {
            'assets': List[AssetsReturnsSimulationBootstrapPostRequestAssetsInner],
            'bootstrap_average_block_length': float,
            'bootstrap_block_length': int,
            'bootstrap_method': str,
            'simulations': int,
            'simulations_length': int
        }

        self.attribute_map = {
            'assets': 'assets',
            'bootstrap_average_block_length': 'bootstrapAverageBlockLength',
            'bootstrap_block_length': 'bootstrapBlockLength',
            'bootstrap_method': 'bootstrapMethod',
            'simulations': 'simulations',
            'simulations_length': 'simulationsLength'
        }

        self._assets = assets
        self._bootstrap_average_block_length = bootstrap_average_block_length
        self._bootstrap_block_length = bootstrap_block_length
        self._bootstrap_method = bootstrap_method
        self._simulations = simulations
        self._simulations_length = simulations_length

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsReturnsSimulationBootstrapPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_returns_simulation_bootstrap_post_request of this AssetsReturnsSimulationBootstrapPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assets(self):
        """Gets the assets of this AssetsReturnsSimulationBootstrapPostRequest.


        :return: The assets of this AssetsReturnsSimulationBootstrapPostRequest.
        :rtype: List[AssetsReturnsSimulationBootstrapPostRequestAssetsInner]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this AssetsReturnsSimulationBootstrapPostRequest.


        :param assets: The assets of this AssetsReturnsSimulationBootstrapPostRequest.
        :type assets: List[AssetsReturnsSimulationBootstrapPostRequestAssetsInner]
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")
        if assets is not None and len(assets) < 2:
            raise ValueError("Invalid value for `assets`, number of items must be greater than or equal to `2`")

        self._assets = assets

    @property
    def bootstrap_average_block_length(self):
        """Gets the bootstrap_average_block_length of this AssetsReturnsSimulationBootstrapPostRequest.

        The average length of the blocks to use in case the bootstrap method is 'stationaryBlock', in time periods; if not provided, defaults to the inverse of 3.15 * the common length of the assetReturns arrays^1/3

        :return: The bootstrap_average_block_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :rtype: float
        """
        return self._bootstrap_average_block_length

    @bootstrap_average_block_length.setter
    def bootstrap_average_block_length(self, bootstrap_average_block_length):
        """Sets the bootstrap_average_block_length of this AssetsReturnsSimulationBootstrapPostRequest.

        The average length of the blocks to use in case the bootstrap method is 'stationaryBlock', in time periods; if not provided, defaults to the inverse of 3.15 * the common length of the assetReturns arrays^1/3

        :param bootstrap_average_block_length: The bootstrap_average_block_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :type bootstrap_average_block_length: float
        """
        if bootstrap_average_block_length is not None and bootstrap_average_block_length < 1:
            raise ValueError("Invalid value for `bootstrap_average_block_length`, must be a value greater than or equal to `1`")

        self._bootstrap_average_block_length = bootstrap_average_block_length

    @property
    def bootstrap_block_length(self):
        """Gets the bootstrap_block_length of this AssetsReturnsSimulationBootstrapPostRequest.

        The length of the blocks to use in case the bootstrap method is 'circularBlock', in time periods; if not provided, defaults to [3.15 * the common length of the assetReturns arrays^1/3]

        :return: The bootstrap_block_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :rtype: int
        """
        return self._bootstrap_block_length

    @bootstrap_block_length.setter
    def bootstrap_block_length(self, bootstrap_block_length):
        """Sets the bootstrap_block_length of this AssetsReturnsSimulationBootstrapPostRequest.

        The length of the blocks to use in case the bootstrap method is 'circularBlock', in time periods; if not provided, defaults to [3.15 * the common length of the assetReturns arrays^1/3]

        :param bootstrap_block_length: The bootstrap_block_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :type bootstrap_block_length: int
        """
        if bootstrap_block_length is not None and bootstrap_block_length < 2:
            raise ValueError("Invalid value for `bootstrap_block_length`, must be a value greater than or equal to `2`")

        self._bootstrap_block_length = bootstrap_block_length

    @property
    def bootstrap_method(self):
        """Gets the bootstrap_method of this AssetsReturnsSimulationBootstrapPostRequest.

        The bootstrap method to use

        :return: The bootstrap_method of this AssetsReturnsSimulationBootstrapPostRequest.
        :rtype: str
        """
        return self._bootstrap_method

    @bootstrap_method.setter
    def bootstrap_method(self, bootstrap_method):
        """Sets the bootstrap_method of this AssetsReturnsSimulationBootstrapPostRequest.

        The bootstrap method to use

        :param bootstrap_method: The bootstrap_method of this AssetsReturnsSimulationBootstrapPostRequest.
        :type bootstrap_method: str
        """
        allowed_values = ["iid", "circularBlock", "stationaryBlock"]  # noqa: E501
        if bootstrap_method not in allowed_values:
            raise ValueError(
                "Invalid value for `bootstrap_method` ({0}), must be one of {1}"
                .format(bootstrap_method, allowed_values)
            )

        self._bootstrap_method = bootstrap_method

    @property
    def simulations(self):
        """Gets the simulations of this AssetsReturnsSimulationBootstrapPostRequest.

        The number of simulations to perform

        :return: The simulations of this AssetsReturnsSimulationBootstrapPostRequest.
        :rtype: int
        """
        return self._simulations

    @simulations.setter
    def simulations(self, simulations):
        """Sets the simulations of this AssetsReturnsSimulationBootstrapPostRequest.

        The number of simulations to perform

        :param simulations: The simulations of this AssetsReturnsSimulationBootstrapPostRequest.
        :type simulations: int
        """
        if simulations is not None and simulations < 1:
            raise ValueError("Invalid value for `simulations`, must be a value greater than or equal to `1`")

        self._simulations = simulations

    @property
    def simulations_length(self):
        """Gets the simulations_length of this AssetsReturnsSimulationBootstrapPostRequest.

        The number of time period(s) to simulate per simulation; if not provided, defaults to the common length of the assetReturns arrays

        :return: The simulations_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :rtype: int
        """
        return self._simulations_length

    @simulations_length.setter
    def simulations_length(self, simulations_length):
        """Sets the simulations_length of this AssetsReturnsSimulationBootstrapPostRequest.

        The number of time period(s) to simulate per simulation; if not provided, defaults to the common length of the assetReturns arrays

        :param simulations_length: The simulations_length of this AssetsReturnsSimulationBootstrapPostRequest.
        :type simulations_length: int
        """
        if simulations_length is not None and simulations_length < 1:
            raise ValueError("Invalid value for `simulations_length`, must be a value greater than or equal to `1`")

        self._simulations_length = simulations_length
