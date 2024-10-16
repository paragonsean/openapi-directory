# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RetirementGoalModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, external_destination_id: str=None, fact_finder_id: int=None, head1_retirement_date: datetime=None, head2_retirement_date: datetime=None):
        """RetirementGoalModel - a model defined in OpenAPI

        :param external_destination_id: The external_destination_id of this RetirementGoalModel.
        :param fact_finder_id: The fact_finder_id of this RetirementGoalModel.
        :param head1_retirement_date: The head1_retirement_date of this RetirementGoalModel.
        :param head2_retirement_date: The head2_retirement_date of this RetirementGoalModel.
        """
        self.openapi_types = {
            'external_destination_id': str,
            'fact_finder_id': int,
            'head1_retirement_date': datetime,
            'head2_retirement_date': datetime
        }

        self.attribute_map = {
            'external_destination_id': 'externalDestinationId',
            'fact_finder_id': 'factFinderId',
            'head1_retirement_date': 'head1RetirementDate',
            'head2_retirement_date': 'head2RetirementDate'
        }

        self._external_destination_id = external_destination_id
        self._fact_finder_id = fact_finder_id
        self._head1_retirement_date = head1_retirement_date
        self._head2_retirement_date = head2_retirement_date

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RetirementGoalModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RetirementGoalModel of this RetirementGoalModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def external_destination_id(self):
        """Gets the external_destination_id of this RetirementGoalModel.


        :return: The external_destination_id of this RetirementGoalModel.
        :rtype: str
        """
        return self._external_destination_id

    @external_destination_id.setter
    def external_destination_id(self, external_destination_id):
        """Sets the external_destination_id of this RetirementGoalModel.


        :param external_destination_id: The external_destination_id of this RetirementGoalModel.
        :type external_destination_id: str
        """
        if external_destination_id is not None and len(external_destination_id) > 64:
            raise ValueError("Invalid value for `external_destination_id`, length must be less than or equal to `64`")
        if external_destination_id is not None and len(external_destination_id) < 0:
            raise ValueError("Invalid value for `external_destination_id`, length must be greater than or equal to `0`")

        self._external_destination_id = external_destination_id

    @property
    def fact_finder_id(self):
        """Gets the fact_finder_id of this RetirementGoalModel.


        :return: The fact_finder_id of this RetirementGoalModel.
        :rtype: int
        """
        return self._fact_finder_id

    @fact_finder_id.setter
    def fact_finder_id(self, fact_finder_id):
        """Sets the fact_finder_id of this RetirementGoalModel.


        :param fact_finder_id: The fact_finder_id of this RetirementGoalModel.
        :type fact_finder_id: int
        """
        if fact_finder_id is None:
            raise ValueError("Invalid value for `fact_finder_id`, must not be `None`")

        self._fact_finder_id = fact_finder_id

    @property
    def head1_retirement_date(self):
        """Gets the head1_retirement_date of this RetirementGoalModel.


        :return: The head1_retirement_date of this RetirementGoalModel.
        :rtype: datetime
        """
        return self._head1_retirement_date

    @head1_retirement_date.setter
    def head1_retirement_date(self, head1_retirement_date):
        """Sets the head1_retirement_date of this RetirementGoalModel.


        :param head1_retirement_date: The head1_retirement_date of this RetirementGoalModel.
        :type head1_retirement_date: datetime
        """

        self._head1_retirement_date = head1_retirement_date

    @property
    def head2_retirement_date(self):
        """Gets the head2_retirement_date of this RetirementGoalModel.


        :return: The head2_retirement_date of this RetirementGoalModel.
        :rtype: datetime
        """
        return self._head2_retirement_date

    @head2_retirement_date.setter
    def head2_retirement_date(self, head2_retirement_date):
        """Sets the head2_retirement_date of this RetirementGoalModel.


        :param head2_retirement_date: The head2_retirement_date of this RetirementGoalModel.
        :type head2_retirement_date: datetime
        """

        self._head2_retirement_date = head2_retirement_date
