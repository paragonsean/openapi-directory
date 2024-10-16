# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Totals(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, total_clicks: str=None, total_cpc: str=None, total_ctr: str=None, total_earnings: str=None, total_impressions: str=None, total_net_ecpm: str=None, total_rpm: str=None):
        """Totals - a model defined in OpenAPI

        :param total_clicks: The total_clicks of this Totals.
        :param total_cpc: The total_cpc of this Totals.
        :param total_ctr: The total_ctr of this Totals.
        :param total_earnings: The total_earnings of this Totals.
        :param total_impressions: The total_impressions of this Totals.
        :param total_net_ecpm: The total_net_ecpm of this Totals.
        :param total_rpm: The total_rpm of this Totals.
        """
        self.openapi_types = {
            'total_clicks': str,
            'total_cpc': str,
            'total_ctr': str,
            'total_earnings': str,
            'total_impressions': str,
            'total_net_ecpm': str,
            'total_rpm': str
        }

        self.attribute_map = {
            'total_clicks': 'total_clicks',
            'total_cpc': 'total_cpc',
            'total_ctr': 'total_ctr',
            'total_earnings': 'total_earnings',
            'total_impressions': 'total_impressions',
            'total_net_ecpm': 'total_net_ecpm',
            'total_rpm': 'total_rpm'
        }

        self._total_clicks = total_clicks
        self._total_cpc = total_cpc
        self._total_ctr = total_ctr
        self._total_earnings = total_earnings
        self._total_impressions = total_impressions
        self._total_net_ecpm = total_net_ecpm
        self._total_rpm = total_rpm

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Totals':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The totals of this Totals.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total_clicks(self):
        """Gets the total_clicks of this Totals.


        :return: The total_clicks of this Totals.
        :rtype: str
        """
        return self._total_clicks

    @total_clicks.setter
    def total_clicks(self, total_clicks):
        """Sets the total_clicks of this Totals.


        :param total_clicks: The total_clicks of this Totals.
        :type total_clicks: str
        """

        self._total_clicks = total_clicks

    @property
    def total_cpc(self):
        """Gets the total_cpc of this Totals.


        :return: The total_cpc of this Totals.
        :rtype: str
        """
        return self._total_cpc

    @total_cpc.setter
    def total_cpc(self, total_cpc):
        """Sets the total_cpc of this Totals.


        :param total_cpc: The total_cpc of this Totals.
        :type total_cpc: str
        """

        self._total_cpc = total_cpc

    @property
    def total_ctr(self):
        """Gets the total_ctr of this Totals.


        :return: The total_ctr of this Totals.
        :rtype: str
        """
        return self._total_ctr

    @total_ctr.setter
    def total_ctr(self, total_ctr):
        """Sets the total_ctr of this Totals.


        :param total_ctr: The total_ctr of this Totals.
        :type total_ctr: str
        """

        self._total_ctr = total_ctr

    @property
    def total_earnings(self):
        """Gets the total_earnings of this Totals.


        :return: The total_earnings of this Totals.
        :rtype: str
        """
        return self._total_earnings

    @total_earnings.setter
    def total_earnings(self, total_earnings):
        """Sets the total_earnings of this Totals.


        :param total_earnings: The total_earnings of this Totals.
        :type total_earnings: str
        """

        self._total_earnings = total_earnings

    @property
    def total_impressions(self):
        """Gets the total_impressions of this Totals.


        :return: The total_impressions of this Totals.
        :rtype: str
        """
        return self._total_impressions

    @total_impressions.setter
    def total_impressions(self, total_impressions):
        """Sets the total_impressions of this Totals.


        :param total_impressions: The total_impressions of this Totals.
        :type total_impressions: str
        """

        self._total_impressions = total_impressions

    @property
    def total_net_ecpm(self):
        """Gets the total_net_ecpm of this Totals.


        :return: The total_net_ecpm of this Totals.
        :rtype: str
        """
        return self._total_net_ecpm

    @total_net_ecpm.setter
    def total_net_ecpm(self, total_net_ecpm):
        """Sets the total_net_ecpm of this Totals.


        :param total_net_ecpm: The total_net_ecpm of this Totals.
        :type total_net_ecpm: str
        """

        self._total_net_ecpm = total_net_ecpm

    @property
    def total_rpm(self):
        """Gets the total_rpm of this Totals.


        :return: The total_rpm of this Totals.
        :rtype: str
        """
        return self._total_rpm

    @total_rpm.setter
    def total_rpm(self, total_rpm):
        """Sets the total_rpm of this Totals.


        :param total_rpm: The total_rpm of this Totals.
        :type total_rpm: str
        """

        self._total_rpm = total_rpm
