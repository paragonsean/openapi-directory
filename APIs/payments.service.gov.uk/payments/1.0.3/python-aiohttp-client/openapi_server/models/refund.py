# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.refund_links_for_search import RefundLinksForSearch
from openapi_server.models.refund_settlement_summary import RefundSettlementSummary
from openapi_server import util


class Refund(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: RefundLinksForSearch=None, amount: int=None, created_date: str=None, refund_id: str=None, settlement_summary: RefundSettlementSummary=None, status: str=None):
        """Refund - a model defined in OpenAPI

        :param links: The links of this Refund.
        :param amount: The amount of this Refund.
        :param created_date: The created_date of this Refund.
        :param refund_id: The refund_id of this Refund.
        :param settlement_summary: The settlement_summary of this Refund.
        :param status: The status of this Refund.
        """
        self.openapi_types = {
            'links': RefundLinksForSearch,
            'amount': int,
            'created_date': str,
            'refund_id': str,
            'settlement_summary': RefundSettlementSummary,
            'status': str
        }

        self.attribute_map = {
            'links': '_links',
            'amount': 'amount',
            'created_date': 'created_date',
            'refund_id': 'refund_id',
            'settlement_summary': 'settlement_summary',
            'status': 'status'
        }

        self._links = links
        self._amount = amount
        self._created_date = created_date
        self._refund_id = refund_id
        self._settlement_summary = settlement_summary
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Refund':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Refund of this Refund.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this Refund.


        :return: The links of this Refund.
        :rtype: RefundLinksForSearch
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Refund.


        :param links: The links of this Refund.
        :type links: RefundLinksForSearch
        """

        self._links = links

    @property
    def amount(self):
        """Gets the amount of this Refund.


        :return: The amount of this Refund.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Refund.


        :param amount: The amount of this Refund.
        :type amount: int
        """

        self._amount = amount

    @property
    def created_date(self):
        """Gets the created_date of this Refund.


        :return: The created_date of this Refund.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Refund.


        :param created_date: The created_date of this Refund.
        :type created_date: str
        """

        self._created_date = created_date

    @property
    def refund_id(self):
        """Gets the refund_id of this Refund.


        :return: The refund_id of this Refund.
        :rtype: str
        """
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        """Sets the refund_id of this Refund.


        :param refund_id: The refund_id of this Refund.
        :type refund_id: str
        """

        self._refund_id = refund_id

    @property
    def settlement_summary(self):
        """Gets the settlement_summary of this Refund.


        :return: The settlement_summary of this Refund.
        :rtype: RefundSettlementSummary
        """
        return self._settlement_summary

    @settlement_summary.setter
    def settlement_summary(self, settlement_summary):
        """Sets the settlement_summary of this Refund.


        :param settlement_summary: The settlement_summary of this Refund.
        :type settlement_summary: RefundSettlementSummary
        """

        self._settlement_summary = settlement_summary

    @property
    def status(self):
        """Gets the status of this Refund.


        :return: The status of this Refund.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Refund.


        :param status: The status of this Refund.
        :type status: str
        """
        allowed_values = ["submitted", "success", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
