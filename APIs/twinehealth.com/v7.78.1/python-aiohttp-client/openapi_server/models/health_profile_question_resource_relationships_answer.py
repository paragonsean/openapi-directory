# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.action_resource_relationships_plan_data import ActionResourceRelationshipsPlanData
from openapi_server.models.health_profile_question_resource_relationships_answer_links import HealthProfileQuestionResourceRelationshipsAnswerLinks
from openapi_server import util


class HealthProfileQuestionResourceRelationshipsAnswer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: ActionResourceRelationshipsPlanData=None, links: HealthProfileQuestionResourceRelationshipsAnswerLinks=None):
        """HealthProfileQuestionResourceRelationshipsAnswer - a model defined in OpenAPI

        :param data: The data of this HealthProfileQuestionResourceRelationshipsAnswer.
        :param links: The links of this HealthProfileQuestionResourceRelationshipsAnswer.
        """
        self.openapi_types = {
            'data': ActionResourceRelationshipsPlanData,
            'links': HealthProfileQuestionResourceRelationshipsAnswerLinks
        }

        self.attribute_map = {
            'data': 'data',
            'links': 'links'
        }

        self._data = data
        self._links = links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HealthProfileQuestionResourceRelationshipsAnswer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HealthProfileQuestionResource_relationships_answer of this HealthProfileQuestionResourceRelationshipsAnswer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this HealthProfileQuestionResourceRelationshipsAnswer.


        :return: The data of this HealthProfileQuestionResourceRelationshipsAnswer.
        :rtype: ActionResourceRelationshipsPlanData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this HealthProfileQuestionResourceRelationshipsAnswer.


        :param data: The data of this HealthProfileQuestionResourceRelationshipsAnswer.
        :type data: ActionResourceRelationshipsPlanData
        """

        self._data = data

    @property
    def links(self):
        """Gets the links of this HealthProfileQuestionResourceRelationshipsAnswer.


        :return: The links of this HealthProfileQuestionResourceRelationshipsAnswer.
        :rtype: HealthProfileQuestionResourceRelationshipsAnswerLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this HealthProfileQuestionResourceRelationshipsAnswer.


        :param links: The links of this HealthProfileQuestionResourceRelationshipsAnswer.
        :type links: HealthProfileQuestionResourceRelationshipsAnswerLinks
        """

        self._links = links
