from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_analytics_admin_v1alpha_list_accounts_response import GoogleAnalyticsAdminV1alphaListAccountsResponse
from openapi_server.models.google_analytics_admin_v1alpha_provision_account_ticket_request import GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest
from openapi_server.models.google_analytics_admin_v1alpha_provision_account_ticket_response import GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse
from openapi_server.models.google_analytics_admin_v1alpha_search_change_history_events_request import GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest
from openapi_server.models.google_analytics_admin_v1alpha_search_change_history_events_response import GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse
from openapi_server import util


async def analyticsadmin_accounts_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """analyticsadmin_accounts_list

    Returns all accounts accessible by the caller. Note that these accounts might not currently have GA4 properties. Soft-deleted (ie: \&quot;trashed\&quot;) accounts are excluded by default. Returns an empty list if no relevant accounts are found.

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
    :param page_size: The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListAccounts&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListAccounts&#x60; must match the call that provided the page token.
    :type page_token: str
    :param show_deleted: Whether to include soft-deleted (ie: \&quot;trashed\&quot;) Accounts in the results. Accounts can be inspected to determine whether they are deleted or not.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def analyticsadmin_accounts_provision_account_ticket(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """analyticsadmin_accounts_provision_account_ticket

    Requests a ticket for creating an account.

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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest.from_dict(body)
    return web.Response(status=200)


async def analyticsadmin_accounts_search_change_history_events(request: web.Request, account, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """analyticsadmin_accounts_search_change_history_events

    Searches through all changes to an account or its children given the specified set of filters.

    :param account: Required. The account resource for which to return change history resources. Format: accounts/{account} Example: \&quot;accounts/100\&quot;
    :type account: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest.from_dict(body)
    return web.Response(status=200)
