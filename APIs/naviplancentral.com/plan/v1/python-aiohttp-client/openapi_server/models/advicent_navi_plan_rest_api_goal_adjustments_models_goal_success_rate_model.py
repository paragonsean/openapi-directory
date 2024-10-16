# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, goal_id: int=None, success_rate: float=None):
        """AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel - a model defined in OpenAPI

        :param description: The description of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :param goal_id: The goal_id of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :param success_rate: The success_rate of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        """
        self.openapi_types = {
            'description': str,
            'goal_id': int,
            'success_rate': float
        }

        self.attribute_map = {
            'description': 'description',
            'goal_id': 'goalId',
            'success_rate': 'successRate'
        }

        self._description = description
        self._goal_id = goal_id
        self._success_rate = success_rate

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.


        :return: The description of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.


        :param description: The description of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :type description: str
        """

        self._description = description

    @property
    def goal_id(self):
        """Gets the goal_id of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.


        :return: The goal_id of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :rtype: int
        """
        return self._goal_id

    @goal_id.setter
    def goal_id(self, goal_id):
        """Sets the goal_id of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.


        :param goal_id: The goal_id of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :type goal_id: int
        """

        self._goal_id = goal_id

    @property
    def success_rate(self):
        """Gets the success_rate of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.


        :return: The success_rate of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.


        :param success_rate: The success_rate of this AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.
        :type success_rate: float
        """

        self._success_rate = success_rate
