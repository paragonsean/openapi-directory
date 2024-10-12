from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_orgpolicy_v2_custom_constraint import GoogleCloudOrgpolicyV2CustomConstraint
from openapi_server.models.google_cloud_orgpolicy_v2_list_custom_constraints_response import GoogleCloudOrgpolicyV2ListCustomConstraintsResponse
from openapi_server import util


async def orgpolicy_organizations_custom_constraints_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """orgpolicy_organizations_custom_constraints_create

    Creates a custom constraint. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the organization does not exist. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.ALREADY_EXISTS&#x60; if the constraint already exists on the given organization.

    :param parent: Required. Must be in the following form: * &#x60;organizations/{organization_id}&#x60;
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudOrgpolicyV2CustomConstraint.from_dict(body)
    return web.Response(status=200)


async def orgpolicy_organizations_custom_constraints_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """orgpolicy_organizations_custom_constraints_list

    Retrieves all of the custom constraints that exist on a particular organization resource.

    :param parent: Required. The target Google Cloud resource that parents the set of custom constraints that will be returned from this call. Must be in one of the following forms: * &#x60;organizations/{organization_id}&#x60;
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
    :param page_size: Size of the pages to be returned. This is currently unsupported and will be ignored. The server may at any point start using this field to limit page size.
    :type page_size: int
    :param page_token: Page token used to retrieve the next page. This is currently unsupported and will be ignored. The server may at any point start using this field.
    :type page_token: str

    """
    return web.Response(status=200)
