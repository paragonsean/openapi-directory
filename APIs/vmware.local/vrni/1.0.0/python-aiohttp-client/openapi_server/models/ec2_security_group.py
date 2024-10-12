# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.base_security_group import BaseSecurityGroup
from openapi_server.models.entity_type import EntityType
from openapi_server.models.reference import Reference
from openapi_server.models.rule_set import RuleSet
from openapi_server import util


class EC2SecurityGroup(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_id: str=None, entity_type: EntityType=None, name: str=None, members: List[Reference]=None, direct_destination_rules: List[RuleSet]=None, direct_members: List[Reference]=None, direct_source_rules: List[RuleSet]=None, excluded_members: List[Reference]=None, indirect_destination_rules: List[RuleSet]=None, indirect_source_rules: List[RuleSet]=None, parents: List[Reference]=None, translated_vm_count: int=None, vendor_id: str=None, region: str=None, vpc: Reference=None):
        """EC2SecurityGroup - a model defined in OpenAPI

        :param entity_id: The entity_id of this EC2SecurityGroup.
        :param entity_type: The entity_type of this EC2SecurityGroup.
        :param name: The name of this EC2SecurityGroup.
        :param members: The members of this EC2SecurityGroup.
        :param direct_destination_rules: The direct_destination_rules of this EC2SecurityGroup.
        :param direct_members: The direct_members of this EC2SecurityGroup.
        :param direct_source_rules: The direct_source_rules of this EC2SecurityGroup.
        :param excluded_members: The excluded_members of this EC2SecurityGroup.
        :param indirect_destination_rules: The indirect_destination_rules of this EC2SecurityGroup.
        :param indirect_source_rules: The indirect_source_rules of this EC2SecurityGroup.
        :param parents: The parents of this EC2SecurityGroup.
        :param translated_vm_count: The translated_vm_count of this EC2SecurityGroup.
        :param vendor_id: The vendor_id of this EC2SecurityGroup.
        :param region: The region of this EC2SecurityGroup.
        :param vpc: The vpc of this EC2SecurityGroup.
        """
        self.openapi_types = {
            'entity_id': str,
            'entity_type': EntityType,
            'name': str,
            'members': List[Reference],
            'direct_destination_rules': List[RuleSet],
            'direct_members': List[Reference],
            'direct_source_rules': List[RuleSet],
            'excluded_members': List[Reference],
            'indirect_destination_rules': List[RuleSet],
            'indirect_source_rules': List[RuleSet],
            'parents': List[Reference],
            'translated_vm_count': int,
            'vendor_id': str,
            'region': str,
            'vpc': Reference
        }

        self.attribute_map = {
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'name': 'name',
            'members': 'members',
            'direct_destination_rules': 'direct_destination_rules',
            'direct_members': 'direct_members',
            'direct_source_rules': 'direct_source_rules',
            'excluded_members': 'excluded_members',
            'indirect_destination_rules': 'indirect_destination_rules',
            'indirect_source_rules': 'indirect_source_rules',
            'parents': 'parents',
            'translated_vm_count': 'translated_vm_count',
            'vendor_id': 'vendor_id',
            'region': 'region',
            'vpc': 'vpc'
        }

        self._entity_id = entity_id
        self._entity_type = entity_type
        self._name = name
        self._members = members
        self._direct_destination_rules = direct_destination_rules
        self._direct_members = direct_members
        self._direct_source_rules = direct_source_rules
        self._excluded_members = excluded_members
        self._indirect_destination_rules = indirect_destination_rules
        self._indirect_source_rules = indirect_source_rules
        self._parents = parents
        self._translated_vm_count = translated_vm_count
        self._vendor_id = vendor_id
        self._region = region
        self._vpc = vpc

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EC2SecurityGroup':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EC2SecurityGroup of this EC2SecurityGroup.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_id(self):
        """Gets the entity_id of this EC2SecurityGroup.


        :return: The entity_id of this EC2SecurityGroup.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EC2SecurityGroup.


        :param entity_id: The entity_id of this EC2SecurityGroup.
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this EC2SecurityGroup.


        :return: The entity_type of this EC2SecurityGroup.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EC2SecurityGroup.


        :param entity_type: The entity_type of this EC2SecurityGroup.
        :type entity_type: EntityType
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this EC2SecurityGroup.


        :return: The name of this EC2SecurityGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EC2SecurityGroup.


        :param name: The name of this EC2SecurityGroup.
        :type name: str
        """

        self._name = name

    @property
    def members(self):
        """Gets the members of this EC2SecurityGroup.


        :return: The members of this EC2SecurityGroup.
        :rtype: List[Reference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this EC2SecurityGroup.


        :param members: The members of this EC2SecurityGroup.
        :type members: List[Reference]
        """

        self._members = members

    @property
    def direct_destination_rules(self):
        """Gets the direct_destination_rules of this EC2SecurityGroup.


        :return: The direct_destination_rules of this EC2SecurityGroup.
        :rtype: List[RuleSet]
        """
        return self._direct_destination_rules

    @direct_destination_rules.setter
    def direct_destination_rules(self, direct_destination_rules):
        """Sets the direct_destination_rules of this EC2SecurityGroup.


        :param direct_destination_rules: The direct_destination_rules of this EC2SecurityGroup.
        :type direct_destination_rules: List[RuleSet]
        """

        self._direct_destination_rules = direct_destination_rules

    @property
    def direct_members(self):
        """Gets the direct_members of this EC2SecurityGroup.


        :return: The direct_members of this EC2SecurityGroup.
        :rtype: List[Reference]
        """
        return self._direct_members

    @direct_members.setter
    def direct_members(self, direct_members):
        """Sets the direct_members of this EC2SecurityGroup.


        :param direct_members: The direct_members of this EC2SecurityGroup.
        :type direct_members: List[Reference]
        """

        self._direct_members = direct_members

    @property
    def direct_source_rules(self):
        """Gets the direct_source_rules of this EC2SecurityGroup.


        :return: The direct_source_rules of this EC2SecurityGroup.
        :rtype: List[RuleSet]
        """
        return self._direct_source_rules

    @direct_source_rules.setter
    def direct_source_rules(self, direct_source_rules):
        """Sets the direct_source_rules of this EC2SecurityGroup.


        :param direct_source_rules: The direct_source_rules of this EC2SecurityGroup.
        :type direct_source_rules: List[RuleSet]
        """

        self._direct_source_rules = direct_source_rules

    @property
    def excluded_members(self):
        """Gets the excluded_members of this EC2SecurityGroup.


        :return: The excluded_members of this EC2SecurityGroup.
        :rtype: List[Reference]
        """
        return self._excluded_members

    @excluded_members.setter
    def excluded_members(self, excluded_members):
        """Sets the excluded_members of this EC2SecurityGroup.


        :param excluded_members: The excluded_members of this EC2SecurityGroup.
        :type excluded_members: List[Reference]
        """

        self._excluded_members = excluded_members

    @property
    def indirect_destination_rules(self):
        """Gets the indirect_destination_rules of this EC2SecurityGroup.


        :return: The indirect_destination_rules of this EC2SecurityGroup.
        :rtype: List[RuleSet]
        """
        return self._indirect_destination_rules

    @indirect_destination_rules.setter
    def indirect_destination_rules(self, indirect_destination_rules):
        """Sets the indirect_destination_rules of this EC2SecurityGroup.


        :param indirect_destination_rules: The indirect_destination_rules of this EC2SecurityGroup.
        :type indirect_destination_rules: List[RuleSet]
        """

        self._indirect_destination_rules = indirect_destination_rules

    @property
    def indirect_source_rules(self):
        """Gets the indirect_source_rules of this EC2SecurityGroup.


        :return: The indirect_source_rules of this EC2SecurityGroup.
        :rtype: List[RuleSet]
        """
        return self._indirect_source_rules

    @indirect_source_rules.setter
    def indirect_source_rules(self, indirect_source_rules):
        """Sets the indirect_source_rules of this EC2SecurityGroup.


        :param indirect_source_rules: The indirect_source_rules of this EC2SecurityGroup.
        :type indirect_source_rules: List[RuleSet]
        """

        self._indirect_source_rules = indirect_source_rules

    @property
    def parents(self):
        """Gets the parents of this EC2SecurityGroup.


        :return: The parents of this EC2SecurityGroup.
        :rtype: List[Reference]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this EC2SecurityGroup.


        :param parents: The parents of this EC2SecurityGroup.
        :type parents: List[Reference]
        """

        self._parents = parents

    @property
    def translated_vm_count(self):
        """Gets the translated_vm_count of this EC2SecurityGroup.


        :return: The translated_vm_count of this EC2SecurityGroup.
        :rtype: int
        """
        return self._translated_vm_count

    @translated_vm_count.setter
    def translated_vm_count(self, translated_vm_count):
        """Sets the translated_vm_count of this EC2SecurityGroup.


        :param translated_vm_count: The translated_vm_count of this EC2SecurityGroup.
        :type translated_vm_count: int
        """

        self._translated_vm_count = translated_vm_count

    @property
    def vendor_id(self):
        """Gets the vendor_id of this EC2SecurityGroup.


        :return: The vendor_id of this EC2SecurityGroup.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this EC2SecurityGroup.


        :param vendor_id: The vendor_id of this EC2SecurityGroup.
        :type vendor_id: str
        """

        self._vendor_id = vendor_id

    @property
    def region(self):
        """Gets the region of this EC2SecurityGroup.


        :return: The region of this EC2SecurityGroup.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this EC2SecurityGroup.


        :param region: The region of this EC2SecurityGroup.
        :type region: str
        """

        self._region = region

    @property
    def vpc(self):
        """Gets the vpc of this EC2SecurityGroup.


        :return: The vpc of this EC2SecurityGroup.
        :rtype: Reference
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this EC2SecurityGroup.


        :param vpc: The vpc of this EC2SecurityGroup.
        :type vpc: Reference
        """

        self._vpc = vpc
