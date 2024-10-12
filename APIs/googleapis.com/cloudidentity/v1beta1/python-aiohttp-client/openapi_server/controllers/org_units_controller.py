from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_org_memberships_response import ListOrgMembershipsResponse
from openapi_server.models.move_org_membership_request import MoveOrgMembershipRequest
from openapi_server.models.operation import Operation
from openapi_server import util


async def cloudidentity_org_units_memberships_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudidentity_org_units_memberships_list

    List OrgMembership resources in an OrgUnit treated as &#39;parent&#39;. Parent format: orgUnits/{$orgUnitId} where &#x60;$orgUnitId&#x60; is the &#x60;orgUnitId&#x60; from the [Admin SDK &#x60;OrgUnit&#x60; resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)

    :param parent: Required. Immutable. OrgUnit which is queried for a list of memberships. Format: orgUnits/{$orgUnitId} where &#x60;$orgUnitId&#x60; is the &#x60;orgUnitId&#x60; from the [Admin SDK &#x60;OrgUnit&#x60; resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits).
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
    :param customer: Required. Immutable. Customer that this OrgMembership belongs to. All authorization will happen on the role assignments of this customer. Format: customers/{$customerId} where &#x60;$customerId&#x60; is the &#x60;id&#x60; from the [Admin SDK &#x60;Customer&#x60; resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/customers). You may also use &#x60;customers/my_customer&#x60; to specify your own organization.
    :type customer: str
    :param filter: The search query. Must be specified in [Common Expression Language](https://opensource.google/projects/cel). May only contain equality operators on the &#x60;type&#x60; (e.g., &#x60;type &#x3D;&#x3D; &#39;shared_drive&#39;&#x60;).
    :type filter: str
    :param page_size: The maximum number of results to return. The service may return fewer than this value. If omitted (or defaulted to zero) the server will default to 50. The maximum allowed value is 100, though requests with page_size greater than that will be silently interpreted as 100.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;OrgMembershipsService.ListOrgMemberships&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListOrgMembershipsRequest&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudidentity_org_units_memberships_move(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_org_units_memberships_move

    Move an OrgMembership to a new OrgUnit. NOTE: This is an atomic copy-and-delete. The resource will have a new copy under the destination OrgUnit and be deleted from the source OrgUnit. The resource can only be searched under the destination OrgUnit afterwards.

    :param name: Required. Immutable. The [resource name](https://cloud.google.com/apis/design/resource_names) of the OrgMembership. Format: orgUnits/{$orgUnitId}/memberships/{$membership} The &#x60;$orgUnitId&#x60; is the &#x60;orgUnitId&#x60; from the [Admin SDK &#x60;OrgUnit&#x60; resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits). To manage a Membership without specifying source &#x60;orgUnitId&#x60;, this API also supports the wildcard character &#39;-&#39; for &#x60;$orgUnitId&#x60; per https://google.aip.dev/159. The &#x60;$membership&#x60; shall be of the form &#x60;{$entityType};{$memberId}&#x60;, where &#x60;$entityType&#x60; is the enum value of OrgMembership.EntityType, and &#x60;memberId&#x60; is the &#x60;id&#x60; from [Drive API (V3) &#x60;Drive&#x60; resource](https://developers.google.com/drive/api/v3/reference/drives#resource) for OrgMembership.EntityType.SHARED_DRIVE.
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
    body = MoveOrgMembershipRequest.from_dict(body)
    return web.Response(status=200)
