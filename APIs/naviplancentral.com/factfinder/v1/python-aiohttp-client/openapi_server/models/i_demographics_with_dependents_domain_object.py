# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_demographics_dependent_domain_object import IDemographicsDependentDomainObject
from openapi_server.models.i_family_head_domain_object import IFamilyHeadDomainObject
from openapi_server import util


class IDemographicsWithDependentsDomainObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city: str=None, created: datetime=None, demographics_id: int=None, dependents: List[IDemographicsDependentDomainObject]=None, external_destination_id: str=None, external_source_id: str=None, fact_finder_id: int=None, head1: IFamilyHeadDomainObject=None, head2: IFamilyHeadDomainObject=None, joint_analysis: bool=None, lock_retirement: bool=None, state: int=None):
        """IDemographicsWithDependentsDomainObject - a model defined in OpenAPI

        :param city: The city of this IDemographicsWithDependentsDomainObject.
        :param created: The created of this IDemographicsWithDependentsDomainObject.
        :param demographics_id: The demographics_id of this IDemographicsWithDependentsDomainObject.
        :param dependents: The dependents of this IDemographicsWithDependentsDomainObject.
        :param external_destination_id: The external_destination_id of this IDemographicsWithDependentsDomainObject.
        :param external_source_id: The external_source_id of this IDemographicsWithDependentsDomainObject.
        :param fact_finder_id: The fact_finder_id of this IDemographicsWithDependentsDomainObject.
        :param head1: The head1 of this IDemographicsWithDependentsDomainObject.
        :param head2: The head2 of this IDemographicsWithDependentsDomainObject.
        :param joint_analysis: The joint_analysis of this IDemographicsWithDependentsDomainObject.
        :param lock_retirement: The lock_retirement of this IDemographicsWithDependentsDomainObject.
        :param state: The state of this IDemographicsWithDependentsDomainObject.
        """
        self.openapi_types = {
            'city': str,
            'created': datetime,
            'demographics_id': int,
            'dependents': List[IDemographicsDependentDomainObject],
            'external_destination_id': str,
            'external_source_id': str,
            'fact_finder_id': int,
            'head1': IFamilyHeadDomainObject,
            'head2': IFamilyHeadDomainObject,
            'joint_analysis': bool,
            'lock_retirement': bool,
            'state': int
        }

        self.attribute_map = {
            'city': 'city',
            'created': 'created',
            'demographics_id': 'demographicsId',
            'dependents': 'dependents',
            'external_destination_id': 'externalDestinationId',
            'external_source_id': 'externalSourceId',
            'fact_finder_id': 'factFinderId',
            'head1': 'head1',
            'head2': 'head2',
            'joint_analysis': 'jointAnalysis',
            'lock_retirement': 'lockRetirement',
            'state': 'state'
        }

        self._city = city
        self._created = created
        self._demographics_id = demographics_id
        self._dependents = dependents
        self._external_destination_id = external_destination_id
        self._external_source_id = external_source_id
        self._fact_finder_id = fact_finder_id
        self._head1 = head1
        self._head2 = head2
        self._joint_analysis = joint_analysis
        self._lock_retirement = lock_retirement
        self._state = state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IDemographicsWithDependentsDomainObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IDemographicsWithDependentsDomainObject of this IDemographicsWithDependentsDomainObject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self):
        """Gets the city of this IDemographicsWithDependentsDomainObject.


        :return: The city of this IDemographicsWithDependentsDomainObject.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this IDemographicsWithDependentsDomainObject.


        :param city: The city of this IDemographicsWithDependentsDomainObject.
        :type city: str
        """

        self._city = city

    @property
    def created(self):
        """Gets the created of this IDemographicsWithDependentsDomainObject.


        :return: The created of this IDemographicsWithDependentsDomainObject.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this IDemographicsWithDependentsDomainObject.


        :param created: The created of this IDemographicsWithDependentsDomainObject.
        :type created: datetime
        """

        self._created = created

    @property
    def demographics_id(self):
        """Gets the demographics_id of this IDemographicsWithDependentsDomainObject.


        :return: The demographics_id of this IDemographicsWithDependentsDomainObject.
        :rtype: int
        """
        return self._demographics_id

    @demographics_id.setter
    def demographics_id(self, demographics_id):
        """Sets the demographics_id of this IDemographicsWithDependentsDomainObject.


        :param demographics_id: The demographics_id of this IDemographicsWithDependentsDomainObject.
        :type demographics_id: int
        """

        self._demographics_id = demographics_id

    @property
    def dependents(self):
        """Gets the dependents of this IDemographicsWithDependentsDomainObject.


        :return: The dependents of this IDemographicsWithDependentsDomainObject.
        :rtype: List[IDemographicsDependentDomainObject]
        """
        return self._dependents

    @dependents.setter
    def dependents(self, dependents):
        """Sets the dependents of this IDemographicsWithDependentsDomainObject.


        :param dependents: The dependents of this IDemographicsWithDependentsDomainObject.
        :type dependents: List[IDemographicsDependentDomainObject]
        """

        self._dependents = dependents

    @property
    def external_destination_id(self):
        """Gets the external_destination_id of this IDemographicsWithDependentsDomainObject.


        :return: The external_destination_id of this IDemographicsWithDependentsDomainObject.
        :rtype: str
        """
        return self._external_destination_id

    @external_destination_id.setter
    def external_destination_id(self, external_destination_id):
        """Sets the external_destination_id of this IDemographicsWithDependentsDomainObject.


        :param external_destination_id: The external_destination_id of this IDemographicsWithDependentsDomainObject.
        :type external_destination_id: str
        """

        self._external_destination_id = external_destination_id

    @property
    def external_source_id(self):
        """Gets the external_source_id of this IDemographicsWithDependentsDomainObject.


        :return: The external_source_id of this IDemographicsWithDependentsDomainObject.
        :rtype: str
        """
        return self._external_source_id

    @external_source_id.setter
    def external_source_id(self, external_source_id):
        """Sets the external_source_id of this IDemographicsWithDependentsDomainObject.


        :param external_source_id: The external_source_id of this IDemographicsWithDependentsDomainObject.
        :type external_source_id: str
        """

        self._external_source_id = external_source_id

    @property
    def fact_finder_id(self):
        """Gets the fact_finder_id of this IDemographicsWithDependentsDomainObject.


        :return: The fact_finder_id of this IDemographicsWithDependentsDomainObject.
        :rtype: int
        """
        return self._fact_finder_id

    @fact_finder_id.setter
    def fact_finder_id(self, fact_finder_id):
        """Sets the fact_finder_id of this IDemographicsWithDependentsDomainObject.


        :param fact_finder_id: The fact_finder_id of this IDemographicsWithDependentsDomainObject.
        :type fact_finder_id: int
        """

        self._fact_finder_id = fact_finder_id

    @property
    def head1(self):
        """Gets the head1 of this IDemographicsWithDependentsDomainObject.


        :return: The head1 of this IDemographicsWithDependentsDomainObject.
        :rtype: IFamilyHeadDomainObject
        """
        return self._head1

    @head1.setter
    def head1(self, head1):
        """Sets the head1 of this IDemographicsWithDependentsDomainObject.


        :param head1: The head1 of this IDemographicsWithDependentsDomainObject.
        :type head1: IFamilyHeadDomainObject
        """

        self._head1 = head1

    @property
    def head2(self):
        """Gets the head2 of this IDemographicsWithDependentsDomainObject.


        :return: The head2 of this IDemographicsWithDependentsDomainObject.
        :rtype: IFamilyHeadDomainObject
        """
        return self._head2

    @head2.setter
    def head2(self, head2):
        """Sets the head2 of this IDemographicsWithDependentsDomainObject.


        :param head2: The head2 of this IDemographicsWithDependentsDomainObject.
        :type head2: IFamilyHeadDomainObject
        """

        self._head2 = head2

    @property
    def joint_analysis(self):
        """Gets the joint_analysis of this IDemographicsWithDependentsDomainObject.


        :return: The joint_analysis of this IDemographicsWithDependentsDomainObject.
        :rtype: bool
        """
        return self._joint_analysis

    @joint_analysis.setter
    def joint_analysis(self, joint_analysis):
        """Sets the joint_analysis of this IDemographicsWithDependentsDomainObject.


        :param joint_analysis: The joint_analysis of this IDemographicsWithDependentsDomainObject.
        :type joint_analysis: bool
        """

        self._joint_analysis = joint_analysis

    @property
    def lock_retirement(self):
        """Gets the lock_retirement of this IDemographicsWithDependentsDomainObject.


        :return: The lock_retirement of this IDemographicsWithDependentsDomainObject.
        :rtype: bool
        """
        return self._lock_retirement

    @lock_retirement.setter
    def lock_retirement(self, lock_retirement):
        """Sets the lock_retirement of this IDemographicsWithDependentsDomainObject.


        :param lock_retirement: The lock_retirement of this IDemographicsWithDependentsDomainObject.
        :type lock_retirement: bool
        """

        self._lock_retirement = lock_retirement

    @property
    def state(self):
        """Gets the state of this IDemographicsWithDependentsDomainObject.


        :return: The state of this IDemographicsWithDependentsDomainObject.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IDemographicsWithDependentsDomainObject.


        :param state: The state of this IDemographicsWithDependentsDomainObject.
        :type state: int
        """

        self._state = state
