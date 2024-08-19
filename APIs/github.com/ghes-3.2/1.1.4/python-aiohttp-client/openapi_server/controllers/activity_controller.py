from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.activity_list_repos_starred_by_user200_response import ActivityListReposStarredByUser200Response
from openapi_server.models.activity_list_stargazers_for_repo200_response import ActivityListStargazersForRepo200Response
from openapi_server.models.activity_mark_notifications_as_read202_response import ActivityMarkNotificationsAsRead202Response
from openapi_server.models.activity_mark_notifications_as_read_request import ActivityMarkNotificationsAsReadRequest
from openapi_server.models.activity_mark_repo_notifications_as_read_request import ActivityMarkRepoNotificationsAsReadRequest
from openapi_server.models.activity_set_repo_subscription_request import ActivitySetRepoSubscriptionRequest
from openapi_server.models.activity_set_thread_subscription_request import ActivitySetThreadSubscriptionRequest
from openapi_server.models.basic_error import BasicError
from openapi_server.models.enterprise_admin_update_org_name202_response import EnterpriseAdminUpdateOrgName202Response
from openapi_server.models.event import Event
from openapi_server.models.feed import Feed
from openapi_server.models.minimal_repository import MinimalRepository
from openapi_server.models.repository import Repository
from openapi_server.models.repository_subscription import RepositorySubscription
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.starred_repository import StarredRepository
from openapi_server.models.thread import Thread
from openapi_server.models.thread_subscription import ThreadSubscription
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def activity_check_repo_is_starred_by_authenticated_user(request: web.Request, owner, repo) -> web.Response:
    """Check if a repository is starred by the authenticated user

    

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str

    """
    return web.Response(status=200)


async def activity_delete_repo_subscription(request: web.Request, owner, repo) -> web.Response:
    """Delete a repository subscription

    This endpoint should only be used to stop watching a repository. To control whether or not you wish to receive notifications from a repository, [set the repository&#39;s subscription manually](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#set-a-repository-subscription).

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str

    """
    return web.Response(status=200)


async def activity_delete_thread_subscription(request: web.Request, thread_id) -> web.Response:
    """Delete a thread subscription

    Mutes all future notifications for a conversation until you comment on the thread or get an **@mention**. If you are watching the repository of the thread, you will still receive notifications. To ignore future notifications for a repository you are watching, use the [Set a thread subscription](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#set-a-thread-subscription) endpoint and set &#x60;ignore&#x60; to &#x60;true&#x60;.

    :param thread_id: The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#list-notifications-for-the-authenticated-user)).
    :type thread_id: int

    """
    return web.Response(status=200)


async def activity_get_feeds(request: web.Request, ) -> web.Response:
    """Get feeds

    GitHub Enterprise Server provides several timeline resources in [Atom](http://en.wikipedia.org/wiki/Atom_(standard)) format. The Feeds API lists all the feeds available to the authenticated user:  *   **Timeline**: The GitHub Enterprise Server global public timeline *   **User**: The public timeline for any user, using [URI template](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#hypermedia) *   **Current user public**: The public timeline for the authenticated user *   **Current user**: The private timeline for the authenticated user *   **Current user actor**: The private timeline for activity created by the authenticated user *   **Current user organizations**: The private timeline for the organizations the authenticated user is a member of. *   **Security advisories**: A collection of public announcements that provide information about security-related vulnerabilities in software on GitHub Enterprise Server.  **Note**: Private feeds are only returned when [authenticating via Basic Auth](https://docs.github.com/enterprise-server@3.2/rest/overview/other-authentication-methods#basic-authentication) since current feed URIs use the older, non revocable auth tokens.


    """
    return web.Response(status=200)


async def activity_get_repo_subscription(request: web.Request, owner, repo) -> web.Response:
    """Get a repository subscription

    

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str

    """
    return web.Response(status=200)


async def activity_get_thread(request: web.Request, thread_id) -> web.Response:
    """Get a thread

    Gets information about a notification thread.

    :param thread_id: The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#list-notifications-for-the-authenticated-user)).
    :type thread_id: int

    """
    return web.Response(status=200)


