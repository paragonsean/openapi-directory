# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.assets_returns_simulation_bootstrap_post200_response_simulations_inner import AssetsReturnsSimulationBootstrapPost200ResponseSimulationsInner
from openapi_server import util


class AssetsReturnsSimulationBootstrapPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, simulations: List[AssetsReturnsSimulationBootstrapPost200ResponseSimulationsInner]=None):
        """AssetsReturnsSimulationBootstrapPost200Response - a model defined in OpenAPI

        :param simulations: The simulations of this AssetsReturnsSimulationBootstrapPost200Response.
        """
        self.openapi_types = {
            'simulations': List[AssetsReturnsSimulationBootstrapPost200ResponseSimulationsInner]
        }

        self.attribute_map = {
            'simulations': 'simulations'
        }

        self._simulations = simulations

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssetsReturnsSimulationBootstrapPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _assets_returns_simulation_bootstrap_post_200_response of this AssetsReturnsSimulationBootstrapPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def simulations(self):
        """Gets the simulations of this AssetsReturnsSimulationBootstrapPost200Response.


        :return: The simulations of this AssetsReturnsSimulationBootstrapPost200Response.
        :rtype: List[AssetsReturnsSimulationBootstrapPost200ResponseSimulationsInner]
        """
        return self._simulations

    @simulations.setter
    def simulations(self, simulations):
        """Sets the simulations of this AssetsReturnsSimulationBootstrapPost200Response.


        :param simulations: The simulations of this AssetsReturnsSimulationBootstrapPost200Response.
        :type simulations: List[AssetsReturnsSimulationBootstrapPost200ResponseSimulationsInner]
        """
        if simulations is None:
            raise ValueError("Invalid value for `simulations`, must not be `None`")

        self._simulations = simulations
