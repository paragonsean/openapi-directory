from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_transitive_membership_response import CheckTransitiveMembershipResponse
from openapi_server.models.group import Group
from openapi_server.models.list_groups_response import ListGroupsResponse
from openapi_server.models.list_memberships_response import ListMembershipsResponse
from openapi_server.models.lookup_group_name_response import LookupGroupNameResponse
from openapi_server.models.lookup_membership_name_response import LookupMembershipNameResponse
from openapi_server.models.membership import Membership
from openapi_server.models.modify_membership_roles_request import ModifyMembershipRolesRequest
from openapi_server.models.modify_membership_roles_response import ModifyMembershipRolesResponse
from openapi_server.models.operation import Operation
from openapi_server.models.search_direct_groups_response import SearchDirectGroupsResponse
from openapi_server.models.search_groups_response import SearchGroupsResponse
from openapi_server.models.search_transitive_groups_response import SearchTransitiveGroupsResponse
from openapi_server.models.search_transitive_memberships_response import SearchTransitiveMembershipsResponse
from openapi_server import util


async def cloudidentity_groups_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, initial_group_config=None, body=None) -> web.Response:
    """cloudidentity_groups_create

    Creates a Group.

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
    :param initial_group_config: Optional. The initial configuration option for the &#x60;Group&#x60;.
    :type initial_group_config: str
    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_groups_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, parent=None, view=None) -> web.Response:
    """cloudidentity_groups_list

    Lists the &#x60;Group&#x60; resources under a customer or namespace.

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
    :param page_size: The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a &#x60;next_page_token&#x60;. If unspecified, defaults to 200 for &#x60;View.BASIC&#x60; and to 50 for &#x60;View.FULL&#x60;. Must not be greater than 1000 for &#x60;View.BASIC&#x60; or 500 for &#x60;View.FULL&#x60;.
    :type page_size: int
    :param page_token: The &#x60;next_page_token&#x60; value returned from a previous list request, if any.
    :type page_token: str
    :param parent: Required. The parent resource under which to list all &#x60;Group&#x60; resources. Must be of the form &#x60;identitysources/{identity_source}&#x60; for external- identity-mapped groups or &#x60;customers/{customer_id}&#x60; for Google Groups. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793)
    :type parent: str
    :param view: The level of detail to be returned. If unspecified, defaults to &#x60;View.BASIC&#x60;.
    :type view: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_lookup(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, group_key_id=None, group_key_namespace=None) -> web.Response:
    """cloudidentity_groups_lookup

    Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a &#x60;Group&#x60; by its &#x60;EntityKey&#x60;.

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
    :param group_key_id: The ID of the entity. For Google-managed entities, the &#x60;id&#x60; should be the email address of an existing group or user. Email addresses need to adhere to [name guidelines for users and groups](https://support.google.com/a/answer/9193374). For external-identity-mapped entities, the &#x60;id&#x60; must be a string conforming to the Identity Source&#39;s requirements. Must be unique within a &#x60;namespace&#x60;.
    :type group_key_id: str
    :param group_key_namespace: The namespace in which the entity exists. If not specified, the &#x60;EntityKey&#x60; represents a Google-managed entity such as a Google user or a Google Group. If specified, the &#x60;EntityKey&#x60; represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of &#x60;identitysources/{identity_source}&#x60;.
    :type group_key_namespace: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_memberships_check_transitive_membership(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, query=None) -> web.Response:
    """cloudidentity_groups_memberships_check_transitive_membership

    Check a potential member for membership in a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A member has membership to a group as long as there is a single viewable transitive membership between the group and the member. The actor must have view permissions to at least one transitive membership between the member and group.

    :param parent: [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to check the transitive membership in. Format: &#x60;groups/{group}&#x60;, where &#x60;group&#x60; is the unique id assigned to the Group to which the Membership belongs to.
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
    :param query: Required. A CEL expression that MUST include member specification. This is a &#x60;required&#x60; field. Certain groups are uniquely identified by both a &#39;member_key_id&#39; and a &#39;member_key_namespace&#39;, which requires an additional query input: &#39;member_key_namespace&#39;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39;&#x60;
    :type query: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_memberships_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_groups_memberships_create

    Creates a &#x60;Membership&#x60;.

    :param parent: Required. The parent &#x60;Group&#x60; resource under which to create the &#x60;Membership&#x60;. Must be of the form &#x60;groups/{group}&#x60;.
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
    body = Membership.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_groups_memberships_get_membership_graph(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, query=None) -> web.Response:
    """cloudidentity_groups_memberships_get_membership_graph

    Get a membership graph of just a member or both a member and a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. Given a member, the response will contain all membership paths from the member. Given both a group and a member, the response will contain all membership paths between the group and the member.

    :param parent: Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group}&#x60;, where &#x60;group&#x60; is the unique ID assigned to the Group to which the Membership belongs to. group can be a wildcard collection id \&quot;-\&quot;. When a group is specified, the membership graph will be constrained to paths between the member (defined in the query) and the parent. If a wildcard collection is provided, all membership paths connected to the member will be returned.
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
    :param query: Required. A CEL expression that MUST include member specification AND label(s). Certain groups are uniquely identified by both a &#39;member_key_id&#39; and a &#39;member_key_namespace&#39;, which requires an additional query input: &#39;member_key_namespace&#39;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels&#x60;
    :type query: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_memberships_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, view=None) -> web.Response:
    """cloudidentity_groups_memberships_list

    Lists the &#x60;Membership&#x60;s within a &#x60;Group&#x60;.

    :param parent: Required. The parent &#x60;Group&#x60; resource under which to lookup the &#x60;Membership&#x60; name. Must be of the form &#x60;groups/{group}&#x60;.
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
    :param page_size: The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a &#x60;next_page_token&#x60;. If unspecified, defaults to 200 for &#x60;GroupView.BASIC&#x60; and to 50 for &#x60;GroupView.FULL&#x60;. Must not be greater than 1000 for &#x60;GroupView.BASIC&#x60; or 500 for &#x60;GroupView.FULL&#x60;.
    :type page_size: int
    :param page_token: The &#x60;next_page_token&#x60; value returned from a previous search request, if any.
    :type page_token: str
    :param view: The level of detail to be returned. If unspecified, defaults to &#x60;View.BASIC&#x60;.
    :type view: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_memberships_lookup(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, member_key_id=None, member_key_namespace=None) -> web.Response:
    """cloudidentity_groups_memberships_lookup

    Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a &#x60;Membership&#x60; by its &#x60;EntityKey&#x60;.

    :param parent: Required. The parent &#x60;Group&#x60; resource under which to lookup the &#x60;Membership&#x60; name. Must be of the form &#x60;groups/{group}&#x60;.
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
    :param member_key_id: The ID of the entity. For Google-managed entities, the &#x60;id&#x60; should be the email address of an existing group or user. Email addresses need to adhere to [name guidelines for users and groups](https://support.google.com/a/answer/9193374). For external-identity-mapped entities, the &#x60;id&#x60; must be a string conforming to the Identity Source&#39;s requirements. Must be unique within a &#x60;namespace&#x60;.
    :type member_key_id: str
    :param member_key_namespace: The namespace in which the entity exists. If not specified, the &#x60;EntityKey&#x60; represents a Google-managed entity such as a Google user or a Google Group. If specified, the &#x60;EntityKey&#x60; represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of &#x60;identitysources/{identity_source}&#x60;.
    :type member_key_namespace: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_memberships_modify_membership_roles(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_groups_memberships_modify_membership_roles

    Modifies the &#x60;MembershipRole&#x60;s of a &#x60;Membership&#x60;.

    :param name: Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Membership&#x60; whose roles are to be modified. Must be of the form &#x60;groups/{group}/memberships/{membership}&#x60;.
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
    body = ModifyMembershipRolesRequest.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_groups_memberships_search_direct_groups(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, order_by=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudidentity_groups_memberships_search_direct_groups

    Searches direct groups of a member.

    :param parent: [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: groups/{group_id}, where group_id is always &#39;-&#39; as this API will search across all groups for a given member.
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
    :param order_by: The ordering of membership relation for the display name or email in the response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending display name: order_by&#x3D;\&quot;group_name\&quot; or order_by&#x3D;\&quot;group_name asc\&quot;. Sort by the descending display name: order_by&#x3D;\&quot;group_name desc\&quot;. Sort by the ascending group key: order_by&#x3D;\&quot;group_key\&quot; or order_by&#x3D;\&quot;group_key asc\&quot;. Sort by the descending group key: order_by&#x3D;\&quot;group_key desc\&quot;.
    :type order_by: str
    :param page_size: The default page size is 200 (max 1000).
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous list request, if any
    :type page_token: str
    :param query: Required. A CEL expression that MUST include member specification AND label(s). Users can search on label attributes of groups. CONTAINS match (&#39;in&#39;) is supported on labels. Identity-mapped groups are uniquely identified by both a &#x60;member_key_id&#x60; and a &#x60;member_key_namespace&#x60;, which requires an additional query input: &#x60;member_key_namespace&#x60;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; &#39;label_value&#39; in labels&#x60;
    :type query: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_memberships_search_transitive_groups(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudidentity_groups_memberships_search_transitive_groups

    Search transitive groups of a member. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive group is any group that has a direct or indirect membership to the member. Actor must have view permissions all transitive groups.

    :param parent: [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group}&#x60;, where &#x60;group&#x60; is always &#39;-&#39; as this API will search across all groups for a given member.
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
    :param page_size: The default page size is 200 (max 1000).
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous list request, if any.
    :type page_token: str
    :param query: Required. A CEL expression that MUST include member specification AND label(s). This is a &#x60;required&#x60; field. Users can search on label attributes of groups. CONTAINS match (&#39;in&#39;) is supported on labels. Identity-mapped groups are uniquely identified by both a &#x60;member_key_id&#x60; and a &#x60;member_key_namespace&#x60;, which requires an additional query input: &#x60;member_key_namespace&#x60;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels&#x60; Query may optionally contain equality operators on the parent of the group restricting the search within a particular customer, e.g. &#x60;parent &#x3D;&#x3D; &#39;customers/{customer_id}&#39;&#x60;. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). This filtering is only supported for Admins with groups read permissons on the input customer. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels &amp;&amp; parent &#x3D;&#x3D; &#39;customers/C046psxkn&#39;&#x60;
    :type query: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_memberships_search_transitive_memberships(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudidentity_groups_memberships_search_transitive_memberships

    Search transitive memberships of a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the group is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive membership is any direct or indirect membership of a group. Actor must have view permissions to all transitive memberships.

    :param parent: [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group}&#x60;, where &#x60;group&#x60; is the unique ID assigned to the Group.
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
    :param page_size: The default page size is 200 (max 1000).
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous list request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudidentity_groups_search(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None, view=None) -> web.Response:
    """cloudidentity_groups_search

    Searches for &#x60;Group&#x60; resources matching a specified query.

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
    :param page_size: The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a &#x60;next_page_token&#x60;. If unspecified, defaults to 200 for &#x60;GroupView.BASIC&#x60; and 50 for &#x60;GroupView.FULL&#x60;. Must not be greater than 1000 for &#x60;GroupView.BASIC&#x60; or 500 for &#x60;GroupView.FULL&#x60;.
    :type page_size: int
    :param page_token: The &#x60;next_page_token&#x60; value returned from a previous search request, if any.
    :type page_token: str
    :param query: Required. The search query. * Must be specified in [Common Expression Language](https://opensource.google/projects/cel). * Must contain equality operators on the parent, e.g. &#x60;parent &#x3D;&#x3D; &#39;customers/{customer_id}&#39;&#x60;. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) * Can contain optional inclusion operators on &#x60;labels&#x60; such as &#x60;&#39;cloudidentity.googleapis.com/groups.discussion_forum&#39; in labels&#x60;). * Can contain an optional equality operator on &#x60;domain_name&#x60;. e.g. &#x60;domain_name &#x3D;&#x3D; &#39;examplepetstore.com&#39;&#x60; * Can contain optional &#x60;startsWith/contains/equality&#x60; operators on &#x60;group_key&#x60;, e.g. &#x60;group_key.startsWith(&#39;dev&#39;)&#x60;, &#x60;group_key.contains(&#39;dev&#39;), group_key &#x3D;&#x3D; &#39;dev@examplepetstore.com&#39;&#x60; * Can contain optional &#x60;startsWith/contains/equality&#x60; operators on &#x60;display_name&#x60;, such as &#x60;display_name.startsWith(&#39;dev&#39;)&#x60; , &#x60;display_name.contains(&#39;dev&#39;)&#x60;, &#x60;display_name &#x3D;&#x3D; &#39;dev&#39;&#x60;
    :type query: str
    :param view: The level of detail to be returned. If unspecified, defaults to &#x60;View.BASIC&#x60;.
    :type view: str

    """
    return web.Response(status=200)
