from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.issue import Issue
from openapi_server.models.issue_comment import IssueComment
from openapi_server.models.issue_event import IssueEvent
from openapi_server.models.issue_event_for_issue import IssueEventForIssue
from openapi_server.models.issue_simple import IssueSimple
from openapi_server.models.issues_add_assignees_request import IssuesAddAssigneesRequest
from openapi_server.models.issues_create_label_request import IssuesCreateLabelRequest
from openapi_server.models.issues_create_milestone_request import IssuesCreateMilestoneRequest
from openapi_server.models.issues_create_request import IssuesCreateRequest
from openapi_server.models.issues_lock_request import IssuesLockRequest
from openapi_server.models.issues_remove_assignees_request import IssuesRemoveAssigneesRequest
from openapi_server.models.issues_set_labels_request import IssuesSetLabelsRequest
from openapi_server.models.issues_update_comment_request import IssuesUpdateCommentRequest
from openapi_server.models.issues_update_label_request import IssuesUpdateLabelRequest
from openapi_server.models.issues_update_milestone_request import IssuesUpdateMilestoneRequest
from openapi_server.models.issues_update_request import IssuesUpdateRequest
from openapi_server.models.label import Label
from openapi_server.models.milestone import Milestone
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.timeline_issue_events import TimelineIssueEvents
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def issues_add_assignees(request: web.Request, owner, repo, issue_number, body=None) -> web.Response:
    """Add assignees to an issue

    Adds up to 10 assignees to an issue. Users already assigned to an issue are not replaced.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesAddAssigneesRequest.from_dict(body)
    return web.Response(status=200)


async def issues_add_labels(request: web.Request, owner, repo, issue_number, body=None) -> web.Response:
    """Add labels to an issue

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesSetLabelsRequest.from_dict(body)
    return web.Response(status=200)


async def issues_check_user_can_be_assigned(request: web.Request, owner, repo, assignee) -> web.Response:
    """Check if a user can be assigned

    Checks if a user has permission to be assigned to an issue in this repository.  If the &#x60;assignee&#x60; can be assigned to issues in the repository, a &#x60;204&#x60; header with no content is returned.  Otherwise a &#x60;404&#x60; status code is returned.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param assignee: 
    :type assignee: str

    """
    return web.Response(status=200)


async def issues_create(request: web.Request, owner, repo, body) -> web.Response:
    """Create an issue

    Any user with pull access to a repository can create an issue. If [issues are disabled in the repository](https://help.github.com/articles/disabling-issues/), the API returns a &#x60;410 Gone&#x60; status.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesCreateRequest.from_dict(body)
    return web.Response(status=200)


async def issues_create_comment(request: web.Request, owner, repo, issue_number, body) -> web.Response:
    """Create an issue comment

    This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesUpdateCommentRequest.from_dict(body)
    return web.Response(status=200)


async def issues_create_label(request: web.Request, owner, repo, body) -> web.Response:
    """Create a label

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesCreateLabelRequest.from_dict(body)
    return web.Response(status=200)


async def issues_create_milestone(request: web.Request, owner, repo, body) -> web.Response:
    """Create a milestone

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesCreateMilestoneRequest.from_dict(body)
    return web.Response(status=200)


async def issues_delete_comment(request: web.Request, owner, repo, comment_id) -> web.Response:
    """Delete an issue comment

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def issues_delete_label(request: web.Request, owner, repo, name) -> web.Response:
    """Delete a label

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def issues_delete_milestone(request: web.Request, owner, repo, milestone_number) -> web.Response:
    """Delete a milestone

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param milestone_number: milestone_number parameter
    :type milestone_number: int

    """
    return web.Response(status=200)


async def issues_get(request: web.Request, owner, repo, issue_number) -> web.Response:
    """Get an issue

    The API returns a [&#x60;301 Moved Permanently&#x60; status](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#http-redirects-redirects) if the issue was [transferred](https://help.github.com/articles/transferring-an-issue-to-another-repository/) to another repository. If the issue was transferred to or deleted from a repository where the authenticated user lacks read access, the API returns a &#x60;404 Not Found&#x60; status. If the issue was deleted from a repository where the authenticated user has read access, the API returns a &#x60;410 Gone&#x60; status. To receive webhook events for transferred and deleted issues, subscribe to the [&#x60;issues&#x60;](https://docs.github.com/enterprise-server@2.20/webhooks/event-payloads/#issues) webhook.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int

    """
    return web.Response(status=200)


