# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IncludedResourcesMap(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bags: object=None, credit_card_fees: object=None, detailed_fare_rules: object=None, other_services: object=None):
        """IncludedResourcesMap - a model defined in OpenAPI

        :param bags: The bags of this IncludedResourcesMap.
        :param credit_card_fees: The credit_card_fees of this IncludedResourcesMap.
        :param detailed_fare_rules: The detailed_fare_rules of this IncludedResourcesMap.
        :param other_services: The other_services of this IncludedResourcesMap.
        """
        self.openapi_types = {
            'bags': object,
            'credit_card_fees': object,
            'detailed_fare_rules': object,
            'other_services': object
        }

        self.attribute_map = {
            'bags': 'bags',
            'credit_card_fees': 'credit-card-fees',
            'detailed_fare_rules': 'detailed-fare-rules',
            'other_services': 'other-services'
        }

        self._bags = bags
        self._credit_card_fees = credit_card_fees
        self._detailed_fare_rules = detailed_fare_rules
        self._other_services = other_services

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IncludedResourcesMap':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The included_resources_map of this IncludedResourcesMap.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bags(self):
        """Gets the bags of this IncludedResourcesMap.

        Map of fee applied by bag option

        :return: The bags of this IncludedResourcesMap.
        :rtype: object
        """
        return self._bags

    @bags.setter
    def bags(self, bags):
        """Sets the bags of this IncludedResourcesMap.

        Map of fee applied by bag option

        :param bags: The bags of this IncludedResourcesMap.
        :type bags: object
        """

        self._bags = bags

    @property
    def credit_card_fees(self):
        """Gets the credit_card_fees of this IncludedResourcesMap.

        Map of fee applied by credit card brand

        :return: The credit_card_fees of this IncludedResourcesMap.
        :rtype: object
        """
        return self._credit_card_fees

    @credit_card_fees.setter
    def credit_card_fees(self, credit_card_fees):
        """Sets the credit_card_fees of this IncludedResourcesMap.

        Map of fee applied by credit card brand

        :param credit_card_fees: The credit_card_fees of this IncludedResourcesMap.
        :type credit_card_fees: object
        """

        self._credit_card_fees = credit_card_fees

    @property
    def detailed_fare_rules(self):
        """Gets the detailed_fare_rules of this IncludedResourcesMap.

        Map of fare rules applied by farebasis

        :return: The detailed_fare_rules of this IncludedResourcesMap.
        :rtype: object
        """
        return self._detailed_fare_rules

    @detailed_fare_rules.setter
    def detailed_fare_rules(self, detailed_fare_rules):
        """Sets the detailed_fare_rules of this IncludedResourcesMap.

        Map of fare rules applied by farebasis

        :param detailed_fare_rules: The detailed_fare_rules of this IncludedResourcesMap.
        :type detailed_fare_rules: object
        """

        self._detailed_fare_rules = detailed_fare_rules

    @property
    def other_services(self):
        """Gets the other_services of this IncludedResourcesMap.

        Map of fee applied by service

        :return: The other_services of this IncludedResourcesMap.
        :rtype: object
        """
        return self._other_services

    @other_services.setter
    def other_services(self, other_services):
        """Sets the other_services of this IncludedResourcesMap.

        Map of fee applied by service

        :param other_services: The other_services of this IncludedResourcesMap.
        :type other_services: object
        """

        self._other_services = other_services
