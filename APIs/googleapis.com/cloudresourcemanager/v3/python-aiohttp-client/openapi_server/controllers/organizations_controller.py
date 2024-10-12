from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_organizations_response import SearchOrganizationsResponse
from openapi_server import util


async def cloudresourcemanager_organizations_search(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudresourcemanager_organizations_search

    Searches organization resources that are visible to the user and satisfy the specified filter. This method returns organizations in an unspecified order. New organizations do not necessarily appear at the end of the results, and may take a small amount of time to appear. Search will only return organizations on which the user has the permission &#x60;resourcemanager.organizations.get&#x60; or has super admin privileges.

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
    :param page_size: Optional. The maximum number of organizations to return in the response. The server can return fewer organizations than requested. If unspecified, server picks an appropriate default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to &#x60;SearchOrganizations&#x60; that indicates from where listing should continue.
    :type page_token: str
    :param query: Optional. An optional query string used to filter the Organizations to return in the response. Query rules are case-insensitive. &#x60;&#x60;&#x60; | Field | Description | |------------------|--------------------------------------------| | directoryCustomerId, owner.directoryCustomerId | Filters by directory customer id. | | domain | Filters by domain. | &#x60;&#x60;&#x60; Organizations may be queried by &#x60;directoryCustomerId&#x60; or by &#x60;domain&#x60;, where the domain is a G Suite domain, for example: * Query &#x60;directorycustomerid:123456789&#x60; returns Organization resources with &#x60;owner.directory_customer_id&#x60; equal to &#x60;123456789&#x60;. * Query &#x60;domain:google.com&#x60; returns Organization resources corresponding to the domain &#x60;google.com&#x60;.
    :type query: str

    """
    return web.Response(status=200)
