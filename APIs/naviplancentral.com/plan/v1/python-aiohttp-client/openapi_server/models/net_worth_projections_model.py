# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.net_worth_projection_model import NetWorthProjectionModel
from openapi_server.models.object_link import ObjectLink
from openapi_server import util


class NetWorthProjectionsModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: List[ObjectLink]=None, projections: List[NetWorthProjectionModel]=None):
        """NetWorthProjectionsModel - a model defined in OpenAPI

        :param links: The links of this NetWorthProjectionsModel.
        :param projections: The projections of this NetWorthProjectionsModel.
        """
        self.openapi_types = {
            'links': List[ObjectLink],
            'projections': List[NetWorthProjectionModel]
        }

        self.attribute_map = {
            'links': 'links',
            'projections': 'projections'
        }

        self._links = links
        self._projections = projections

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NetWorthProjectionsModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NetWorthProjectionsModel of this NetWorthProjectionsModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this NetWorthProjectionsModel.


        :return: The links of this NetWorthProjectionsModel.
        :rtype: List[ObjectLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NetWorthProjectionsModel.


        :param links: The links of this NetWorthProjectionsModel.
        :type links: List[ObjectLink]
        """

        self._links = links

    @property
    def projections(self):
        """Gets the projections of this NetWorthProjectionsModel.


        :return: The projections of this NetWorthProjectionsModel.
        :rtype: List[NetWorthProjectionModel]
        """
        return self._projections

    @projections.setter
    def projections(self, projections):
        """Sets the projections of this NetWorthProjectionsModel.


        :param projections: The projections of this NetWorthProjectionsModel.
        :type projections: List[NetWorthProjectionModel]
        """

        self._projections = projections
