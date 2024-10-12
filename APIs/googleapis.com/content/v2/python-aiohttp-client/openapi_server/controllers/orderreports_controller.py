from typing import List, Dict
from aiohttp import web

from openapi_server.models.orderreports_list_disbursements_response import OrderreportsListDisbursementsResponse
from openapi_server.models.orderreports_list_transactions_response import OrderreportsListTransactionsResponse
from openapi_server import util


async def content_orderreports_listdisbursements(request: web.Request, merchant_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, disbursement_end_date=None, disbursement_start_date=None, max_results=None, page_token=None) -> web.Response:
    """content_orderreports_listdisbursements

    Retrieves a report for disbursements from your Merchant Center account.

    :param merchant_id: The ID of the account that manages the order. This cannot be a multi-client account.
    :type merchant_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param disbursement_end_date: The last date which disbursements occurred. In ISO 8601 format. Default: current date.
    :type disbursement_end_date: str
    :param disbursement_start_date: The first date which disbursements occurred. In ISO 8601 format.
    :type disbursement_start_date: str
    :param max_results: The maximum number of disbursements to return in the response, used for paging.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str

    """
    return web.Response(status=200)


async def content_orderreports_listtransactions(request: web.Request, merchant_id, disbursement_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, page_token=None, transaction_end_date=None, transaction_start_date=None) -> web.Response:
    """content_orderreports_listtransactions

    Retrieves a list of transactions for a disbursement from your Merchant Center account.

    :param merchant_id: The ID of the account that manages the order. This cannot be a multi-client account.
    :type merchant_id: str
    :param disbursement_id: The Google-provided ID of the disbursement (found in Wallet).
    :type disbursement_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param max_results: The maximum number of disbursements to return in the response, used for paging.
    :type max_results: int
    :param page_token: The token returned by the previous request.
    :type page_token: str
    :param transaction_end_date: The last date in which transaction occurred. In ISO 8601 format. Default: current date.
    :type transaction_end_date: str
    :param transaction_start_date: The first date in which transaction occurred. In ISO 8601 format.
    :type transaction_start_date: str

    """
    return web.Response(status=200)