async def issues_get_comment(request: web.Request, owner, repo, comment_id) -> web.Response:
    """Get an issue comment

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def issues_get_event(request: web.Request, owner, repo, event_id) -> web.Response:
    """Get an issue event

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param event_id: 
    :type event_id: int

    """
    return web.Response(status=200)


async def issues_get_label(request: web.Request, owner, repo, name) -> web.Response:
    """Get a label

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def issues_get_milestone(request: web.Request, owner, repo, milestone_number) -> web.Response:
    """Get a milestone

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param milestone_number: milestone_number parameter
    :type milestone_number: int

    """
    return web.Response(status=200)


async def issues_list(request: web.Request, filter=None, state=None, labels=None, sort=None, direction=None, since=None, collab=None, orgs=None, owned=None, pulls=None, per_page=None, page=None) -> web.Response:
    """List issues assigned to the authenticated user

    List issues assigned to the authenticated user across all visible repositories including owned repositories, member repositories, and organization repositories. You can use the &#x60;filter&#x60; query parameter to fetch issues that are not necessarily assigned to you.   **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

    :param filter: Indicates which sorts of issues to return. Can be one of:   \\* &#x60;assigned&#x60;: Issues assigned to you   \\* &#x60;created&#x60;: Issues created by you   \\* &#x60;mentioned&#x60;: Issues mentioning you   \\* &#x60;subscribed&#x60;: Issues you&#39;re subscribed to updates for   \\* &#x60;all&#x60; or &#x60;repos&#x60;: All issues the authenticated user can see, regardless of participation or creation
    :type filter: str
    :param state: Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;.
    :type state: str
    :param labels: A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60;
    :type labels: str
    :param sort: What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;.
    :type sort: str
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param collab: 
    :type collab: bool
    :param orgs: 
    :type orgs: bool
    :param owned: 
    :type owned: bool
    :param pulls: 
    :type pulls: bool
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def issues_list_assignees(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List assignees

    Lists the [available assignees](https://help.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_list_comments(request: web.Request, owner, repo, issue_number, since=None, per_page=None, page=None) -> web.Response:
    """List issue comments

    Issue Comments are ordered by ascending ID.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def issues_list_comments_for_repo(request: web.Request, owner, repo, sort=None, direction=None, since=None, per_page=None, page=None) -> web.Response:
    """List issue comments for a repository

    By default, Issue Comments are ordered by ascending ID.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param sort: One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to).
    :type sort: str
    :param direction: Either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without the &#x60;sort&#x60; parameter.
    :type direction: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def issues_list_events(request: web.Request, owner, repo, issue_number, per_page=None, page=None) -> web.Response:
    """List issue events

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_list_events_for_repo(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List issue events for a repository

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_list_events_for_timeline(request: web.Request, owner, repo, issue_number, per_page=None, page=None) -> web.Response:
    """List timeline events for an issue

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_list_for_authenticated_user(request: web.Request, filter=None, state=None, labels=None, sort=None, direction=None, since=None, per_page=None, page=None) -> web.Response:
    """List user account issues assigned to the authenticated user

    List issues across owned and member repositories assigned to the authenticated user.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

    :param filter: Indicates which sorts of issues to return. Can be one of:   \\* &#x60;assigned&#x60;: Issues assigned to you   \\* &#x60;created&#x60;: Issues created by you   \\* &#x60;mentioned&#x60;: Issues mentioning you   \\* &#x60;subscribed&#x60;: Issues you&#39;re subscribed to updates for   \\* &#x60;all&#x60; or &#x60;repos&#x60;: All issues the authenticated user can see, regardless of participation or creation
    :type filter: str
    :param state: Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;.
    :type state: str
    :param labels: A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60;
    :type labels: str
    :param sort: What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;.
    :type sort: str
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def issues_list_for_org(request: web.Request, org, filter=None, state=None, labels=None, sort=None, direction=None, since=None, per_page=None, page=None) -> web.Response:
    """List organization issues assigned to the authenticated user

    List issues in an organization assigned to the authenticated user.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

    :param org: 
    :type org: str
    :param filter: Indicates which sorts of issues to return. Can be one of:   \\* &#x60;assigned&#x60;: Issues assigned to you   \\* &#x60;created&#x60;: Issues created by you   \\* &#x60;mentioned&#x60;: Issues mentioning you   \\* &#x60;subscribed&#x60;: Issues you&#39;re subscribed to updates for   \\* &#x60;all&#x60; or &#x60;repos&#x60;: All issues the authenticated user can see, regardless of participation or creation
    :type filter: str
    :param state: Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;.
    :type state: str
    :param labels: A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60;
    :type labels: str
    :param sort: What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;.
    :type sort: str
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def issues_list_for_repo(request: web.Request, owner, repo, milestone=None, state=None, assignee=None, creator=None, mentioned=None, labels=None, sort=None, direction=None, since=None, per_page=None, page=None) -> web.Response:
    """List repository issues

    List issues in a repository.  **Note**: GitHub&#39;s REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@2.20/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param milestone: If an &#x60;integer&#x60; is passed, it should refer to a milestone by its &#x60;number&#x60; field. If the string &#x60;*&#x60; is passed, issues with any milestone are accepted. If the string &#x60;none&#x60; is passed, issues without milestones are returned.
    :type milestone: str
    :param state: Indicates the state of the issues to return. Can be either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;.
    :type state: str
    :param assignee: Can be the name of a user. Pass in &#x60;none&#x60; for issues with no assigned user, and &#x60;*&#x60; for issues assigned to any user.
    :type assignee: str
    :param creator: The user that created the issue.
    :type creator: str
    :param mentioned: A user that&#39;s mentioned in the issue.
    :type mentioned: str
    :param labels: A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60;
    :type labels: str
    :param sort: What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;comments&#x60;.
    :type sort: str
    :param direction: One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending).
    :type direction: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def issues_list_labels_for_milestone(request: web.Request, owner, repo, milestone_number, per_page=None, page=None) -> web.Response:
    """List labels for issues in a milestone

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param milestone_number: milestone_number parameter
    :type milestone_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_list_labels_for_repo(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List labels for a repository

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_list_labels_on_issue(request: web.Request, owner, repo, issue_number, per_page=None, page=None) -> web.Response:
    """List labels for an issue

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_list_milestones(request: web.Request, owner, repo, state=None, sort=None, direction=None, per_page=None, page=None) -> web.Response:
    """List milestones

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param state: The state of the milestone. Either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;.
    :type state: str
    :param sort: What to sort results by. Either &#x60;due_on&#x60; or &#x60;completeness&#x60;.
    :type sort: str
    :param direction: The direction of the sort. Either &#x60;asc&#x60; or &#x60;desc&#x60;.
    :type direction: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def issues_lock(request: web.Request, owner, repo, issue_number, body=None) -> web.Response:
    """Lock an issue

    Users with push access can lock an issue or pull request&#39;s conversation.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesLockRequest.from_dict(body)
    return web.Response(status=200)


