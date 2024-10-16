# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.object_link import ObjectLink
from openapi_server.models.projected_annual_summary_model import ProjectedAnnualSummaryModel
from openapi_server import util


class ProjectedAnnualSummariesModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: List[ObjectLink]=None, projections: List[ProjectedAnnualSummaryModel]=None):
        """ProjectedAnnualSummariesModel - a model defined in OpenAPI

        :param links: The links of this ProjectedAnnualSummariesModel.
        :param projections: The projections of this ProjectedAnnualSummariesModel.
        """
        self.openapi_types = {
            'links': List[ObjectLink],
            'projections': List[ProjectedAnnualSummaryModel]
        }

        self.attribute_map = {
            'links': 'links',
            'projections': 'projections'
        }

        self._links = links
        self._projections = projections

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProjectedAnnualSummariesModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProjectedAnnualSummariesModel of this ProjectedAnnualSummariesModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this ProjectedAnnualSummariesModel.


        :return: The links of this ProjectedAnnualSummariesModel.
        :rtype: List[ObjectLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProjectedAnnualSummariesModel.


        :param links: The links of this ProjectedAnnualSummariesModel.
        :type links: List[ObjectLink]
        """

        self._links = links

    @property
    def projections(self):
        """Gets the projections of this ProjectedAnnualSummariesModel.


        :return: The projections of this ProjectedAnnualSummariesModel.
        :rtype: List[ProjectedAnnualSummaryModel]
        """
        return self._projections

    @projections.setter
    def projections(self, projections):
        """Sets the projections of this ProjectedAnnualSummariesModel.


        :param projections: The projections of this ProjectedAnnualSummariesModel.
        :type projections: List[ProjectedAnnualSummaryModel]
        """

        self._projections = projections
