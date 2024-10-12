from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.location import Location
from openapi_server import util


async def mybusinessbusinessinformation_accounts_locations_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """mybusinessbusinessinformation_accounts_locations_create

    Creates a new Location that will be owned by the logged in user.

    :param parent: Required. The name of the account in which to create this location.
    :type parent: str
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
    :param request_id: Optional. A unique request ID for the server to detect duplicated requests. We recommend using UUIDs. Max length is 50 characters.
    :type request_id: str
    :param validate_only: Optional. If true, the request is validated without actually creating the location.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Location.from_dict(body)
    return web.Response(status=200)


async def mybusinessbusinessinformation_accounts_locations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, read_mask=None) -> web.Response:
    """mybusinessbusinessinformation_accounts_locations_list

    Lists the locations for the specified account.

    :param parent: Required. The name of the account to fetch locations from. If the parent Account is of AccountType PERSONAL, only Locations that are directly owned by the Account are returned, otherwise it will return all accessible locations from the Account, either directly or indirectly.
    :type parent: str
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
    :param filter: Optional. A filter constraining the locations to return. The response includes only entries that match the filter. If &#x60;filter&#x60; is empty, then constraints are applied and all locations (paginated) are retrieved for the requested account. For more information about valid fields and example usage, see [Work with Location Data Guide](https://developers.google.com/my-business/content/location-data#filter_results_when_you_list_locations).
    :type filter: str
    :param order_by: Optional. Sorting order for the request. Multiple fields should be comma-separated, following SQL syntax. The default sorting order is ascending. To specify descending order, a suffix \&quot; desc\&quot; should be added. Valid fields to order_by are title and store_code. For example: \&quot;title, store_code desc\&quot; or \&quot;title\&quot; or \&quot;store_code desc\&quot;
    :type order_by: str
    :param page_size: Optional. How many locations to fetch per page. Default value is 10 if not set. Minimum is 1, and maximum page size is 100.
    :type page_size: int
    :param page_token: Optional. If specified, it fetches the next &#x60;page&#x60; of locations. The page token is returned by previous calls to &#x60;ListLocations&#x60; when there were more locations than could fit in the requested page size.
    :type page_token: str
    :param read_mask: Required. Read mask to specify what fields will be returned in the response.
    :type read_mask: str

    """
    return web.Response(status=200)