async def issues_remove_all_labels(request: web.Request, owner, repo, issue_number) -> web.Response:
    """Remove all labels from an issue

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int

    """
    return web.Response(status=200)


async def issues_remove_assignees(request: web.Request, owner, repo, issue_number, body=None) -> web.Response:
    """Remove assignees from an issue

    Removes one or more assignees from an issue.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesRemoveAssigneesRequest.from_dict(body)
    return web.Response(status=200)


async def issues_remove_label(request: web.Request, owner, repo, issue_number, name) -> web.Response:
    """Remove a label from an issue

    Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a &#x60;404 Not Found&#x60; status if the label does not exist.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def issues_set_labels(request: web.Request, owner, repo, issue_number, body=None) -> web.Response:
    """Set labels for an issue

    Removes any previous labels and sets the new labels for an issue.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesSetLabelsRequest.from_dict(body)
    return web.Response(status=200)


async def issues_unlock(request: web.Request, owner, repo, issue_number) -> web.Response:
    """Unlock an issue

    Users with push access can unlock an issue&#39;s conversation.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int

    """
    return web.Response(status=200)


async def issues_update(request: web.Request, owner, repo, issue_number, body=None) -> web.Response:
    """Update an issue

    Issue owners and users with push access can edit an issue.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param issue_number: issue_number parameter
    :type issue_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def issues_update_comment(request: web.Request, owner, repo, comment_id, body) -> web.Response:
    """Update an issue comment

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesUpdateCommentRequest.from_dict(body)
    return web.Response(status=200)


async def issues_update_label(request: web.Request, owner, repo, name, body=None) -> web.Response:
    """Update a label

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param name: 
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesUpdateLabelRequest.from_dict(body)
    return web.Response(status=200)


async def issues_update_milestone(request: web.Request, owner, repo, milestone_number, body=None) -> web.Response:
    """Update a milestone

    

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param milestone_number: milestone_number parameter
    :type milestone_number: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssuesUpdateMilestoneRequest.from_dict(body)
    return web.Response(status=200)
