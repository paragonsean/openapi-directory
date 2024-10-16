# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, downstream: float=None, percentage: float=None, total: float=None, upstream: float=None):
        """GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage - a model defined in OpenAPI

        :param downstream: The downstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :param percentage: The percentage of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :param total: The total of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :param upstream: The upstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        """
        self.openapi_types = {
            'downstream': float,
            'percentage': float,
            'total': float,
            'upstream': float
        }

        self.attribute_map = {
            'downstream': 'downstream',
            'percentage': 'percentage',
            'total': 'total',
            'upstream': 'upstream'
        }

        self._downstream = downstream
        self._percentage = percentage
        self._total = total
        self._upstream = upstream

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationSummaryTopClientsByUsage_200_response_inner_usage of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def downstream(self):
        """Gets the downstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Downstream data usage by client

        :return: The downstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :rtype: float
        """
        return self._downstream

    @downstream.setter
    def downstream(self, downstream):
        """Sets the downstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Downstream data usage by client

        :param downstream: The downstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :type downstream: float
        """

        self._downstream = downstream

    @property
    def percentage(self):
        """Gets the percentage of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Percentage of total data usage by client

        :return: The percentage of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Percentage of total data usage by client

        :param percentage: The percentage of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :type percentage: float
        """

        self._percentage = percentage

    @property
    def total(self):
        """Gets the total of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Total data usage by client

        :return: The total of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Total data usage by client

        :param total: The total of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :type total: float
        """

        self._total = total

    @property
    def upstream(self):
        """Gets the upstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Upstream data usage by client

        :return: The upstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :rtype: float
        """
        return self._upstream

    @upstream.setter
    def upstream(self, upstream):
        """Sets the upstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.

        Upstream data usage by client

        :param upstream: The upstream of this GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.
        :type upstream: float
        """

        self._upstream = upstream
