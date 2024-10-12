# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.day_of_execution import DayOfExecution
from openapi_server.models.execution_rule import ExecutionRule
from openapi_server.models.frequency_code import FrequencyCode
from openapi_server import util


class PeriodicPaymentInitiationXmlPart2StandingorderTypeJson(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, day_of_execution: DayOfExecution=None, end_date: date=None, execution_rule: ExecutionRule=None, frequency: FrequencyCode=None, start_date: date=None):
        """PeriodicPaymentInitiationXmlPart2StandingorderTypeJson - a model defined in OpenAPI

        :param day_of_execution: The day_of_execution of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :param end_date: The end_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :param execution_rule: The execution_rule of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :param frequency: The frequency of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :param start_date: The start_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        """
        self.openapi_types = {
            'day_of_execution': DayOfExecution,
            'end_date': date,
            'execution_rule': ExecutionRule,
            'frequency': FrequencyCode,
            'start_date': date
        }

        self.attribute_map = {
            'day_of_execution': 'dayOfExecution',
            'end_date': 'endDate',
            'execution_rule': 'executionRule',
            'frequency': 'frequency',
            'start_date': 'startDate'
        }

        self._day_of_execution = day_of_execution
        self._end_date = end_date
        self._execution_rule = execution_rule
        self._frequency = frequency
        self._start_date = start_date

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PeriodicPaymentInitiationXmlPart2StandingorderTypeJson':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The periodicPaymentInitiation_xml-Part2-standingorderType_json of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def day_of_execution(self):
        """Gets the day_of_execution of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.


        :return: The day_of_execution of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :rtype: DayOfExecution
        """
        return self._day_of_execution

    @day_of_execution.setter
    def day_of_execution(self, day_of_execution):
        """Sets the day_of_execution of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.


        :param day_of_execution: The day_of_execution of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :type day_of_execution: DayOfExecution
        """

        self._day_of_execution = day_of_execution

    @property
    def end_date(self):
        """Gets the end_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.

        The last applicable day of execution. If not given, it is an infinite standing order. 

        :return: The end_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.

        The last applicable day of execution. If not given, it is an infinite standing order. 

        :param end_date: The end_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def execution_rule(self):
        """Gets the execution_rule of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.


        :return: The execution_rule of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :rtype: ExecutionRule
        """
        return self._execution_rule

    @execution_rule.setter
    def execution_rule(self, execution_rule):
        """Sets the execution_rule of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.


        :param execution_rule: The execution_rule of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :type execution_rule: ExecutionRule
        """

        self._execution_rule = execution_rule

    @property
    def frequency(self):
        """Gets the frequency of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.


        :return: The frequency of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :rtype: FrequencyCode
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.


        :param frequency: The frequency of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :type frequency: FrequencyCode
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")

        self._frequency = frequency

    @property
    def start_date(self):
        """Gets the start_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.

        The first applicable day of execution starting from this date is the first payment. 

        :return: The start_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.

        The first applicable day of execution starting from this date is the first payment. 

        :param start_date: The start_date of this PeriodicPaymentInitiationXmlPart2StandingorderTypeJson.
        :type start_date: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")

        self._start_date = start_date
