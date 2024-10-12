from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts import Accounts
from openapi_server.models.ad_client import AdClient
from openapi_server.models.ad_clients import AdClients
from openapi_server.models.ad_code import AdCode
from openapi_server.models.ad_unit import AdUnit
from openapi_server.models.ad_units import AdUnits
from openapi_server.models.report import Report
from openapi_server import util


async def adsensehost_accounts_adclients_get(request: web.Request, account_id, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_accounts_adclients_get

    Get information about one of the ad clients in the specified publisher&#39;s AdSense account.

    :param account_id: Account which contains the ad client.
    :type account_id: str
    :param ad_client_id: Ad client to get.
    :type ad_client_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def adsensehost_accounts_adclients_list(request: web.Request, account_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None) -> web.Response:
    """adsensehost_accounts_adclients_list

    List all hosted ad clients in the specified hosted account.

    :param account_id: Account for which to list ad clients.
    :type account_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: The maximum number of ad clients to include in the response, used for paging.
    :type max_results: int
    :param page_token: A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response.
    :type page_token: str

    """
    return web.Response(status=200)


async def adsensehost_accounts_adunits_delete(request: web.Request, account_id, ad_client_id, ad_unit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_accounts_adunits_delete

    Delete the specified ad unit from the specified publisher AdSense account.

    :param account_id: Account which contains the ad unit.
    :type account_id: str
    :param ad_client_id: Ad client for which to get ad unit.
    :type ad_client_id: str
    :param ad_unit_id: Ad unit to delete.
    :type ad_unit_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def adsensehost_accounts_adunits_get(request: web.Request, account_id, ad_client_id, ad_unit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_accounts_adunits_get

    Get the specified host ad unit in this AdSense account.

    :param account_id: Account which contains the ad unit.
    :type account_id: str
    :param ad_client_id: Ad client for which to get ad unit.
    :type ad_client_id: str
    :param ad_unit_id: Ad unit to get.
    :type ad_unit_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def adsensehost_accounts_adunits_get_ad_code(request: web.Request, account_id, ad_client_id, ad_unit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, host_custom_channel_id=None) -> web.Response:
    """adsensehost_accounts_adunits_get_ad_code

    Get ad code for the specified ad unit, attaching the specified host custom channels.

    :param account_id: Account which contains the ad client.
    :type account_id: str
    :param ad_client_id: Ad client with contains the ad unit.
    :type ad_client_id: str
    :param ad_unit_id: Ad unit to get the code for.
    :type ad_unit_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param host_custom_channel_id: Host custom channel to attach to the ad code.
    :type host_custom_channel_id: List[str]

    """
    return web.Response(status=200)


async def adsensehost_accounts_adunits_insert(request: web.Request, account_id, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adsensehost_accounts_adunits_insert

    Insert the supplied ad unit into the specified publisher AdSense account.

    :param account_id: Account which will contain the ad unit.
    :type account_id: str
    :param ad_client_id: Ad client into which to insert the ad unit.
    :type ad_client_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = AdUnit.from_dict(body)
    return web.Response(status=200)


async def adsensehost_accounts_adunits_list(request: web.Request, account_id, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, include_inactive=None, max_results=None, page_token=None) -> web.Response:
    """adsensehost_accounts_adunits_list

    List all ad units in the specified publisher&#39;s AdSense account.

    :param account_id: Account which contains the ad client.
    :type account_id: str
    :param ad_client_id: Ad client for which to list ad units.
    :type ad_client_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param include_inactive: Whether to include inactive ad units. Default: true.
    :type include_inactive: bool
    :param max_results: The maximum number of ad units to include in the response, used for paging.
    :type max_results: int
    :param page_token: A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response.
    :type page_token: str

    """
    return web.Response(status=200)


async def adsensehost_accounts_adunits_patch(request: web.Request, account_id, ad_client_id, ad_unit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adsensehost_accounts_adunits_patch

    Update the supplied ad unit in the specified publisher AdSense account. This method supports patch semantics.

    :param account_id: Account which contains the ad client.
    :type account_id: str
    :param ad_client_id: Ad client which contains the ad unit.
    :type ad_client_id: str
    :param ad_unit_id: Ad unit to get.
    :type ad_unit_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = AdUnit.from_dict(body)
    return web.Response(status=200)


async def adsensehost_accounts_adunits_update(request: web.Request, account_id, ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """adsensehost_accounts_adunits_update

    Update the supplied ad unit in the specified publisher AdSense account.

    :param account_id: Account which contains the ad client.
    :type account_id: str
    :param ad_client_id: Ad client which contains the ad unit.
    :type ad_client_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = AdUnit.from_dict(body)
    return web.Response(status=200)


async def adsensehost_accounts_get(request: web.Request, account_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_accounts_get

    Get information about the selected associated AdSense account.

    :param account_id: Account to get information about.
    :type account_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def adsensehost_accounts_list(request: web.Request, filter_ad_client_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """adsensehost_accounts_list

    List hosted accounts associated with this AdSense account by ad client id.

    :param filter_ad_client_id: Ad clients to list accounts for.
    :type filter_ad_client_id: List[str]
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def adsensehost_accounts_reports_generate(request: web.Request, account_id, start_date, end_date, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, dimension=None, filter=None, locale=None, max_results=None, metric=None, sort=None, start_index=None) -> web.Response:
    """adsensehost_accounts_reports_generate

    Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify \&quot;alt&#x3D;csv\&quot; as a query parameter.

    :param account_id: Hosted account upon which to report.
    :type account_id: str
    :param start_date: Start of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive.
    :type start_date: str
    :param end_date: End of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive.
    :type end_date: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param dimension: Dimensions to base the report on.
    :type dimension: List[str]
    :param filter: Filters to be run on the report.
    :type filter: List[str]
    :param locale: Optional locale to use for translating report output to a local language. Defaults to \&quot;en_US\&quot; if not specified.
    :type locale: str
    :param max_results: The maximum number of rows of report data to return.
    :type max_results: int
    :param metric: Numeric columns to include in the report.
    :type metric: List[str]
    :param sort: The name of a dimension or metric to sort the resulting report on, optionally prefixed with \&quot;+\&quot; to sort ascending or \&quot;-\&quot; to sort descending. If no prefix is specified, the column is sorted ascending.
    :type sort: List[str]
    :param start_index: Index of the first row of report data to return.
    :type start_index: int

    """
    return web.Response(status=200)
