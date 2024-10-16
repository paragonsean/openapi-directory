# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.fact_finder_module_with_id_model import FactFinderModuleWithIdModel
from openapi_server import util


class FactFinderModulesModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fact_finder_modules: List[FactFinderModuleWithIdModel]=None):
        """FactFinderModulesModel - a model defined in OpenAPI

        :param fact_finder_modules: The fact_finder_modules of this FactFinderModulesModel.
        """
        self.openapi_types = {
            'fact_finder_modules': List[FactFinderModuleWithIdModel]
        }

        self.attribute_map = {
            'fact_finder_modules': 'factFinderModules'
        }

        self._fact_finder_modules = fact_finder_modules

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FactFinderModulesModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FactFinderModulesModel of this FactFinderModulesModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fact_finder_modules(self):
        """Gets the fact_finder_modules of this FactFinderModulesModel.


        :return: The fact_finder_modules of this FactFinderModulesModel.
        :rtype: List[FactFinderModuleWithIdModel]
        """
        return self._fact_finder_modules

    @fact_finder_modules.setter
    def fact_finder_modules(self, fact_finder_modules):
        """Sets the fact_finder_modules of this FactFinderModulesModel.


        :param fact_finder_modules: The fact_finder_modules of this FactFinderModulesModel.
        :type fact_finder_modules: List[FactFinderModuleWithIdModel]
        """

        self._fact_finder_modules = fact_finder_modules
