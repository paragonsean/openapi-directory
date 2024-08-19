from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.minimal_repository import MinimalRepository
from openapi_server.models.orgs_remove_outside_collaborator422_response import OrgsRemoveOutsideCollaborator422Response
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.team import Team
from openapi_server.models.team_discussion import TeamDiscussion
from openapi_server.models.team_discussion_comment import TeamDiscussionComment
from openapi_server.models.team_full import TeamFull
from openapi_server.models.team_membership import TeamMembership
from openapi_server.models.team_project import TeamProject
from openapi_server.models.team_repository import TeamRepository
from openapi_server.models.teams_add_or_update_membership_for_user_in_org_request import TeamsAddOrUpdateMembershipForUserInOrgRequest
from openapi_server.models.teams_add_or_update_project_permissions_in_org_request import TeamsAddOrUpdateProjectPermissionsInOrgRequest
from openapi_server.models.teams_add_or_update_project_permissions_legacy_request import TeamsAddOrUpdateProjectPermissionsLegacyRequest
from openapi_server.models.teams_add_or_update_repo_permissions_in_org_request import TeamsAddOrUpdateRepoPermissionsInOrgRequest
from openapi_server.models.teams_add_or_update_repo_permissions_legacy_request import TeamsAddOrUpdateRepoPermissionsLegacyRequest
from openapi_server.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest
from openapi_server.models.teams_create_discussion_in_org_request import TeamsCreateDiscussionInOrgRequest
from openapi_server.models.teams_create_request import TeamsCreateRequest
from openapi_server.models.teams_update_discussion_in_org_request import TeamsUpdateDiscussionInOrgRequest
from openapi_server.models.teams_update_in_org_request import TeamsUpdateInOrgRequest
from openapi_server.models.teams_update_legacy_request import TeamsUpdateLegacyRequest
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def teams_add_member_legacy(request: web.Request, team_id, username) -> web.Response:
    """Add team member (Legacy)

    The \&quot;Add team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Add or update team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they&#39;re changing. The person being added to the team must be a member of the team&#39;s organization.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param team_id: 
    :type team_id: int
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def teams_add_or_update_membership_for_user_in_org(request: web.Request, org, team_slug, username, body=None) -> web.Response:
    """Add or update team membership for a user

    Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Adds an organization member to a team. An authenticated organization owner or team maintainer can add organization members to a team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  An organization owner can add someone who is not part of the team&#39;s organization to a team. When an organization owner adds someone to a team who is not an organization member, this endpoint will send an invitation to the person via email. This newly-created membership will be in the \&quot;pending\&quot; state until the person accepts the invitation, at which point the membership will transition to the \&quot;active\&quot; state and the user will be added as a member of the team.  If the user is already a member of the team, this endpoint will update the role of the team member&#39;s role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PUT /organizations/{org_id}/team/{team_id}/memberships/{username}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsAddOrUpdateMembershipForUserInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_add_or_update_membership_for_user_legacy(request: web.Request, team_id, username, body=None) -> web.Response:
    """Add or update team membership for a user (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  If the user is already a member of the team&#39;s organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  If the user is unaffiliated with the team&#39;s organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the \&quot;pending\&quot; state until the user accepts the invitation, at which point the membership will transition to the \&quot;active\&quot; state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.  If the user is already a member of the team, this endpoint will update the role of the team member&#39;s role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

    :param team_id: 
    :type team_id: int
    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsAddOrUpdateMembershipForUserInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_add_or_update_project_permissions_in_org(request: web.Request, org, team_slug, project_id, body=None) -> web.Response:
    """Add or update team project permissions

    Adds an organization project to a team. To add a project to a team or update the team&#39;s permission on a project, the authenticated user must have &#x60;admin&#x60; permissions for the project. The project and team must be part of the same organization.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PUT /organizations/{org_id}/team/{team_id}/projects/{project_id}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param project_id: 
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsAddOrUpdateProjectPermissionsInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_add_or_update_project_permissions_legacy(request: web.Request, team_id, project_id, body=None) -> web.Response:
    """Add or update team project permissions (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-project-permissions) endpoint.  Adds an organization project to a team. To add a project to a team or update the team&#39;s permission on a project, the authenticated user must have &#x60;admin&#x60; permissions for the project. The project and team must be part of the same organization.

    :param team_id: 
    :type team_id: int
    :param project_id: 
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsAddOrUpdateProjectPermissionsLegacyRequest.from_dict(body)
    return web.Response(status=200)


async def teams_add_or_update_repo_permissions_in_org(request: web.Request, org, team_slug, owner, repo, body=None) -> web.Response:
    """Add or update team repository permissions

    To add a repository to a team or update the team&#39;s permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a &#x60;422 Unprocessable Entity&#x60; status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}&#x60;.  For more information about the permission levels, see \&quot;[Repository permission levels for an organization](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)\&quot;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsAddOrUpdateRepoPermissionsInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_add_or_update_repo_permissions_legacy(request: web.Request, team_id, owner, repo, body=None) -> web.Response:
    """Add or update team repository permissions (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new \&quot;[Add or update team repository permissions](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-repository-permissions)\&quot; endpoint.  To add a repository to a team or update the team&#39;s permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a &#x60;422 Unprocessable Entity&#x60; status if you attempt to add a repository to a team that is not owned by the organization.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param team_id: 
    :type team_id: int
    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsAddOrUpdateRepoPermissionsLegacyRequest.from_dict(body)
    return web.Response(status=200)


async def teams_check_permissions_for_project_in_org(request: web.Request, org, team_slug, project_id) -> web.Response:
    """Check team permissions for a project

    Checks whether a team has &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60; permissions for an organization project. The response includes projects inherited from a parent team.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/projects/{project_id}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param project_id: 
    :type project_id: int

    """
    return web.Response(status=200)


async def teams_check_permissions_for_project_legacy(request: web.Request, team_id, project_id) -> web.Response:
    """Check team permissions for a project (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#check-team-permissions-for-a-project) endpoint.  Checks whether a team has &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60; permissions for an organization project. The response includes projects inherited from a parent team.

    :param team_id: 
    :type team_id: int
    :param project_id: 
    :type project_id: int

    """
    return web.Response(status=200)


async def teams_check_permissions_for_repo_in_org(request: web.Request, org, team_slug, owner, repo) -> web.Response:
    """Check team permissions for a repository

    Checks whether a team has &#x60;admin&#x60;, &#x60;push&#x60;, &#x60;maintain&#x60;, &#x60;triage&#x60;, or &#x60;pull&#x60; permission for a repository. Repositories inherited through a parent team will also be checked.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@2.21/rest/overview/media-types/) via the &#x60;application/vnd.github.v3.repository+json&#x60; accept header.  If a team doesn&#39;t have permission for the repository, you will receive a &#x60;404 Not Found&#x60; response status.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def teams_check_permissions_for_repo_legacy(request: web.Request, team_id, owner, repo) -> web.Response:
    """Check team permissions for a repository (Legacy)

    **Note**: Repositories inherited through a parent team will also be checked.  **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#check-team-permissions-for-a-repository) endpoint.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@2.21/rest/overview/media-types/) via the &#x60;Accept&#x60; header:

    :param team_id: 
    :type team_id: int
    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def teams_create(request: web.Request, org, body) -> web.Response:
    """Create a team

    To create a team, the authenticated user must be a member or owner of &#x60;{org}&#x60;. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see \&quot;[Setting team creation permissions](https://help.github.com/en/articles/setting-team-creation-permissions-in-your-organization).\&quot;  When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of &#x60;maintainers&#x60;. For more information, see \&quot;[About teams](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/about-teams)\&quot;.

    :param org: 
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def teams_create_discussion_comment_in_org(request: web.Request, org, team_slug, discussion_number, body) -> web.Response:
    """Create a discussion comment

    Creates a new comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateDiscussionCommentInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_create_discussion_comment_legacy(request: web.Request, team_id, discussion_number, body) -> web.Response:
    """Create a discussion comment (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Create a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-discussion-comment) endpoint.  Creates a new comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateDiscussionCommentInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_create_discussion_in_org(request: web.Request, org, team_slug, body) -> web.Response:
    """Create a discussion

    Creates a new discussion post on a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/{org_id}/team/{team_id}/discussions&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateDiscussionInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_create_discussion_legacy(request: web.Request, team_id, body) -> web.Response:
    """Create a discussion (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;Create a discussion&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-discussion) endpoint.  Creates a new discussion post on a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

    :param team_id: 
    :type team_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateDiscussionInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_delete_discussion_comment_in_org(request: web.Request, org, team_slug, discussion_number, comment_number) -> web.Response:
    """Delete a discussion comment

    Deletes a comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int

    """
    return web.Response(status=200)


async def teams_delete_discussion_comment_legacy(request: web.Request, team_id, discussion_number, comment_number) -> web.Response:
    """Delete a discussion comment (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#delete-a-discussion-comment) endpoint.  Deletes a comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int

    """
    return web.Response(status=200)


async def teams_delete_discussion_in_org(request: web.Request, org, team_slug, discussion_number) -> web.Response:
    """Delete a discussion

    Delete a discussion from a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int

    """
    return web.Response(status=200)


async def teams_delete_discussion_legacy(request: web.Request, team_id, discussion_number) -> web.Response:
    """Delete a discussion (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;Delete a discussion&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#delete-a-discussion) endpoint.  Delete a discussion from a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int

    """
    return web.Response(status=200)


async def teams_delete_in_org(request: web.Request, org, team_slug) -> web.Response:
    """Delete a team

    To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str

    """
    return web.Response(status=200)


async def teams_delete_legacy(request: web.Request, team_id) -> web.Response:
    """Delete a team (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#delete-a-team) endpoint.  To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.

    :param team_id: 
    :type team_id: int

    """
    return web.Response(status=200)


async def teams_get_by_name(request: web.Request, org, team_slug) -> web.Response:
    """Get a team by name

    Gets a team using the team&#39;s &#x60;slug&#x60;. GitHub Enterprise Server generates the &#x60;slug&#x60; from the team &#x60;name&#x60;.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str

    """
    return web.Response(status=200)


async def teams_get_discussion_comment_in_org(request: web.Request, org, team_slug, discussion_number, comment_number) -> web.Response:
    """Get a discussion comment

    Get a specific comment on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int

    """
    return web.Response(status=200)


async def teams_get_discussion_comment_legacy(request: web.Request, team_id, discussion_number, comment_number) -> web.Response:
    """Get a discussion comment (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-a-discussion-comment) endpoint.  Get a specific comment on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int

    """
    return web.Response(status=200)


async def teams_get_discussion_in_org(request: web.Request, org, team_slug, discussion_number) -> web.Response:
    """Get a discussion

    Get a specific discussion on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int

    """
    return web.Response(status=200)


async def teams_get_discussion_legacy(request: web.Request, team_id, discussion_number) -> web.Response:
    """Get a discussion (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-a-discussion) endpoint.  Get a specific discussion on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int

    """
    return web.Response(status=200)


async def teams_get_legacy(request: web.Request, team_id) -> web.Response:
    """Get a team (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-a-team-by-name) endpoint.

    :param team_id: 
    :type team_id: int

    """
    return web.Response(status=200)


async def teams_get_member_legacy(request: web.Request, team_id, username) -> web.Response:
    """Get team member (Legacy)

    The \&quot;Get team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Get team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.  To list members in a team, the team must be visible to the authenticated user.

    :param team_id: 
    :type team_id: int
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def teams_get_membership_for_user_in_org(request: web.Request, org, team_slug, username) -> web.Response:
    """Get team membership for a user

    Team members will include the members of child teams.  To get a user&#39;s membership with a team, the team must be visible to the authenticated user.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/memberships/{username}&#x60;.  **Note:** The response contains the &#x60;state&#x60; of the membership and the member&#39;s &#x60;role&#x60;.  The &#x60;role&#x60; for organization owners is set to &#x60;maintainer&#x60;. For more information about &#x60;maintainer&#x60; roles, see see [Create a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-team).

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def teams_get_membership_for_user_legacy(request: web.Request, team_id, username) -> web.Response:
    """Get team membership for a user (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-team-membership-for-a-user) endpoint.  Team members will include the members of child teams.  To get a user&#39;s membership with a team, the team must be visible to the authenticated user.  **Note:** The response contains the &#x60;state&#x60; of the membership and the member&#39;s &#x60;role&#x60;.  The &#x60;role&#x60; for organization owners is set to &#x60;maintainer&#x60;. For more information about &#x60;maintainer&#x60; roles, see [Create a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-team).

    :param team_id: 
    :type team_id: int
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def teams_list(request: web.Request, org, per_page=None, page=None) -> web.Response:
    """List teams

    Lists all teams in an organization that are visible to the authenticated user.

    :param org: 
    :type org: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_child_in_org(request: web.Request, org, team_slug, per_page=None, page=None) -> web.Response:
    """List child teams

    Lists the child teams of the team specified by &#x60;{team_slug}&#x60;.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/teams&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_child_legacy(request: web.Request, team_id, per_page=None, page=None) -> web.Response:
    """List child teams (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List child teams&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-child-teams) endpoint.

    :param team_id: 
    :type team_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_discussion_comments_in_org(request: web.Request, org, team_slug, discussion_number, direction=None, per_page=None, page=None) -> web.Response:
    """List discussion comments

    List all comments on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_discussion_comments_legacy(request: web.Request, team_id, discussion_number, direction=None, per_page=None, page=None) -> web.Response:
    """List discussion comments (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List discussion comments](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-discussion-comments) endpoint.  List all comments on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_discussions_in_org(request: web.Request, org, team_slug, direction=None, per_page=None, page=None, pinned=None) -> web.Response:
    """List discussions

    List all discussions on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param pinned: Pinned discussions only filter
    :type pinned: str

    """
    return web.Response(status=200)


async def teams_list_discussions_legacy(request: web.Request, team_id, direction=None, per_page=None, page=None) -> web.Response:
    """List discussions (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List discussions&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-discussions) endpoint.  List all discussions on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_for_authenticated_user(request: web.Request, per_page=None, page=None) -> web.Response:
    """List teams for the authenticated user

    List all of the teams across all of the organizations to which the authenticated user belongs. This method requires &#x60;user&#x60;, &#x60;repo&#x60;, or &#x60;read:org&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/).

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_members_in_org(request: web.Request, org, team_slug, role=None, per_page=None, page=None) -> web.Response:
    """List team members

    Team members will include the members of child teams.  To list members in a team, the team must be visible to the authenticated user.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param role: Filters members returned by their role in the team. Can be one of:   \\* &#x60;member&#x60; - normal members of the team.   \\* &#x60;maintainer&#x60; - team maintainers.   \\* &#x60;all&#x60; - all members of the team.
    :type role: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_members_legacy(request: web.Request, team_id, role=None, per_page=None, page=None) -> web.Response:
    """List team members (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List team members&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-team-members) endpoint.  Team members will include the members of child teams.

    :param team_id: 
    :type team_id: int
    :param role: Filters members returned by their role in the team. Can be one of:   \\* &#x60;member&#x60; - normal members of the team.   \\* &#x60;maintainer&#x60; - team maintainers.   \\* &#x60;all&#x60; - all members of the team.
    :type role: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_projects_in_org(request: web.Request, org, team_slug, per_page=None, page=None) -> web.Response:
    """List team projects

    Lists the organization projects for a team.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/projects&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_projects_legacy(request: web.Request, team_id, per_page=None, page=None) -> web.Response:
    """List team projects (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List team projects&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-team-projects) endpoint.  Lists the organization projects for a team.

    :param team_id: 
    :type team_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_repos_in_org(request: web.Request, org, team_slug, per_page=None, page=None) -> web.Response:
    """List team repositories

    Lists a team&#39;s repositories visible to the authenticated user.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/repos&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_list_repos_legacy(request: web.Request, team_id, per_page=None, page=None) -> web.Response:
    """List team repositories (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-team-repositories) endpoint.

    :param team_id: 
    :type team_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def teams_remove_member_legacy(request: web.Request, team_id, username) -> web.Response:
    """Remove team member (Legacy)

    The \&quot;Remove team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Remove team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a team member, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;

    :param team_id: 
    :type team_id: int
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def teams_remove_membership_for_user_in_org(request: web.Request, org, team_slug, username) -> web.Response:
    """Remove team membership for a user

    Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a membership between a user and a team, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/memberships/{username}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def teams_remove_membership_for_user_legacy(request: web.Request, team_id, username) -> web.Response:
    """Remove team membership for a user (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-team-membership-for-a-user) endpoint.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a membership between a user and a team, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;

    :param team_id: 
    :type team_id: int
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def teams_remove_project_in_org(request: web.Request, org, team_slug, project_id) -> web.Response:
    """Remove a project from a team

    Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have &#x60;read&#x60; access to both the team and project, or &#x60;admin&#x60; access to the team or project. This endpoint removes the project from the team, but does not delete the project.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/projects/{project_id}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param project_id: 
    :type project_id: int

    """
    return web.Response(status=200)


async def teams_remove_project_legacy(request: web.Request, team_id, project_id) -> web.Response:
    """Remove a project from a team (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-a-project-from-a-team) endpoint.  Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have &#x60;read&#x60; access to both the team and project, or &#x60;admin&#x60; access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it.

    :param team_id: 
    :type team_id: int
    :param project_id: 
    :type project_id: int

    """
    return web.Response(status=200)


async def teams_remove_repo_in_org(request: web.Request, org, team_slug, owner, repo) -> web.Response:
    """Remove a repository from a team

    If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def teams_remove_repo_legacy(request: web.Request, team_id, owner, repo) -> web.Response:
    """Remove a repository from a team (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-a-repository-from-a-team) endpoint.  If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team.

    :param team_id: 
    :type team_id: int
    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def teams_update_discussion_comment_in_org(request: web.Request, org, team_slug, discussion_number, comment_number, body) -> web.Response:
    """Update a discussion comment

    Edits the body text of a discussion comment. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateDiscussionCommentInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_discussion_comment_legacy(request: web.Request, team_id, discussion_number, comment_number, body) -> web.Response:
    """Update a discussion comment (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#update-a-discussion-comment) endpoint.  Edits the body text of a discussion comment. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateDiscussionCommentInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_discussion_in_org(request: web.Request, org, team_slug, discussion_number, body=None) -> web.Response:
    """Update a discussion

    Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdateDiscussionInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_discussion_legacy(request: web.Request, team_id, discussion_number, body=None) -> web.Response:
    """Update a discussion (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#update-a-discussion) endpoint.  Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdateDiscussionInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_in_org(request: web.Request, org, team_slug, body=None) -> web.Response:
    """Update a team

    To edit a team, the authenticated user must either be an organization owner or a team maintainer.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PATCH /organizations/{org_id}/team/{team_id}&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdateInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_legacy(request: web.Request, team_id, body) -> web.Response:
    """Update a team (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#update-a-team) endpoint.  To edit a team, the authenticated user must either be an organization owner or a team maintainer.  **Note:** With nested teams, the &#x60;privacy&#x60; for parent teams cannot be &#x60;secret&#x60;.

    :param team_id: 
    :type team_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdateLegacyRequest.from_dict(body)
    return web.Response(status=200)
