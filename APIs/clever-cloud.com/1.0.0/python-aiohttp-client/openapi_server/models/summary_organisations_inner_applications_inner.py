# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SummaryOrganisationsInnerApplicationsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, archived: bool=False, commit: str=None, id: str=None, instance_type: str=None, instance_variant: str=None, name: str=None, state: str=None, variant_slug: str=None):
        """SummaryOrganisationsInnerApplicationsInner - a model defined in OpenAPI

        :param archived: The archived of this SummaryOrganisationsInnerApplicationsInner.
        :param commit: The commit of this SummaryOrganisationsInnerApplicationsInner.
        :param id: The id of this SummaryOrganisationsInnerApplicationsInner.
        :param instance_type: The instance_type of this SummaryOrganisationsInnerApplicationsInner.
        :param instance_variant: The instance_variant of this SummaryOrganisationsInnerApplicationsInner.
        :param name: The name of this SummaryOrganisationsInnerApplicationsInner.
        :param state: The state of this SummaryOrganisationsInnerApplicationsInner.
        :param variant_slug: The variant_slug of this SummaryOrganisationsInnerApplicationsInner.
        """
        self.openapi_types = {
            'archived': bool,
            'commit': str,
            'id': str,
            'instance_type': str,
            'instance_variant': str,
            'name': str,
            'state': str,
            'variant_slug': str
        }

        self.attribute_map = {
            'archived': 'archived',
            'commit': 'commit',
            'id': 'id',
            'instance_type': 'instanceType',
            'instance_variant': 'instanceVariant',
            'name': 'name',
            'state': 'state',
            'variant_slug': 'variantSlug'
        }

        self._archived = archived
        self._commit = commit
        self._id = id
        self._instance_type = instance_type
        self._instance_variant = instance_variant
        self._name = name
        self._state = state
        self._variant_slug = variant_slug

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SummaryOrganisationsInnerApplicationsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Summary_organisations_inner_applications_inner of this SummaryOrganisationsInnerApplicationsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def archived(self):
        """Gets the archived of this SummaryOrganisationsInnerApplicationsInner.


        :return: The archived of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SummaryOrganisationsInnerApplicationsInner.


        :param archived: The archived of this SummaryOrganisationsInnerApplicationsInner.
        :type archived: bool
        """

        self._archived = archived

    @property
    def commit(self):
        """Gets the commit of this SummaryOrganisationsInnerApplicationsInner.


        :return: The commit of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this SummaryOrganisationsInnerApplicationsInner.


        :param commit: The commit of this SummaryOrganisationsInnerApplicationsInner.
        :type commit: str
        """

        self._commit = commit

    @property
    def id(self):
        """Gets the id of this SummaryOrganisationsInnerApplicationsInner.


        :return: The id of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SummaryOrganisationsInnerApplicationsInner.


        :param id: The id of this SummaryOrganisationsInnerApplicationsInner.
        :type id: str
        """

        self._id = id

    @property
    def instance_type(self):
        """Gets the instance_type of this SummaryOrganisationsInnerApplicationsInner.


        :return: The instance_type of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this SummaryOrganisationsInnerApplicationsInner.


        :param instance_type: The instance_type of this SummaryOrganisationsInnerApplicationsInner.
        :type instance_type: str
        """

        self._instance_type = instance_type

    @property
    def instance_variant(self):
        """Gets the instance_variant of this SummaryOrganisationsInnerApplicationsInner.


        :return: The instance_variant of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: str
        """
        return self._instance_variant

    @instance_variant.setter
    def instance_variant(self, instance_variant):
        """Sets the instance_variant of this SummaryOrganisationsInnerApplicationsInner.


        :param instance_variant: The instance_variant of this SummaryOrganisationsInnerApplicationsInner.
        :type instance_variant: str
        """

        self._instance_variant = instance_variant

    @property
    def name(self):
        """Gets the name of this SummaryOrganisationsInnerApplicationsInner.


        :return: The name of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SummaryOrganisationsInnerApplicationsInner.


        :param name: The name of this SummaryOrganisationsInnerApplicationsInner.
        :type name: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this SummaryOrganisationsInnerApplicationsInner.


        :return: The state of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SummaryOrganisationsInnerApplicationsInner.


        :param state: The state of this SummaryOrganisationsInnerApplicationsInner.
        :type state: str
        """

        self._state = state

    @property
    def variant_slug(self):
        """Gets the variant_slug of this SummaryOrganisationsInnerApplicationsInner.


        :return: The variant_slug of this SummaryOrganisationsInnerApplicationsInner.
        :rtype: str
        """
        return self._variant_slug

    @variant_slug.setter
    def variant_slug(self, variant_slug):
        """Sets the variant_slug of this SummaryOrganisationsInnerApplicationsInner.


        :param variant_slug: The variant_slug of this SummaryOrganisationsInnerApplicationsInner.
        :type variant_slug: str
        """

        self._variant_slug = variant_slug
