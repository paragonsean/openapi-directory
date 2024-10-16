# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AssetsReturnsSimulationMonteCarloGaussianPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, asset_average_return: float=None, asset_volatility: float=None, simulations: int=1, simulations_length: int=1):
        """AssetsReturnsSimulationMonteCarloGaussianPostRequest - a model defined in OpenAPI

        :param asset_average_return: The asset_average_return of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :param asset_volatility: The asset_volatility of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :param simulations: The simulations of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :param simulations_length: The simulations_length of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        """
        self.openapi_types = {
            'asset_average_return': float,
            'asset_volatility': float,
            'simulations': int,
            'simulations_length': int
        }

        self.attribute_map = {
            'asset_average_return': 'assetAverageReturn',
            'asset_volatility': 'assetVolatility',
            'simulations': 'simulations',
            'simulations_length': 'simulationsLength'
        }

        self._asset_average_return = asset_average_return
        self._asset_volatility = asset_volatility
        self._simulations = simulations
        self._simulations_length = simulations_length

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsReturnsSimulationMonteCarloGaussianPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_returns_simulation_monte_carlo_gaussian_post_request of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def asset_average_return(self):
        """Gets the asset_average_return of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The arithmetic average return of the asset, corresponding to the mean of the Gaussian distribution

        :return: The asset_average_return of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :rtype: float
        """
        return self._asset_average_return

    @asset_average_return.setter
    def asset_average_return(self, asset_average_return):
        """Sets the asset_average_return of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The arithmetic average return of the asset, corresponding to the mean of the Gaussian distribution

        :param asset_average_return: The asset_average_return of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :type asset_average_return: float
        """
        if asset_average_return is None:
            raise ValueError("Invalid value for `asset_average_return`, must not be `None`")

        self._asset_average_return = asset_average_return

    @property
    def asset_volatility(self):
        """Gets the asset_volatility of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The volatility of the asset returns, corresponding to the standard deviation of the Gaussian distribution

        :return: The asset_volatility of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :rtype: float
        """
        return self._asset_volatility

    @asset_volatility.setter
    def asset_volatility(self, asset_volatility):
        """Sets the asset_volatility of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The volatility of the asset returns, corresponding to the standard deviation of the Gaussian distribution

        :param asset_volatility: The asset_volatility of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :type asset_volatility: float
        """
        if asset_volatility is None:
            raise ValueError("Invalid value for `asset_volatility`, must not be `None`")
        if asset_volatility is not None and asset_volatility <= 0:
            raise ValueError("Invalid value for `asset_volatility`, must be a value greater than `0`")

        self._asset_volatility = asset_volatility

    @property
    def simulations(self):
        """Gets the simulations of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The number of simulations to perform

        :return: The simulations of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :rtype: int
        """
        return self._simulations

    @simulations.setter
    def simulations(self, simulations):
        """Sets the simulations of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The number of simulations to perform

        :param simulations: The simulations of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :type simulations: int
        """
        if simulations is not None and simulations < 1:
            raise ValueError("Invalid value for `simulations`, must be a value greater than or equal to `1`")

        self._simulations = simulations

    @property
    def simulations_length(self):
        """Gets the simulations_length of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The number of time period(s) to simulate per simulation

        :return: The simulations_length of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :rtype: int
        """
        return self._simulations_length

    @simulations_length.setter
    def simulations_length(self, simulations_length):
        """Sets the simulations_length of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.

        The number of time period(s) to simulate per simulation

        :param simulations_length: The simulations_length of this AssetsReturnsSimulationMonteCarloGaussianPostRequest.
        :type simulations_length: int
        """
        if simulations_length is not None and simulations_length < 1:
            raise ValueError("Invalid value for `simulations_length`, must be a value greater than or equal to `1`")

        self._simulations_length = simulations_length
