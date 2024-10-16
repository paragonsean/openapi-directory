# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.life_insurance_policy_with_sub_entities_model import LifeInsurancePolicyWithSubEntitiesModel
from openapi_server import util


class LifeInsurancePoliciesWithSubEntitiesModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, life_insurance_policies: List[LifeInsurancePolicyWithSubEntitiesModel]=None):
        """LifeInsurancePoliciesWithSubEntitiesModel - a model defined in OpenAPI

        :param life_insurance_policies: The life_insurance_policies of this LifeInsurancePoliciesWithSubEntitiesModel.
        """
        self.openapi_types = {
            'life_insurance_policies': List[LifeInsurancePolicyWithSubEntitiesModel]
        }

        self.attribute_map = {
            'life_insurance_policies': 'lifeInsurancePolicies'
        }

        self._life_insurance_policies = life_insurance_policies

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LifeInsurancePoliciesWithSubEntitiesModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LifeInsurancePoliciesWithSubEntitiesModel of this LifeInsurancePoliciesWithSubEntitiesModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def life_insurance_policies(self):
        """Gets the life_insurance_policies of this LifeInsurancePoliciesWithSubEntitiesModel.


        :return: The life_insurance_policies of this LifeInsurancePoliciesWithSubEntitiesModel.
        :rtype: List[LifeInsurancePolicyWithSubEntitiesModel]
        """
        return self._life_insurance_policies

    @life_insurance_policies.setter
    def life_insurance_policies(self, life_insurance_policies):
        """Sets the life_insurance_policies of this LifeInsurancePoliciesWithSubEntitiesModel.


        :param life_insurance_policies: The life_insurance_policies of this LifeInsurancePoliciesWithSubEntitiesModel.
        :type life_insurance_policies: List[LifeInsurancePolicyWithSubEntitiesModel]
        """

        self._life_insurance_policies = life_insurance_policies
