from typing import List, Dict
from aiohttp import web

from openapi_server.models.derived_holding_summary_response import DerivedHoldingSummaryResponse
from openapi_server.models.derived_networth_response import DerivedNetworthResponse
from openapi_server.models.derived_transaction_summary_response import DerivedTransactionSummaryResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def get_holding_summary(request: web.Request, account_ids=None, classification_type=None, include=None) -> web.Response:
    """Get Holding Summary

    The get holding summary service is used to get the summary of asset classifications for the user.&lt;br&gt;By default, accounts with status as ACTIVE and TO BE CLOSED will be considered.&lt;br&gt;If the include parameter value is passed as details then a summary with holdings and account information is returned.&lt;br&gt;

    :param account_ids: Comma separated accountIds
    :type account_ids: str
    :param classification_type: e.g. Country, Sector, etc.
    :type classification_type: str
    :param include: details
    :type include: str

    """
    return web.Response(status=200)


async def get_networth(request: web.Request, account_ids=None, container=None, from_date=None, include=None, interval=None, skip=None, to_date=None, top=None) -> web.Response:
    """Get Networth Summary

    The get networth service is used to get the networth for the user.&lt;br&gt;If the include parameter value is passed as details then networth with historical balances is returned. &lt;br&gt;

    :param account_ids: comma separated accountIds
    :type account_ids: str
    :param container: bank/creditCard/investment/insurance/loan/realEstate/otherAssets/otherLiabilities
    :type container: str
    :param from_date: from date for balance retrieval (YYYY-MM-DD)
    :type from_date: str
    :param include: details
    :type include: str
    :param interval: D-daily, W-weekly or M-monthly
    :type interval: str
    :param skip: skip (Min 0)
    :type skip: int
    :param to_date: toDate for balance retrieval (YYYY-MM-DD)
    :type to_date: str
    :param top: top (Max 500)
    :type top: int

    """
    return web.Response(status=200)


async def get_transaction_summary(request: web.Request, group_by, account_id=None, category_id=None, category_type=None, from_date=None, include=None, include_user_category=None, interval=None, to_date=None) -> web.Response:
    """Get Transaction Summary

    The transaction summary service provides the summary values of transactions for the given date range by category type, high-level categories, or system-defined categories.&lt;br&gt;&lt;br&gt;Yodlee has the transaction data stored for a day, month, year and week per category as per the availability of user&#39;s data. If the include parameter value is passed as details, then summary details will be returned depending on the interval passed-monthly is the default.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;ol&gt; &lt;li&gt; Details can be requested for only one system-defined category&lt;li&gt;Passing categoryType is mandatory except when the groupBy value is CATEGORY_TYPE&lt;li&gt;Dates will not be respected for monthly, yearly, and weekly details&lt;li&gt;When monthly details are requested, only the fromDate and toDate month will be respected&lt;li&gt;When yearly details are requested, only the fromDate and toDate year will be respected&lt;li&gt;For weekly data points, details will be provided for every Sunday date available within the fromDate and toDate&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter&lt;/li&gt;&lt;/ol&gt;

    :param group_by: CATEGORY_TYPE, HIGH_LEVEL_CATEGORY or CATEGORY
    :type group_by: str
    :param account_id: comma separated account Ids
    :type account_id: str
    :param category_id: comma separated categoryIds
    :type category_id: str
    :param category_type: INCOME, EXPENSE, TRANSFER, UNCATEGORIZE or DEFERRED_COMPENSATION
    :type category_type: str
    :param from_date: YYYY-MM-DD format
    :type from_date: str
    :param include: details
    :type include: str
    :param include_user_category: TRUE/FALSE
    :type include_user_category: bool
    :param interval: D-daily, W-weekly, M-mothly or Y-yearly
    :type interval: str
    :param to_date: YYYY-MM-DD format
    :type to_date: str

    """
    return web.Response(status=200)
