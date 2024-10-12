from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.org_hook import OrgHook
from openapi_server.models.org_membership import OrgMembership
from openapi_server.models.organization_full import OrganizationFull
from openapi_server.models.organization_simple import OrganizationSimple
from openapi_server.models.orgs_create_webhook_request import OrgsCreateWebhookRequest
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.orgs_set_membership_for_user_request import OrgsSetMembershipForUserRequest
from openapi_server.models.orgs_update422_response import OrgsUpdate422Response
from openapi_server.models.orgs_update_membership_for_authenticated_user_request import OrgsUpdateMembershipForAuthenticatedUserRequest
from openapi_server.models.orgs_update_request import OrgsUpdateRequest
from openapi_server.models.orgs_update_webhook_request import OrgsUpdateWebhookRequest
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def orgs_check_membership_for_user(request: web.Request, org, username) -> web.Response:
    """Check organization membership for a user

    Check if a user is, publicly or privately, a member of the organization.

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_check_public_membership_for_user(request: web.Request, org, username) -> web.Response:
    """Check public organization membership for a user

    

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_convert_member_to_outside_collaborator(request: web.Request, org, username) -> web.Response:
    """Convert an organization member to outside collaborator

    When an organization member is converted to an outside collaborator, they&#39;ll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see \&quot;[Converting an organization member to an outside collaborator](https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)\&quot;.

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_create_webhook(request: web.Request, org, body) -> web.Response:
    """Create an organization webhook

    Here&#39;s how you can create a hook that posts payloads in JSON format:

    :param org: 
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrgsCreateWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def orgs_delete_webhook(request: web.Request, org, hook_id) -> web.Response:
    """Delete an organization webhook

    

    :param org: 
    :type org: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def orgs_get(request: web.Request, org) -> web.Response:
    """Get an organization

    To see many of the organization response values, you need to be an authenticated organization owner with the &#x60;admin:org&#x60; scope. When the value of &#x60;two_factor_requirement_enabled&#x60; is &#x60;true&#x60;, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).  GitHub Apps with the &#x60;Organization plan&#x60; permission can use this endpoint to retrieve information about an organization&#39;s GitHub Enterprise Server plan. See \&quot;[Authenticating with GitHub Apps](https://docs.github.com/enterprise-server@2.18/apps/building-github-apps/authenticating-with-github-apps/)\&quot; for details. For an example response, see &#39;Response with GitHub Enterprise Server plan information&#39; below.\&quot;

    :param org: 
    :type org: str

    """
    return web.Response(status=200)


async def orgs_get_membership_for_authenticated_user(request: web.Request, org) -> web.Response:
    """Get an organization membership for the authenticated user

    

    :param org: 
    :type org: str

    """
    return web.Response(status=200)


async def orgs_get_membership_for_user(request: web.Request, org, username) -> web.Response:
    """Get organization membership for a user

    In order to get a user&#39;s membership with an organization, the authenticated user must be an organization member. The &#x60;state&#x60; parameter in the response can be used to identify the user&#39;s membership status.

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_get_webhook(request: web.Request, org, hook_id) -> web.Response:
    """Get an organization webhook

    Returns a webhook configured in an organization. To get only the webhook &#x60;config&#x60; properties, see \&quot;[Get a webhook configuration for an organization](/rest/reference/orgs#get-a-webhook-configuration-for-an-organization).\&quot;

    :param org: 
    :type org: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def orgs_list(request: web.Request, since=None, per_page=None) -> web.Response:
    """List organizations

    Lists all organizations, in the order that they were created on GitHub Enterprise Server.  **Note:** Pagination is powered exclusively by the &#x60;since&#x60; parameter. Use the [Link header](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of organizations.

    :param since: An organization ID. Only return organizations with an ID greater than this ID.
    :type since: int
    :param per_page: Results per page (max 100)
    :type per_page: int

    """
    return web.Response(status=200)


async def orgs_list_for_authenticated_user(request: web.Request, per_page=None, page=None) -> web.Response:
    """List organizations for the authenticated user

    List organizations for the authenticated user.  **OAuth scope requirements**  This only lists organizations that your authorization allows you to operate on in some way (e.g., you can list teams with &#x60;read:org&#x60; scope, you can publicize your organization membership with &#x60;user&#x60; scope, etc.). Therefore, this API requires at least &#x60;user&#x60; or &#x60;read:org&#x60; scope. OAuth requests with insufficient scope receive a &#x60;403 Forbidden&#x60; response.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def orgs_list_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List organizations for a user

    List [public organization memberships](https://help.github.com/articles/publicizing-or-concealing-organization-membership) for the specified user.  This method only lists _public_ memberships, regardless of authentication. If you need to fetch all of the organization memberships (public and private) for the authenticated user, use the [List organizations for the authenticated user](https://docs.github.com/enterprise-server@2.18/rest/reference/orgs#list-organizations-for-the-authenticated-user) API instead.

    :param username: 
    :type username: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def orgs_list_members(request: web.Request, org, filter=None, role=None, per_page=None, page=None) -> web.Response:
    """List organization members

    List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned.

    :param org: 
    :type org: str
    :param filter: Filter members returned in the list. Can be one of:   \\* &#x60;2fa_disabled&#x60; - Members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled. Available for organization owners.   \\* &#x60;all&#x60; - All members the authenticated user can see.
    :type filter: str
    :param role: Filter members returned by their role. Can be one of:   \\* &#x60;all&#x60; - All members of the organization, regardless of role.   \\* &#x60;admin&#x60; - Organization owners.   \\* &#x60;member&#x60; - Non-owner organization members.
    :type role: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def orgs_list_memberships_for_authenticated_user(request: web.Request, state=None, per_page=None, page=None) -> web.Response:
    """List organization memberships for the authenticated user

    

    :param state: Indicates the state of the memberships to return. Can be either &#x60;active&#x60; or &#x60;pending&#x60;. If not specified, the API returns both active and pending memberships.
    :type state: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def orgs_list_outside_collaborators(request: web.Request, org, filter=None, per_page=None, page=None) -> web.Response:
    """List outside collaborators for an organization

    List all users who are outside collaborators of an organization.

    :param org: 
    :type org: str
    :param filter: Filter the list of outside collaborators. Can be one of:   \\* &#x60;2fa_disabled&#x60;: Outside collaborators without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled.   \\* &#x60;all&#x60;: All outside collaborators.
    :type filter: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def orgs_list_public_members(request: web.Request, org, per_page=None, page=None) -> web.Response:
    """List public organization members

    Members of an organization can choose to have their membership publicized or not.

    :param org: 
    :type org: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def orgs_list_webhooks(request: web.Request, org, per_page=None, page=None) -> web.Response:
    """List organization webhooks

    

    :param org: 
    :type org: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def orgs_ping_webhook(request: web.Request, org, hook_id) -> web.Response:
    """Ping an organization webhook

    This will trigger a [ping event](https://docs.github.com/enterprise-server@2.18/webhooks/#ping-event) to be sent to the hook.

    :param org: 
    :type org: str
    :param hook_id: 
    :type hook_id: int

    """
    return web.Response(status=200)


async def orgs_remove_member(request: web.Request, org, username) -> web.Response:
    """Remove an organization member

    Removing a user from this list will remove them from all teams and they will no longer have any access to the organization&#39;s repositories.

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_remove_membership_for_user(request: web.Request, org, username) -> web.Response:
    """Remove organization membership for a user

    In order to remove a user&#39;s membership with an organization, the authenticated user must be an organization owner.  If the specified user is an active member of the organization, this will remove them from the organization. If the specified user has been invited to the organization, this will cancel their invitation. The specified user will receive an email notification in both cases.

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_remove_outside_collaborator(request: web.Request, org, username) -> web.Response:
    """Remove outside collaborator from an organization

    Removing a user from this list will remove them from all the organization&#39;s repositories.

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_remove_public_membership_for_authenticated_user(request: web.Request, org, username) -> web.Response:
    """Remove public organization membership for the authenticated user

    

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_set_membership_for_user(request: web.Request, org, username, body=None) -> web.Response:
    """Set organization membership for a user

    Only authenticated organization owners can add a member to the organization or update the member&#39;s role.  *   If the authenticated user is _adding_ a member to the organization, the invited user will receive an email inviting them to the organization. The user&#39;s [membership status](https://docs.github.com/enterprise-server@2.18/rest/reference/orgs#get-organization-membership-for-a-user) will be &#x60;pending&#x60; until they accept the invitation.      *   Authenticated users can _update_ a user&#39;s membership by passing the &#x60;role&#x60; parameter. If the authenticated user changes a member&#39;s role to &#x60;admin&#x60;, the affected user will receive an email notifying them that they&#39;ve been made an organization owner. If the authenticated user changes an owner&#39;s role to &#x60;member&#x60;, no email will be sent.  **Rate limits**  To prevent abuse, the authenticated user is limited to 50 organization invitations per 24 hour period. If the organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period.

    :param org: 
    :type org: str
    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrgsSetMembershipForUserRequest.from_dict(body)
    return web.Response(status=200)


async def orgs_set_public_membership_for_authenticated_user(request: web.Request, org, username) -> web.Response:
    """Set public organization membership for the authenticated user

    The user can publicize their own membership. (A user cannot publicize the membership for another user.)  Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param org: 
    :type org: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def orgs_update(request: web.Request, org, body=None) -> web.Response:
    """Update an organization

    **Parameter Deprecation Notice:** GitHub Enterprise Server will replace and discontinue &#x60;members_allowed_repository_creation_type&#x60; in favor of more granular permissions. The new input parameters are &#x60;members_can_create_public_repositories&#x60;, &#x60;members_can_create_private_repositories&#x60; for all organizations and &#x60;members_can_create_internal_repositories&#x60; for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).  Enables an authenticated organization owner with the &#x60;admin:org&#x60; scope to update the organization&#39;s profile and member privileges.

    :param org: 
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrgsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def orgs_update_membership_for_authenticated_user(request: web.Request, org, body) -> web.Response:
    """Update an organization membership for the authenticated user

    

    :param org: 
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrgsUpdateMembershipForAuthenticatedUserRequest.from_dict(body)
    return web.Response(status=200)


async def orgs_update_webhook(request: web.Request, org, hook_id, body=None) -> web.Response:
    """Update an organization webhook

    Updates a webhook configured in an organization. When you update a webhook, the &#x60;secret&#x60; will be overwritten. If you previously had a &#x60;secret&#x60; set, you must provide the same &#x60;secret&#x60; or set a new &#x60;secret&#x60; or the secret will be removed. If you are only updating individual webhook &#x60;config&#x60; properties, use \&quot;[Update a webhook configuration for an organization](/rest/reference/orgs#update-a-webhook-configuration-for-an-organization).\&quot;

    :param org: 
    :type org: str
    :param hook_id: 
    :type hook_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = OrgsUpdateWebhookRequest.from_dict(body)
    return web.Response(status=200)
