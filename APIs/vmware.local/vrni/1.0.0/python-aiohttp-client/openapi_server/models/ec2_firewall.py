# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.base_firewall import BaseFirewall
from openapi_server.models.entity_type import EntityType
from openapi_server.models.reference import Reference
from openapi_server.models.rule_set import RuleSet
from openapi_server import util


class EC2Firewall(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_id: str=None, entity_type: EntityType=None, name: str=None, exclusions: List[Reference]=None, firewall_rules: List[RuleSet]=None):
        """EC2Firewall - a model defined in OpenAPI

        :param entity_id: The entity_id of this EC2Firewall.
        :param entity_type: The entity_type of this EC2Firewall.
        :param name: The name of this EC2Firewall.
        :param exclusions: The exclusions of this EC2Firewall.
        :param firewall_rules: The firewall_rules of this EC2Firewall.
        """
        self.openapi_types = {
            'entity_id': str,
            'entity_type': EntityType,
            'name': str,
            'exclusions': List[Reference],
            'firewall_rules': List[RuleSet]
        }

        self.attribute_map = {
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'name': 'name',
            'exclusions': 'exclusions',
            'firewall_rules': 'firewall_rules'
        }

        self._entity_id = entity_id
        self._entity_type = entity_type
        self._name = name
        self._exclusions = exclusions
        self._firewall_rules = firewall_rules

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EC2Firewall':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EC2Firewall of this EC2Firewall.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_id(self):
        """Gets the entity_id of this EC2Firewall.


        :return: The entity_id of this EC2Firewall.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EC2Firewall.


        :param entity_id: The entity_id of this EC2Firewall.
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this EC2Firewall.


        :return: The entity_type of this EC2Firewall.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EC2Firewall.


        :param entity_type: The entity_type of this EC2Firewall.
        :type entity_type: EntityType
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this EC2Firewall.


        :return: The name of this EC2Firewall.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EC2Firewall.


        :param name: The name of this EC2Firewall.
        :type name: str
        """

        self._name = name

    @property
    def exclusions(self):
        """Gets the exclusions of this EC2Firewall.


        :return: The exclusions of this EC2Firewall.
        :rtype: List[Reference]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """Sets the exclusions of this EC2Firewall.


        :param exclusions: The exclusions of this EC2Firewall.
        :type exclusions: List[Reference]
        """

        self._exclusions = exclusions

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this EC2Firewall.


        :return: The firewall_rules of this EC2Firewall.
        :rtype: List[RuleSet]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this EC2Firewall.


        :param firewall_rules: The firewall_rules of this EC2Firewall.
        :type firewall_rules: List[RuleSet]
        """

        self._firewall_rules = firewall_rules
