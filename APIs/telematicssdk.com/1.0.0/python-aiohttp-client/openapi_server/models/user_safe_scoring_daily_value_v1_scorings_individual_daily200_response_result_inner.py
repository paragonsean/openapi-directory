# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, acceleration_score: float=None, app_id: str=None, braking_score: float=None, calc_date: str=None, company_id: str=None, cornering_score: float=None, device_token: str=None, distracted_score: float=None, instance_id: str=None, overall_score: float=None, speeding_score: float=None):
        """UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner - a model defined in OpenAPI

        :param acceleration_score: The acceleration_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param app_id: The app_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param braking_score: The braking_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param calc_date: The calc_date of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param company_id: The company_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param cornering_score: The cornering_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param device_token: The device_token of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param distracted_score: The distracted_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param instance_id: The instance_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param overall_score: The overall_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :param speeding_score: The speeding_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        """
        self.openapi_types = {
            'acceleration_score': float,
            'app_id': str,
            'braking_score': float,
            'calc_date': str,
            'company_id': str,
            'cornering_score': float,
            'device_token': str,
            'distracted_score': float,
            'instance_id': str,
            'overall_score': float,
            'speeding_score': float
        }

        self.attribute_map = {
            'acceleration_score': 'AccelerationScore',
            'app_id': 'AppId',
            'braking_score': 'BrakingScore',
            'calc_date': 'CalcDate',
            'company_id': 'CompanyId',
            'cornering_score': 'CorneringScore',
            'device_token': 'DeviceToken',
            'distracted_score': 'DistractedScore',
            'instance_id': 'InstanceId',
            'overall_score': 'OverallScore',
            'speeding_score': 'SpeedingScore'
        }

        self._acceleration_score = acceleration_score
        self._app_id = app_id
        self._braking_score = braking_score
        self._calc_date = calc_date
        self._company_id = company_id
        self._cornering_score = cornering_score
        self._device_token = device_token
        self._distracted_score = distracted_score
        self._instance_id = instance_id
        self._overall_score = overall_score
        self._speeding_score = speeding_score

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The userSafeScoringDailyValue_v1_scorings_individual_daily_200_response_Result_inner of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def acceleration_score(self):
        """Gets the acceleration_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The acceleration_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: float
        """
        return self._acceleration_score

    @acceleration_score.setter
    def acceleration_score(self, acceleration_score):
        """Sets the acceleration_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param acceleration_score: The acceleration_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type acceleration_score: float
        """

        self._acceleration_score = acceleration_score

    @property
    def app_id(self):
        """Gets the app_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The app_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param app_id: The app_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def braking_score(self):
        """Gets the braking_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The braking_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: float
        """
        return self._braking_score

    @braking_score.setter
    def braking_score(self, braking_score):
        """Sets the braking_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param braking_score: The braking_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type braking_score: float
        """

        self._braking_score = braking_score

    @property
    def calc_date(self):
        """Gets the calc_date of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The calc_date of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: str
        """
        return self._calc_date

    @calc_date.setter
    def calc_date(self, calc_date):
        """Sets the calc_date of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param calc_date: The calc_date of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type calc_date: str
        """

        self._calc_date = calc_date

    @property
    def company_id(self):
        """Gets the company_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The company_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param company_id: The company_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type company_id: str
        """

        self._company_id = company_id

    @property
    def cornering_score(self):
        """Gets the cornering_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The cornering_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: float
        """
        return self._cornering_score

    @cornering_score.setter
    def cornering_score(self, cornering_score):
        """Sets the cornering_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param cornering_score: The cornering_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type cornering_score: float
        """

        self._cornering_score = cornering_score

    @property
    def device_token(self):
        """Gets the device_token of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The device_token of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: str
        """
        return self._device_token

    @device_token.setter
    def device_token(self, device_token):
        """Sets the device_token of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param device_token: The device_token of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type device_token: str
        """

        self._device_token = device_token

    @property
    def distracted_score(self):
        """Gets the distracted_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The distracted_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: float
        """
        return self._distracted_score

    @distracted_score.setter
    def distracted_score(self, distracted_score):
        """Sets the distracted_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param distracted_score: The distracted_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type distracted_score: float
        """

        self._distracted_score = distracted_score

    @property
    def instance_id(self):
        """Gets the instance_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The instance_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param instance_id: The instance_id of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type instance_id: str
        """

        self._instance_id = instance_id

    @property
    def overall_score(self):
        """Gets the overall_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The overall_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: float
        """
        return self._overall_score

    @overall_score.setter
    def overall_score(self, overall_score):
        """Sets the overall_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param overall_score: The overall_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type overall_score: float
        """

        self._overall_score = overall_score

    @property
    def speeding_score(self):
        """Gets the speeding_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :return: The speeding_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :rtype: float
        """
        return self._speeding_score

    @speeding_score.setter
    def speeding_score(self, speeding_score):
        """Sets the speeding_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.


        :param speeding_score: The speeding_score of this UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.
        :type speeding_score: float
        """

        self._speeding_score = speeding_score
