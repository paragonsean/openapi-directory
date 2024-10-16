# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.load_balancer_ingress import LoadBalancerIngress
from openapi_server import util


class LoadBalancerStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ingress: List[LoadBalancerIngress]=None):
        """LoadBalancerStatus - a model defined in OpenAPI

        :param ingress: The ingress of this LoadBalancerStatus.
        """
        self.openapi_types = {
            'ingress': List[LoadBalancerIngress]
        }

        self.attribute_map = {
            'ingress': 'ingress'
        }

        self._ingress = ingress

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LoadBalancerStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LoadBalancerStatus of this LoadBalancerStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ingress(self):
        """Gets the ingress of this LoadBalancerStatus.

        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. +optional

        :return: The ingress of this LoadBalancerStatus.
        :rtype: List[LoadBalancerIngress]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """Sets the ingress of this LoadBalancerStatus.

        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. +optional

        :param ingress: The ingress of this LoadBalancerStatus.
        :type ingress: List[LoadBalancerIngress]
        """

        self._ingress = ingress
