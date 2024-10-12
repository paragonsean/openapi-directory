from typing import List, Dict
from aiohttp import web

from openapi_server.models.inbound_sso_assignment import InboundSsoAssignment
from openapi_server.models.list_inbound_sso_assignments_response import ListInboundSsoAssignmentsResponse
from openapi_server.models.operation import Operation
from openapi_server import util


async def cloudidentity_inbound_sso_assignments_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_inbound_sso_assignments_create

    Creates an InboundSsoAssignment for users and devices in a &#x60;Customer&#x60; under a given &#x60;Group&#x60; or &#x60;OrgUnit&#x60;.

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
    body = InboundSsoAssignment.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_inbound_sso_assignments_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None) -> web.Response:
    """cloudidentity_inbound_sso_assignments_delete

    Deletes an InboundSsoAssignment. To disable SSO, Create (or Update) an assignment that has &#x60;sso_mode&#x60; &#x3D;&#x3D; &#x60;SSO_OFF&#x60;.

    :param name: Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the InboundSsoAssignment to delete. Format: &#x60;inboundSsoAssignments/{assignment}&#x60;
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
    :param customer: Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs.
    :type customer: str

    """
    return web.Response(status=200)


async def cloudidentity_inbound_sso_assignments_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, read_mask=None) -> web.Response:
    """cloudidentity_inbound_sso_assignments_get

    Gets an InboundSsoAssignment.

    :param name: Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the InboundSsoAssignment to fetch. Format: &#x60;inboundSsoAssignments/{assignment}&#x60;
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
    :param read_mask: Field-level read mask of which fields to return. \&quot;*\&quot; returns all fields. If not specified, all fields will be returned. May only contain the following field: &#x60;member_restriction&#x60;.
    :type read_mask: str

    """
    return web.Response(status=200)


async def cloudidentity_inbound_sso_assignments_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudidentity_inbound_sso_assignments_list

    Lists the InboundSsoAssignments for a &#x60;Customer&#x60;.

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
    :param filter: A CEL expression to filter the results. The only supported filter is filtering by customer. For example: &#x60;customer&#x3D;&#x3D;customers/C0123abc&#x60;. Omitting the filter or specifying a filter of &#x60;customer&#x3D;&#x3D;customers/my_customer&#x60; will return the assignments for the customer that the caller (authenticated user) belongs to.
    :type filter: str
    :param page_size: The maximum number of assignments to return. The service may return fewer than this value. If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time. The maximum allowed value is 100, though requests with page_size greater than that will be silently interpreted as having this maximum value. This may increase in the futue.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListInboundSsoAssignments&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListInboundSsoAssignments&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudidentity_inbound_sso_assignments_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """cloudidentity_inbound_sso_assignments_patch

    Updates an InboundSsoAssignment. The body of this request is the &#x60;inbound_sso_assignment&#x60; field and the &#x60;update_mask&#x60; is relative to that. For example: a PATCH to &#x60;/v1/inboundSsoAssignments/0abcdefg1234567&amp;update_mask&#x3D;rank&#x60; with a body of &#x60;{ \&quot;rank\&quot;: 1 }&#x60; moves that (presumably group-targeted) SSO assignment to the highest priority and shifts any other group-targeted assignments down in priority.

    :param name: Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Inbound SSO Assignment.
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
    :param update_mask: Required. The list of fields to be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = InboundSsoAssignment.from_dict(body)
    return web.Response(status=200)
