from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_org_data_exchanges_response import ListOrgDataExchangesResponse
from openapi_server import util


async def analyticshub_organizations_locations_data_exchanges_list(request: web.Request, organization, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """analyticshub_organizations_locations_data_exchanges_list

    Lists all data exchanges from projects in a given organization and location.

    :param organization: Required. The organization resource path of the projects containing DataExchanges. e.g. &#x60;organizations/myorg/locations/US&#x60;.
    :type organization: str
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
    :param page_size: The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection.
    :type page_size: int
    :param page_token: Page token, returned by a previous call, to request the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)
