# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.resource_representation import ResourceRepresentation
from openapi_server.models.scope_representation import ScopeRepresentation
from openapi_server import util


class PolicyRepresentation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, config: Dict[str, object]=None, decision_strategy: str=None, description: str=None, id: str=None, logic: str=None, name: str=None, owner: str=None, policies: List[str]=None, resources: List[str]=None, resources_data: List[ResourceRepresentation]=None, scopes: List[str]=None, scopes_data: List[ScopeRepresentation]=None, type: str=None):
        """PolicyRepresentation - a model defined in OpenAPI

        :param config: The config of this PolicyRepresentation.
        :param decision_strategy: The decision_strategy of this PolicyRepresentation.
        :param description: The description of this PolicyRepresentation.
        :param id: The id of this PolicyRepresentation.
        :param logic: The logic of this PolicyRepresentation.
        :param name: The name of this PolicyRepresentation.
        :param owner: The owner of this PolicyRepresentation.
        :param policies: The policies of this PolicyRepresentation.
        :param resources: The resources of this PolicyRepresentation.
        :param resources_data: The resources_data of this PolicyRepresentation.
        :param scopes: The scopes of this PolicyRepresentation.
        :param scopes_data: The scopes_data of this PolicyRepresentation.
        :param type: The type of this PolicyRepresentation.
        """
        self.openapi_types = {
            'config': Dict[str, object],
            'decision_strategy': str,
            'description': str,
            'id': str,
            'logic': str,
            'name': str,
            'owner': str,
            'policies': List[str],
            'resources': List[str],
            'resources_data': List[ResourceRepresentation],
            'scopes': List[str],
            'scopes_data': List[ScopeRepresentation],
            'type': str
        }

        self.attribute_map = {
            'config': 'config',
            'decision_strategy': 'decisionStrategy',
            'description': 'description',
            'id': 'id',
            'logic': 'logic',
            'name': 'name',
            'owner': 'owner',
            'policies': 'policies',
            'resources': 'resources',
            'resources_data': 'resourcesData',
            'scopes': 'scopes',
            'scopes_data': 'scopesData',
            'type': 'type'
        }

        self._config = config
        self._decision_strategy = decision_strategy
        self._description = description
        self._id = id
        self._logic = logic
        self._name = name
        self._owner = owner
        self._policies = policies
        self._resources = resources
        self._resources_data = resources_data
        self._scopes = scopes
        self._scopes_data = scopes_data
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PolicyRepresentation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PolicyRepresentation of this PolicyRepresentation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config(self):
        """Gets the config of this PolicyRepresentation.


        :return: The config of this PolicyRepresentation.
        :rtype: Dict[str, object]
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this PolicyRepresentation.


        :param config: The config of this PolicyRepresentation.
        :type config: Dict[str, object]
        """

        self._config = config

    @property
    def decision_strategy(self):
        """Gets the decision_strategy of this PolicyRepresentation.


        :return: The decision_strategy of this PolicyRepresentation.
        :rtype: str
        """
        return self._decision_strategy

    @decision_strategy.setter
    def decision_strategy(self, decision_strategy):
        """Sets the decision_strategy of this PolicyRepresentation.


        :param decision_strategy: The decision_strategy of this PolicyRepresentation.
        :type decision_strategy: str
        """
        allowed_values = ["AFFIRMATIVE", "UNANIMOUS", "CONSENSUS"]  # noqa: E501
        if decision_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `decision_strategy` ({0}), must be one of {1}"
                .format(decision_strategy, allowed_values)
            )

        self._decision_strategy = decision_strategy

    @property
    def description(self):
        """Gets the description of this PolicyRepresentation.


        :return: The description of this PolicyRepresentation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyRepresentation.


        :param description: The description of this PolicyRepresentation.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this PolicyRepresentation.


        :return: The id of this PolicyRepresentation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyRepresentation.


        :param id: The id of this PolicyRepresentation.
        :type id: str
        """

        self._id = id

    @property
    def logic(self):
        """Gets the logic of this PolicyRepresentation.


        :return: The logic of this PolicyRepresentation.
        :rtype: str
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this PolicyRepresentation.


        :param logic: The logic of this PolicyRepresentation.
        :type logic: str
        """
        allowed_values = ["POSITIVE", "NEGATIVE"]  # noqa: E501
        if logic not in allowed_values:
            raise ValueError(
                "Invalid value for `logic` ({0}), must be one of {1}"
                .format(logic, allowed_values)
            )

        self._logic = logic

    @property
    def name(self):
        """Gets the name of this PolicyRepresentation.


        :return: The name of this PolicyRepresentation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyRepresentation.


        :param name: The name of this PolicyRepresentation.
        :type name: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this PolicyRepresentation.


        :return: The owner of this PolicyRepresentation.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PolicyRepresentation.


        :param owner: The owner of this PolicyRepresentation.
        :type owner: str
        """

        self._owner = owner

    @property
    def policies(self):
        """Gets the policies of this PolicyRepresentation.


        :return: The policies of this PolicyRepresentation.
        :rtype: List[str]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PolicyRepresentation.


        :param policies: The policies of this PolicyRepresentation.
        :type policies: List[str]
        """

        self._policies = policies

    @property
    def resources(self):
        """Gets the resources of this PolicyRepresentation.


        :return: The resources of this PolicyRepresentation.
        :rtype: List[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this PolicyRepresentation.


        :param resources: The resources of this PolicyRepresentation.
        :type resources: List[str]
        """

        self._resources = resources

    @property
    def resources_data(self):
        """Gets the resources_data of this PolicyRepresentation.


        :return: The resources_data of this PolicyRepresentation.
        :rtype: List[ResourceRepresentation]
        """
        return self._resources_data

    @resources_data.setter
    def resources_data(self, resources_data):
        """Sets the resources_data of this PolicyRepresentation.


        :param resources_data: The resources_data of this PolicyRepresentation.
        :type resources_data: List[ResourceRepresentation]
        """

        self._resources_data = resources_data

    @property
    def scopes(self):
        """Gets the scopes of this PolicyRepresentation.


        :return: The scopes of this PolicyRepresentation.
        :rtype: List[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this PolicyRepresentation.


        :param scopes: The scopes of this PolicyRepresentation.
        :type scopes: List[str]
        """

        self._scopes = scopes

    @property
    def scopes_data(self):
        """Gets the scopes_data of this PolicyRepresentation.


        :return: The scopes_data of this PolicyRepresentation.
        :rtype: List[ScopeRepresentation]
        """
        return self._scopes_data

    @scopes_data.setter
    def scopes_data(self, scopes_data):
        """Sets the scopes_data of this PolicyRepresentation.


        :param scopes_data: The scopes_data of this PolicyRepresentation.
        :type scopes_data: List[ScopeRepresentation]
        """

        self._scopes_data = scopes_data

    @property
    def type(self):
        """Gets the type of this PolicyRepresentation.


        :return: The type of this PolicyRepresentation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyRepresentation.


        :param type: The type of this PolicyRepresentation.
        :type type: str
        """

        self._type = type
