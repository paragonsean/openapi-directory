from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_domain import CustomDomain
from openapi_server.models.list_custom_domains_response import ListCustomDomainsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_sites_response import ListSitesResponse
from openapi_server.models.operation import Operation
from openapi_server.models.site import Site
from openapi_server.models.undelete_custom_domain_request import UndeleteCustomDomainRequest
from openapi_server import util


async def firebasehosting_projects_sites_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, site_id=None, validate_only=None, body=None) -> web.Response:
    """firebasehosting_projects_sites_create

    Creates a new Hosting Site in the specified parent Firebase project. Note that Hosting sites can take several minutes to propagate through Firebase systems.

    :param parent: Required. The Firebase project in which to create a Hosting site, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;Site&#x60; [&#x60;name&#x60;](../projects#Site.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param site_id: Required. Immutable. A globally unique identifier for the Hosting site. This identifier is used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid domain name label.
    :type site_id: str
    :param validate_only: Optional. If set, validates that the site_id is available and that the request would succeed, returning the expected resulting site or error.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Site.from_dict(body)
    return web.Response(status=200)


async def firebasehosting_projects_sites_custom_domains_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, custom_domain_id=None, validate_only=None, body=None) -> web.Response:
    """firebasehosting_projects_sites_custom_domains_create

    Creates a &#x60;CustomDomain&#x60;.

    :param parent: Required. The custom domain&#39;s parent, specifically a Firebase Hosting &#x60;Site&#x60;.
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
    :param custom_domain_id: Required. The ID of the &#x60;CustomDomain&#x60;, which is the domain name you&#39;d like to use with Firebase Hosting.
    :type custom_domain_id: str
    :param validate_only: If true, Hosting validates that it&#39;s possible to complete your request but doesn&#39;t actually create a new &#x60;CustomDomain&#x60;.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = CustomDomain.from_dict(body)
    return web.Response(status=200)


async def firebasehosting_projects_sites_custom_domains_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """firebasehosting_projects_sites_custom_domains_list

    Lists each &#x60;CustomDomain&#x60; associated with the specified parent Hosting site. Returns &#x60;CustomDomain&#x60;s in a consistent, but undefined, order to facilitate pagination.

    :param parent: Required. The Firebase Hosting &#x60;Site&#x60; with &#x60;CustomDomain&#x60; entities you&#39;d like to list.
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
    :param page_size: The max number of &#x60;CustomDomain&#x60; entities to return in a request. Defaults to 10.
    :type page_size: int
    :param page_token: A token from a previous call to &#x60;ListCustomDomains&#x60; that tells the server where to resume listing.
    :type page_token: str
    :param show_deleted: If true, the request returns soft-deleted &#x60;CustomDomain&#x60;s that haven&#39;t been fully-deleted yet. To restore deleted &#x60;CustomDomain&#x60;s, make an &#x60;UndeleteCustomDomain&#x60; request.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def firebasehosting_projects_sites_custom_domains_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firebasehosting_projects_sites_custom_domains_operations_list

    Lists operations that match the specified filter in the request.

    :param name: The name of the operation&#39;s parent resource.
    :type name: str
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
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def firebasehosting_projects_sites_custom_domains_undelete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebasehosting_projects_sites_custom_domains_undelete

    Undeletes the specified &#x60;CustomDomain&#x60; if it has been soft-deleted. Hosting retains soft-deleted custom domains for around 30 days before permanently deleting them.

    :param name: Required. The name of the &#x60;CustomDomain&#x60; to delete.
    :type name: str
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
    body = UndeleteCustomDomainRequest.from_dict(body)
    return web.Response(status=200)


async def firebasehosting_projects_sites_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """firebasehosting_projects_sites_list

    Lists each Hosting Site associated with the specified parent Firebase project.

    :param parent: Required. The Firebase project for which to list sites, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;Site&#x60; [&#x60;name&#x60;](../projects#Site.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param page_size: Optional. The maximum number of sites to return. The service may return a lower number if fewer sites exist than this maximum number. If unspecified, defaults to 40.
    :type page_size: int
    :param page_token: Optional. A token from a previous call to &#x60;ListSites&#x60; that tells the server where to resume listing.
    :type page_token: str

    """
    return web.Response(status=200)
