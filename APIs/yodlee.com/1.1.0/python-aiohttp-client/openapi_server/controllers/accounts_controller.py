from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_historical_balances_response import AccountHistoricalBalancesResponse
from openapi_server.models.account_response import AccountResponse
from openapi_server.models.create_account_request import CreateAccountRequest
from openapi_server.models.created_account_response import CreatedAccountResponse
from openapi_server.models.evaluate_address_request import EvaluateAddressRequest
from openapi_server.models.evaluate_address_response import EvaluateAddressResponse
from openapi_server.models.update_account_request import UpdateAccountRequest
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def create_manual_account(request: web.Request, body) -> web.Response:
    """Add Manual Account

    The add account service is used to add manual accounts.&lt;br&gt;The response of add account service includes the account name , account number and Yodlee generated account id.&lt;br&gt;All manual accounts added will be included as part of networth calculation by default.&lt;br&gt;Add manual account support is available for bank, card, investment, insurance and loan container only.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;A real estate account addition is only supported for SYSTEM and MANUAL valuation type.&lt;/li&gt;

    :param body: accountParam
    :type body: dict | bytes

    """
    body = CreateAccountRequest.from_dict(body)
    return web.Response(status=200)


async def delete_account(request: web.Request, account_id) -> web.Response:
    """Delete Account

    The delete account service allows an account to be deleted.&lt;br&gt;This service does not return a response. The HTTP response code is 204 (Success with no content).&lt;br&gt;

    :param account_id: accountId
    :type account_id: int

    """
    return web.Response(status=200)


async def evaluate_address(request: web.Request, body) -> web.Response:
    """Evaluate Address

    Use this service to validate the address before adding the real estate account.&lt;br&gt;If the address is valid, the service will return the complete address information.&lt;br&gt;The response will contain multiple addresses if the user-provided input matches with multiple entries in the vendor database.&lt;br&gt;In the case of multiple matches, the user can select the appropriate address from the list and then invoke the add account service with the complete address.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;Yodlee recommends to use this service before adding the real estate account to avoid failures.&lt;/li&gt;

    :param body: addressParam
    :type body: dict | bytes

    """
    body = EvaluateAddressRequest.from_dict(body)
    return web.Response(status=200)


async def get_account(request: web.Request, account_id, include=None) -> web.Response:
    """Get Account Details

    The get account details service provides detailed information of an account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.&lt;/li&gt;

    :param account_id: accountId
    :type account_id: int
    :param include: profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.
    :type include: str

    """
    return web.Response(status=200)


async def get_all_accounts(request: web.Request, account_id=None, container=None, include=None, provider_account_id=None, request_id=None, status=None) -> web.Response:
    """Get Accounts

    The get accounts service provides information about accounts added by the user.&lt;br&gt;By default, this service returns information for active and to be closed accounts.&lt;br&gt;If requestId is provided, the accounts that are updated in the context of the requestId will be provided in the response.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;&lt;li&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.&lt;/li&gt;&lt;li&gt;fullAccountNumberList, PII (Personal Identifiable Information) and holder details are not available by default, as it is a premium feature that needs security approval. This will not be available for testing in Sandbox environment.&lt;/li&gt;

    :param account_id: Comma separated accountIds.
    :type account_id: str
    :param container: bank/creditCard/investment/insurance/loan/reward/realEstate/otherAssets/otherLiabilities
    :type container: str
    :param include: profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.
    :type include: str
    :param provider_account_id: Comma separated providerAccountIds.
    :type provider_account_id: str
    :param request_id: The unique identifier that returns contextual data
    :type request_id: str
    :param status: ACTIVE,INACTIVE,TO_BE_CLOSED,CLOSED
    :type status: str

    """
    return web.Response(status=200)


async def get_historical_balances(request: web.Request, account_id=None, from_date=None, include_cf=None, interval=None, skip=None, to_date=None, top=None) -> web.Response:
    """Get Historical Balances

    The historical balances service is used to retrieve the historical balances for an account or a user.&lt;br&gt;Historical balances are daily (D), weekly (W), and monthly (M). &lt;br&gt;The interval input should be passed as D, W, and M to retrieve the desired historical balances. The default interval is daily (D). &lt;br&gt;When no account id is provided, historical balances of the accounts that are active, to be closed, and closed are provided in the response. &lt;br&gt;If the fromDate and toDate are not passed, the last 90 days of data will be provided. &lt;br&gt;The fromDate and toDate should be passed in the YYYY-MM-DD format. &lt;br&gt;The date field in the response denotes the date for which the balance is requested.&lt;br&gt;includeCF needs to be sent as true if the customer wants to return carried forward balances for a date when the data is not available. &lt;br&gt;asofDate field in the response denotes the date as of which the balance was updated for that account.&lt;br&gt;When there is no balance available for a requested date and if includeCF is sent as true, the previous date for which the balance is available is provided in the response. &lt;br&gt;When there is no previous balance available, no data will be sent.

    :param account_id: accountId
    :type account_id: str
    :param from_date: from date for balance retrieval (YYYY-MM-DD)
    :type from_date: str
    :param include_cf: Consider carry forward logic for missing balances
    :type include_cf: bool
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


async def update_account(request: web.Request, account_id, body) -> web.Response:
    """Update Account

    The update account service is used to update manual and aggregated accounts.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;Update manual account support is available for bank, card, investment, insurance, loan, otherAssets, otherLiabilities and realEstate containers only.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt; A real estate account update is only supported for SYSTEM and MANUAL valuation type.&lt;/li&gt;&lt;li&gt; Attribute &lt;b&gt;isEbillEnrolled&lt;/b&gt; is deprecated as it is applicable for bill accounts only.&lt;/li&gt;

    :param account_id: accountId
    :type account_id: int
    :param body: accountRequest
    :type body: dict | bytes

    """
    body = UpdateAccountRequest.from_dict(body)
    return web.Response(status=200)
