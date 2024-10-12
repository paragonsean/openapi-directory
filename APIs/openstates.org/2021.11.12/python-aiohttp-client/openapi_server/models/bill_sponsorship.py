# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.compact_person import CompactPerson
from openapi_server.models.organization import Organization
from openapi_server import util


class BillSponsorship(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, classification: str=None, entity_type: str=None, name: str=None, organization: Organization=None, person: CompactPerson=None, primary: bool=None):
        """BillSponsorship - a model defined in OpenAPI

        :param classification: The classification of this BillSponsorship.
        :param entity_type: The entity_type of this BillSponsorship.
        :param name: The name of this BillSponsorship.
        :param organization: The organization of this BillSponsorship.
        :param person: The person of this BillSponsorship.
        :param primary: The primary of this BillSponsorship.
        """
        self.openapi_types = {
            'classification': str,
            'entity_type': str,
            'name': str,
            'organization': Organization,
            'person': CompactPerson,
            'primary': bool
        }

        self.attribute_map = {
            'classification': 'classification',
            'entity_type': 'entity_type',
            'name': 'name',
            'organization': 'organization',
            'person': 'person',
            'primary': 'primary'
        }

        self._classification = classification
        self._entity_type = entity_type
        self._name = name
        self._organization = organization
        self._person = person
        self._primary = primary

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BillSponsorship':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BillSponsorship of this BillSponsorship.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def classification(self):
        """Gets the classification of this BillSponsorship.


        :return: The classification of this BillSponsorship.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this BillSponsorship.


        :param classification: The classification of this BillSponsorship.
        :type classification: str
        """
        if classification is None:
            raise ValueError("Invalid value for `classification`, must not be `None`")

        self._classification = classification

    @property
    def entity_type(self):
        """Gets the entity_type of this BillSponsorship.


        :return: The entity_type of this BillSponsorship.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this BillSponsorship.


        :param entity_type: The entity_type of this BillSponsorship.
        :type entity_type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this BillSponsorship.


        :return: The name of this BillSponsorship.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillSponsorship.


        :param name: The name of this BillSponsorship.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this BillSponsorship.


        :return: The organization of this BillSponsorship.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this BillSponsorship.


        :param organization: The organization of this BillSponsorship.
        :type organization: Organization
        """

        self._organization = organization

    @property
    def person(self):
        """Gets the person of this BillSponsorship.


        :return: The person of this BillSponsorship.
        :rtype: CompactPerson
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this BillSponsorship.


        :param person: The person of this BillSponsorship.
        :type person: CompactPerson
        """

        self._person = person

    @property
    def primary(self):
        """Gets the primary of this BillSponsorship.


        :return: The primary of this BillSponsorship.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this BillSponsorship.


        :param primary: The primary of this BillSponsorship.
        :type primary: bool
        """
        if primary is None:
            raise ValueError("Invalid value for `primary`, must not be `None`")

        self._primary = primary
