# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.object_link import ObjectLink
from openapi_server import util


class CriticalIllnessInsurancePolicyTypeModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, links: List[ObjectLink]=None, name: str=None):
        """CriticalIllnessInsurancePolicyTypeModel - a model defined in OpenAPI

        :param id: The id of this CriticalIllnessInsurancePolicyTypeModel.
        :param links: The links of this CriticalIllnessInsurancePolicyTypeModel.
        :param name: The name of this CriticalIllnessInsurancePolicyTypeModel.
        """
        self.openapi_types = {
            'id': int,
            'links': List[ObjectLink],
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'links': 'links',
            'name': 'name'
        }

        self._id = id
        self._links = links
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CriticalIllnessInsurancePolicyTypeModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CriticalIllnessInsurancePolicyTypeModel of this CriticalIllnessInsurancePolicyTypeModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CriticalIllnessInsurancePolicyTypeModel.


        :return: The id of this CriticalIllnessInsurancePolicyTypeModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CriticalIllnessInsurancePolicyTypeModel.


        :param id: The id of this CriticalIllnessInsurancePolicyTypeModel.
        :type id: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this CriticalIllnessInsurancePolicyTypeModel.


        :return: The links of this CriticalIllnessInsurancePolicyTypeModel.
        :rtype: List[ObjectLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CriticalIllnessInsurancePolicyTypeModel.


        :param links: The links of this CriticalIllnessInsurancePolicyTypeModel.
        :type links: List[ObjectLink]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this CriticalIllnessInsurancePolicyTypeModel.


        :return: The name of this CriticalIllnessInsurancePolicyTypeModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CriticalIllnessInsurancePolicyTypeModel.


        :param name: The name of this CriticalIllnessInsurancePolicyTypeModel.
        :type name: str
        """

        self._name = name
