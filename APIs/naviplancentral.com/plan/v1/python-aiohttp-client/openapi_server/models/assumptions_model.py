# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_assumptions import IAssumptions
from openapi_server.models.object_link import ObjectLink
from openapi_server import util


class AssumptionsModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assumptions: IAssumptions=None, links: List[ObjectLink]=None):
        """AssumptionsModel - a model defined in OpenAPI

        :param assumptions: The assumptions of this AssumptionsModel.
        :param links: The links of this AssumptionsModel.
        """
        self.openapi_types = {
            'assumptions': IAssumptions,
            'links': List[ObjectLink]
        }

        self.attribute_map = {
            'assumptions': 'assumptions',
            'links': 'links'
        }

        self._assumptions = assumptions
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AssumptionsModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AssumptionsModel of this AssumptionsModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assumptions(self):
        """Gets the assumptions of this AssumptionsModel.


        :return: The assumptions of this AssumptionsModel.
        :rtype: IAssumptions
        """
        return self._assumptions

    @assumptions.setter
    def assumptions(self, assumptions):
        """Sets the assumptions of this AssumptionsModel.


        :param assumptions: The assumptions of this AssumptionsModel.
        :type assumptions: IAssumptions
        """

        self._assumptions = assumptions

    @property
    def links(self):
        """Gets the links of this AssumptionsModel.


        :return: The links of this AssumptionsModel.
        :rtype: List[ObjectLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssumptionsModel.


        :param links: The links of this AssumptionsModel.
        :type links: List[ObjectLink]
        """

        self._links = links