async def activity_get_thread_subscription_for_authenticated_user(request: web.Request, thread_id) -> web.Response:
    """Get a thread subscription for the authenticated user

    This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#get-a-repository-subscription).  Note that subscriptions are only generated if a user is participating in a conversation--for example, they&#39;ve replied to the thread, were **@mentioned**, or manually subscribe to a thread.

    :param thread_id: The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#list-notifications-for-the-authenticated-user)).
    :type thread_id: int

    """
    return web.Response(status=200)


async def activity_list_events_for_authenticated_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List events for the authenticated user

    If you are authenticated as the given user, you will see your private events. Otherwise, you&#39;ll only see public events.

    :param username: The handle for the GitHub user account.
    :type username: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_notifications_for_authenticated_user(request: web.Request, all=None, participating=None, since=None, before=None, page=None, per_page=None) -> web.Response:
    """List notifications for the authenticated user

    List all notifications for the current user, sorted by most recently updated.

    :param all: If &#x60;true&#x60;, show notifications marked as read.
    :type all: bool
    :param participating: If &#x60;true&#x60;, only shows notifications in which the user is directly participating or mentioned.
    :type participating: bool
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param before: Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type before: str
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: The number of results per page (max 50).
    :type per_page: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def activity_list_org_events_for_authenticated_user(request: web.Request, username, org, per_page=None, page=None) -> web.Response:
    """List organization events for the authenticated user

    This is the user&#39;s organization dashboard. You must be authenticated as the user to view this.

    :param username: The handle for the GitHub user account.
    :type username: str
    :param org: The organization name. The name is not case sensitive.
    :type org: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_public_events(request: web.Request, per_page=None, page=None) -> web.Response:
    """List public events

    We delay the public events feed by five minutes, which means the most recent event returned by the public events API actually occurred at least five minutes ago.

    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_public_events_for_repo_network(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List public events for a network of repositories

    

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_public_events_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List public events for a user

    

    :param username: The handle for the GitHub user account.
    :type username: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_public_org_events(request: web.Request, org, per_page=None, page=None) -> web.Response:
    """List public organization events

    

    :param org: The organization name. The name is not case sensitive.
    :type org: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_received_events_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List events received by the authenticated user

    These are events that you&#39;ve received by watching repos and following users. If you are authenticated as the given user, you will see private events. Otherwise, you&#39;ll only see public events.

    :param username: The handle for the GitHub user account.
    :type username: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_received_public_events_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List public events received by a user

    

    :param username: The handle for the GitHub user account.
    :type username: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_repo_events(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List repository events

    

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_repo_notifications_for_authenticated_user(request: web.Request, owner, repo, all=None, participating=None, since=None, before=None, per_page=None, page=None) -> web.Response:
    """List repository notifications for the authenticated user

    Lists all notifications for the current user in the specified repository.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param all: If &#x60;true&#x60;, show notifications marked as read.
    :type all: bool
    :param participating: If &#x60;true&#x60;, only shows notifications in which the user is directly participating or mentioned.
    :type participating: bool
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param before: Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type before: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def activity_list_repos_starred_by_authenticated_user(request: web.Request, sort=None, direction=None, per_page=None, page=None) -> web.Response:
    """List repositories starred by the authenticated user

    Lists repositories the authenticated user has starred.  You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@3.2/rest/overview/media-types/) via the &#x60;Accept&#x60; header: &#x60;application/vnd.github.star+json&#x60;.

    :param sort: The property to sort the results by. &#x60;created&#x60; means when the repository was starred. &#x60;updated&#x60; means when the repository was last pushed to.
    :type sort: str
    :param direction: The direction to sort the results by.
    :type direction: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_repos_starred_by_user(request: web.Request, username, sort=None, direction=None, per_page=None, page=None) -> web.Response:
    """List repositories starred by a user

    Lists repositories a user has starred.  You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@3.2/rest/overview/media-types/) via the &#x60;Accept&#x60; header: &#x60;application/vnd.github.star+json&#x60;.

    :param username: The handle for the GitHub user account.
    :type username: str
    :param sort: The property to sort the results by. &#x60;created&#x60; means when the repository was starred. &#x60;updated&#x60; means when the repository was last pushed to.
    :type sort: str
    :param direction: The direction to sort the results by.
    :type direction: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_repos_watched_by_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List repositories watched by a user

    Lists repositories a user is watching.

    :param username: The handle for the GitHub user account.
    :type username: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_stargazers_for_repo(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List stargazers

    Lists the people that have starred the repository.  You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@3.2/rest/overview/media-types/) via the &#x60;Accept&#x60; header: &#x60;application/vnd.github.star+json&#x60;.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_watched_repos_for_authenticated_user(request: web.Request, per_page=None, page=None) -> web.Response:
    """List repositories watched by the authenticated user

    Lists repositories the authenticated user is watching.

    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_list_watchers_for_repo(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List watchers

    Lists the people watching the specified repository.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def activity_mark_notifications_as_read(request: web.Request, body=None) -> web.Response:
    """Mark notifications as read

    Marks all notifications as \&quot;read\&quot; for the current user. If the number of notifications is too large to complete in one request, you will receive a &#x60;202 Accepted&#x60; status and GitHub Enterprise Server will run an asynchronous process to mark notifications as \&quot;read.\&quot; To check whether any \&quot;unread\&quot; notifications remain, you can use the [List notifications for the authenticated user](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter &#x60;all&#x3D;false&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = ActivityMarkNotificationsAsReadRequest.from_dict(body)
    return web.Response(status=200)


async def activity_mark_repo_notifications_as_read(request: web.Request, owner, repo, body=None) -> web.Response:
    """Mark repository notifications as read

    Marks all notifications in a repository as \&quot;read\&quot; for the current user. If the number of notifications is too large to complete in one request, you will receive a &#x60;202 Accepted&#x60; status and GitHub Enterprise Server will run an asynchronous process to mark notifications as \&quot;read.\&quot; To check whether any \&quot;unread\&quot; notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter &#x60;all&#x3D;false&#x60;.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActivityMarkRepoNotificationsAsReadRequest.from_dict(body)
    return web.Response(status=200)


async def activity_mark_thread_as_read(request: web.Request, thread_id) -> web.Response:
    """Mark a thread as read

    Marks a thread as \&quot;read.\&quot; Marking a thread as \&quot;read\&quot; is equivalent to clicking a notification in your notification inbox on GitHub Enterprise Server: https://github.com/notifications.

    :param thread_id: The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#list-notifications-for-the-authenticated-user)).
    :type thread_id: int

    """
    return web.Response(status=200)


async def activity_set_repo_subscription(request: web.Request, owner, repo, body=None) -> web.Response:
    """Set a repository subscription

    If you would like to watch a repository, set &#x60;subscribed&#x60; to &#x60;true&#x60;. If you would like to ignore notifications made within a repository, set &#x60;ignored&#x60; to &#x60;true&#x60;. If you would like to stop watching a repository, [delete the repository&#39;s subscription](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#delete-a-repository-subscription) completely.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActivitySetRepoSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def activity_set_thread_subscription(request: web.Request, thread_id, body=None) -> web.Response:
    """Set a thread subscription

    If you are watching a repository, you receive notifications for all threads by default. Use this endpoint to ignore future notifications for threads until you comment on the thread or get an **@mention**.  You can also use this endpoint to subscribe to threads that you are currently not receiving notifications for or to subscribed to threads that you have previously ignored.  Unsubscribing from a conversation in a repository that you are not watching is functionally equivalent to the [Delete a thread subscription](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#delete-a-thread-subscription) endpoint.

    :param thread_id: The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/enterprise-server@3.2/rest/reference/activity#list-notifications-for-the-authenticated-user)).
    :type thread_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ActivitySetThreadSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def activity_star_repo_for_authenticated_user(request: web.Request, owner, repo) -> web.Response:
    """Star a repository for the authenticated user

    Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str

    """
    return web.Response(status=200)


async def activity_unstar_repo_for_authenticated_user(request: web.Request, owner, repo) -> web.Response:
    """Unstar a repository for the authenticated user

    

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str

    """
    return web.Response(status=200)
