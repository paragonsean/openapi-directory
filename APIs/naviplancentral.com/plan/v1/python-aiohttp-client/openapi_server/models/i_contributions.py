# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_inter_company_dividend_received import IInterCompanyDividendReceived
from openapi_server.models.i_share_purchase import ISharePurchase
from openapi_server.models.i_shareholder_loan import IShareholderLoan
from openapi_server import util


class IContributions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, inter_company_dividends_received: List[IInterCompanyDividendReceived]=None, share_purchases: List[ISharePurchase]=None, shareholder_loans: List[IShareholderLoan]=None):
        """IContributions - a model defined in OpenAPI

        :param inter_company_dividends_received: The inter_company_dividends_received of this IContributions.
        :param share_purchases: The share_purchases of this IContributions.
        :param shareholder_loans: The shareholder_loans of this IContributions.
        """
        self.openapi_types = {
            'inter_company_dividends_received': List[IInterCompanyDividendReceived],
            'share_purchases': List[ISharePurchase],
            'shareholder_loans': List[IShareholderLoan]
        }

        self.attribute_map = {
            'inter_company_dividends_received': 'interCompanyDividendsReceived',
            'share_purchases': 'sharePurchases',
            'shareholder_loans': 'shareholderLoans'
        }

        self._inter_company_dividends_received = inter_company_dividends_received
        self._share_purchases = share_purchases
        self._shareholder_loans = shareholder_loans

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IContributions':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IContributions of this IContributions.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def inter_company_dividends_received(self):
        """Gets the inter_company_dividends_received of this IContributions.


        :return: The inter_company_dividends_received of this IContributions.
        :rtype: List[IInterCompanyDividendReceived]
        """
        return self._inter_company_dividends_received

    @inter_company_dividends_received.setter
    def inter_company_dividends_received(self, inter_company_dividends_received):
        """Sets the inter_company_dividends_received of this IContributions.


        :param inter_company_dividends_received: The inter_company_dividends_received of this IContributions.
        :type inter_company_dividends_received: List[IInterCompanyDividendReceived]
        """

        self._inter_company_dividends_received = inter_company_dividends_received

    @property
    def share_purchases(self):
        """Gets the share_purchases of this IContributions.


        :return: The share_purchases of this IContributions.
        :rtype: List[ISharePurchase]
        """
        return self._share_purchases

    @share_purchases.setter
    def share_purchases(self, share_purchases):
        """Sets the share_purchases of this IContributions.


        :param share_purchases: The share_purchases of this IContributions.
        :type share_purchases: List[ISharePurchase]
        """

        self._share_purchases = share_purchases

    @property
    def shareholder_loans(self):
        """Gets the shareholder_loans of this IContributions.


        :return: The shareholder_loans of this IContributions.
        :rtype: List[IShareholderLoan]
        """
        return self._shareholder_loans

    @shareholder_loans.setter
    def shareholder_loans(self, shareholder_loans):
        """Sets the shareholder_loans of this IContributions.


        :param shareholder_loans: The shareholder_loans of this IContributions.
        :type shareholder_loans: List[IShareholderLoan]
        """

        self._shareholder_loans = shareholder_loans
