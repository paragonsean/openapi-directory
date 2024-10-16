# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.critical_illness_insurance_policy_type_model import CriticalIllnessInsurancePolicyTypeModel
from openapi_server import util


class CriticalIllnessInsurancePolicyTypesModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, insurance_policy_types: List[CriticalIllnessInsurancePolicyTypeModel]=None):
        """CriticalIllnessInsurancePolicyTypesModel - a model defined in OpenAPI

        :param insurance_policy_types: The insurance_policy_types of this CriticalIllnessInsurancePolicyTypesModel.
        """
        self.openapi_types = {
            'insurance_policy_types': List[CriticalIllnessInsurancePolicyTypeModel]
        }

        self.attribute_map = {
            'insurance_policy_types': 'insurancePolicyTypes'
        }

        self._insurance_policy_types = insurance_policy_types

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CriticalIllnessInsurancePolicyTypesModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CriticalIllnessInsurancePolicyTypesModel of this CriticalIllnessInsurancePolicyTypesModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def insurance_policy_types(self):
        """Gets the insurance_policy_types of this CriticalIllnessInsurancePolicyTypesModel.


        :return: The insurance_policy_types of this CriticalIllnessInsurancePolicyTypesModel.
        :rtype: List[CriticalIllnessInsurancePolicyTypeModel]
        """
        return self._insurance_policy_types

    @insurance_policy_types.setter
    def insurance_policy_types(self, insurance_policy_types):
        """Sets the insurance_policy_types of this CriticalIllnessInsurancePolicyTypesModel.


        :param insurance_policy_types: The insurance_policy_types of this CriticalIllnessInsurancePolicyTypesModel.
        :type insurance_policy_types: List[CriticalIllnessInsurancePolicyTypeModel]
        """

        self._insurance_policy_types = insurance_policy_types
