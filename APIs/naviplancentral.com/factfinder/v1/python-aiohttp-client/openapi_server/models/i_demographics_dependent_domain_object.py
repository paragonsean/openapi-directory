# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IDemographicsDependentDomainObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, birth_date: datetime=None, demographics_id: int=None, dependent_id: int=None, dependent_of: str=None, external_destination_id: str=None, first_name: str=None, last_name: str=None, relationship: str=None):
        """IDemographicsDependentDomainObject - a model defined in OpenAPI

        :param birth_date: The birth_date of this IDemographicsDependentDomainObject.
        :param demographics_id: The demographics_id of this IDemographicsDependentDomainObject.
        :param dependent_id: The dependent_id of this IDemographicsDependentDomainObject.
        :param dependent_of: The dependent_of of this IDemographicsDependentDomainObject.
        :param external_destination_id: The external_destination_id of this IDemographicsDependentDomainObject.
        :param first_name: The first_name of this IDemographicsDependentDomainObject.
        :param last_name: The last_name of this IDemographicsDependentDomainObject.
        :param relationship: The relationship of this IDemographicsDependentDomainObject.
        """
        self.openapi_types = {
            'birth_date': datetime,
            'demographics_id': int,
            'dependent_id': int,
            'dependent_of': str,
            'external_destination_id': str,
            'first_name': str,
            'last_name': str,
            'relationship': str
        }

        self.attribute_map = {
            'birth_date': 'birthDate',
            'demographics_id': 'demographicsId',
            'dependent_id': 'dependentId',
            'dependent_of': 'dependentOf',
            'external_destination_id': 'externalDestinationId',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'relationship': 'relationship'
        }

        self._birth_date = birth_date
        self._demographics_id = demographics_id
        self._dependent_id = dependent_id
        self._dependent_of = dependent_of
        self._external_destination_id = external_destination_id
        self._first_name = first_name
        self._last_name = last_name
        self._relationship = relationship

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IDemographicsDependentDomainObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IDemographicsDependentDomainObject of this IDemographicsDependentDomainObject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def birth_date(self):
        """Gets the birth_date of this IDemographicsDependentDomainObject.


        :return: The birth_date of this IDemographicsDependentDomainObject.
        :rtype: datetime
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this IDemographicsDependentDomainObject.


        :param birth_date: The birth_date of this IDemographicsDependentDomainObject.
        :type birth_date: datetime
        """

        self._birth_date = birth_date

    @property
    def demographics_id(self):
        """Gets the demographics_id of this IDemographicsDependentDomainObject.


        :return: The demographics_id of this IDemographicsDependentDomainObject.
        :rtype: int
        """
        return self._demographics_id

    @demographics_id.setter
    def demographics_id(self, demographics_id):
        """Sets the demographics_id of this IDemographicsDependentDomainObject.


        :param demographics_id: The demographics_id of this IDemographicsDependentDomainObject.
        :type demographics_id: int
        """

        self._demographics_id = demographics_id

    @property
    def dependent_id(self):
        """Gets the dependent_id of this IDemographicsDependentDomainObject.


        :return: The dependent_id of this IDemographicsDependentDomainObject.
        :rtype: int
        """
        return self._dependent_id

    @dependent_id.setter
    def dependent_id(self, dependent_id):
        """Sets the dependent_id of this IDemographicsDependentDomainObject.


        :param dependent_id: The dependent_id of this IDemographicsDependentDomainObject.
        :type dependent_id: int
        """

        self._dependent_id = dependent_id

    @property
    def dependent_of(self):
        """Gets the dependent_of of this IDemographicsDependentDomainObject.


        :return: The dependent_of of this IDemographicsDependentDomainObject.
        :rtype: str
        """
        return self._dependent_of

    @dependent_of.setter
    def dependent_of(self, dependent_of):
        """Sets the dependent_of of this IDemographicsDependentDomainObject.


        :param dependent_of: The dependent_of of this IDemographicsDependentDomainObject.
        :type dependent_of: str
        """
        allowed_values = ["Client", "CoClient", "Joint", "Other"]  # noqa: E501
        if dependent_of not in allowed_values:
            raise ValueError(
                "Invalid value for `dependent_of` ({0}), must be one of {1}"
                .format(dependent_of, allowed_values)
            )

        self._dependent_of = dependent_of

    @property
    def external_destination_id(self):
        """Gets the external_destination_id of this IDemographicsDependentDomainObject.


        :return: The external_destination_id of this IDemographicsDependentDomainObject.
        :rtype: str
        """
        return self._external_destination_id

    @external_destination_id.setter
    def external_destination_id(self, external_destination_id):
        """Sets the external_destination_id of this IDemographicsDependentDomainObject.


        :param external_destination_id: The external_destination_id of this IDemographicsDependentDomainObject.
        :type external_destination_id: str
        """

        self._external_destination_id = external_destination_id

    @property
    def first_name(self):
        """Gets the first_name of this IDemographicsDependentDomainObject.


        :return: The first_name of this IDemographicsDependentDomainObject.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this IDemographicsDependentDomainObject.


        :param first_name: The first_name of this IDemographicsDependentDomainObject.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this IDemographicsDependentDomainObject.


        :return: The last_name of this IDemographicsDependentDomainObject.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this IDemographicsDependentDomainObject.


        :param last_name: The last_name of this IDemographicsDependentDomainObject.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def relationship(self):
        """Gets the relationship of this IDemographicsDependentDomainObject.


        :return: The relationship of this IDemographicsDependentDomainObject.
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this IDemographicsDependentDomainObject.


        :param relationship: The relationship of this IDemographicsDependentDomainObject.
        :type relationship: str
        """
        allowed_values = ["Son", "Daughter", "FosterSon", "FosterDaughter", "Grandson", "Granddaughter", "Nephew", "Niece", "MaleCousin", "FemaleCousin", "Father", "Mother", "Grandfather", "Grandmother", "Uncle", "Aunt", "Brother", "Sister", "SonInLaw", "DaughterInLaw", "MaleOther", "FemaleOther"]  # noqa: E501
        if relationship not in allowed_values:
            raise ValueError(
                "Invalid value for `relationship` ({0}), must be one of {1}"
                .format(relationship, allowed_values)
            )

        self._relationship = relationship
