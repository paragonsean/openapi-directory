from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.reaction import Reaction
from openapi_server.models.reactions_create_for_commit_comment_request import ReactionsCreateForCommitCommentRequest
from openapi_server.models.reactions_create_for_issue_comment_request import ReactionsCreateForIssueCommentRequest
from openapi_server.models.reactions_create_for_issue_request import ReactionsCreateForIssueRequest
from openapi_server.models.reactions_create_for_pull_request_review_comment_request import ReactionsCreateForPullRequestReviewCommentRequest
from openapi_server.models.reactions_create_for_team_discussion_comment_in_org_request import ReactionsCreateForTeamDiscussionCommentInOrgRequest
from openapi_server.models.reactions_create_for_team_discussion_in_org_request import ReactionsCreateForTeamDiscussionInOrgRequest
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def reactions_create_for_commit_comment(request: web.Request, owner, repo, comment_id, body) -> web.Response:
    """Create reaction for a commit comment

    Create a reaction to a [commit comment](https://docs.github.com/enterprise-server@2.21/rest/reference/repos#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this commit comment.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReactionsCreateForCommitCommentRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_create_for_issue(request: web.Request, owner, repo, issue_number, body) -> web.Response:
    """Create reaction for an issue

    Create a reaction to an [issue](https://docs.github.com/enterprise-server@2.21/rest/reference/issues/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReactionsCreateForIssueRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_create_for_issue_comment(request: web.Request, owner, repo, comment_id, body) -> web.Response:
    """Create reaction for an issue comment

    Create a reaction to an [issue comment](https://docs.github.com/enterprise-server@2.21/rest/reference/issues#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue comment.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReactionsCreateForIssueCommentRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_create_for_pull_request_review_comment(request: web.Request, owner, repo, comment_id, body) -> web.Response:
    """Create reaction for a pull request review comment

    Create a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@2.21/rest/reference/pulls#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this pull request review comment.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReactionsCreateForPullRequestReviewCommentRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_create_for_team_discussion_comment_in_org(request: web.Request, org, team_slug, discussion_number, comment_number, body) -> web.Response:
    """Create reaction for a team discussion comment

    Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion comment.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions&#x60;.

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
    body = ReactionsCreateForTeamDiscussionCommentInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_create_for_team_discussion_comment_legacy(request: web.Request, team_id, discussion_number, comment_number, body) -> web.Response:
    """Create reaction for a team discussion comment (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new \&quot;[Create reaction for a team discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#create-reaction-for-a-team-discussion-comment)\&quot; endpoint.  Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion comment.

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReactionsCreateForTeamDiscussionCommentInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_create_for_team_discussion_in_org(request: web.Request, org, team_slug, discussion_number, body) -> web.Response:
    """Create reaction for a team discussion

    Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReactionsCreateForTeamDiscussionInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_create_for_team_discussion_legacy(request: web.Request, team_id, discussion_number, body) -> web.Response:
    """Create reaction for a team discussion (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;Create reaction for a team discussion&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#create-reaction-for-a-team-discussion) endpoint.  Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion.

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReactionsCreateForTeamDiscussionInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def reactions_delete_for_commit_comment(request: web.Request, owner, repo, comment_id, reaction_id) -> web.Response:
    """Delete a commit comment reaction

    **Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id&#x60;.  Delete a reaction to a [commit comment](https://docs.github.com/enterprise-server@2.21/rest/reference/repos#comments).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param reaction_id: 
    :type reaction_id: int

    """
    return web.Response(status=200)


async def reactions_delete_for_issue(request: web.Request, owner, repo, issue_number, reaction_id) -> web.Response:
    """Delete an issue reaction

    **Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE /repositories/:repository_id/issues/:issue_number/reactions/:reaction_id&#x60;.  Delete a reaction to an [issue](https://docs.github.com/enterprise-server@2.21/rest/reference/issues/).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param reaction_id: 
    :type reaction_id: int

    """
    return web.Response(status=200)


async def reactions_delete_for_issue_comment(request: web.Request, owner, repo, comment_id, reaction_id) -> web.Response:
    """Delete an issue comment reaction

    **Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE delete /repositories/:repository_id/issues/comments/:comment_id/reactions/:reaction_id&#x60;.  Delete a reaction to an [issue comment](https://docs.github.com/enterprise-server@2.21/rest/reference/issues#comments).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param reaction_id: 
    :type reaction_id: int

    """
    return web.Response(status=200)


async def reactions_delete_for_pull_request_comment(request: web.Request, owner, repo, comment_id, reaction_id) -> web.Response:
    """Delete a pull request comment reaction

    **Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE /repositories/:repository_id/pulls/comments/:comment_id/reactions/:reaction_id.&#x60;  Delete a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@2.21/rest/reference/pulls#review-comments).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param reaction_id: 
    :type reaction_id: int

    """
    return web.Response(status=200)


async def reactions_delete_for_team_discussion(request: web.Request, org, team_slug, discussion_number, reaction_id) -> web.Response:
    """Delete team discussion reaction

    **Note:** You can also specify a team or organization with &#x60;team_id&#x60; and &#x60;org_id&#x60; using the route &#x60;DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions/:reaction_id&#x60;.  Delete a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param reaction_id: 
    :type reaction_id: int

    """
    return web.Response(status=200)


async def reactions_delete_for_team_discussion_comment(request: web.Request, org, team_slug, discussion_number, comment_number, reaction_id) -> web.Response:
    """Delete team discussion comment reaction

    **Note:** You can also specify a team or organization with &#x60;team_id&#x60; and &#x60;org_id&#x60; using the route &#x60;DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id&#x60;.  Delete a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int
    :param reaction_id: 
    :type reaction_id: int

    """
    return web.Response(status=200)


async def reactions_delete_legacy(request: web.Request, reaction_id) -> web.Response:
    """Delete a reaction (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Reactions API. We recommend migrating your existing code to use the new delete reactions endpoints. For more information, see this [blog post](https://developer.github.com/changes/2020-02-26-new-delete-reactions-endpoints/).  OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), when deleting a [team discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussions) or [team discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussion-comments).

    :param reaction_id: 
    :type reaction_id: int

    """
    return web.Response(status=200)


async def reactions_list_for_commit_comment(request: web.Request, owner, repo, comment_id, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for a commit comment

    List the reactions to a [commit comment](https://docs.github.com/enterprise-server@2.21/rest/reference/repos#comments).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a commit comment.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def reactions_list_for_issue(request: web.Request, owner, repo, issue_number, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for an issue

    List the reactions to an [issue](https://docs.github.com/enterprise-server@2.21/rest/reference/issues).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def reactions_list_for_issue_comment(request: web.Request, owner, repo, comment_id, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for an issue comment

    List the reactions to an [issue comment](https://docs.github.com/enterprise-server@2.21/rest/reference/issues#comments).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue comment.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def reactions_list_for_pull_request_review_comment(request: web.Request, owner, repo, comment_id, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for a pull request review comment

    List the reactions to a [pull request review comment](https://docs.github.com/enterprise-server@2.21/rest/reference/pulls#review-comments).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a pull request review comment.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def reactions_list_for_team_discussion_comment_in_org(request: web.Request, org, team_slug, discussion_number, comment_number, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for a team discussion comment

    List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussion-comments/). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def reactions_list_for_team_discussion_comment_legacy(request: web.Request, team_id, discussion_number, comment_number, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for a team discussion comment (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List reactions for a team discussion comment&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#list-reactions-for-a-team-discussion-comment) endpoint.  List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param comment_number: 
    :type comment_number: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def reactions_list_for_team_discussion_in_org(request: web.Request, org, team_slug, discussion_number, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for a team discussion

    List the reactions to a [team discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussions). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions&#x60;.

    :param org: 
    :type org: str
    :param team_slug: team_slug parameter
    :type team_slug: str
    :param discussion_number: 
    :type discussion_number: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def reactions_list_for_team_discussion_legacy(request: web.Request, team_id, discussion_number, content=None, per_page=None, page=None) -> web.Response:
    """List reactions for a team discussion (Legacy)

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List reactions for a team discussion&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#list-reactions-for-a-team-discussion) endpoint.  List the reactions to a [team discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#discussions). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param team_id: 
    :type team_id: int
    :param discussion_number: 
    :type discussion_number: int
    :param content: Returns a single [reaction type](https://docs.github.com/enterprise-server@2.21/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion.
    :type content: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)
