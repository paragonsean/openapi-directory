from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.activity import Activity
from openapi_server.models.admin_account import AdminAccount
from openapi_server.models.admin_report import AdminReport
from openapi_server.models.announcement import Announcement
from openapi_server.models.api_v1_admin_accounts_id_action_post_request import ApiV1AdminAccountsIdActionPostRequest
from openapi_server.models.api_v1_domain_blocks_post_request import ApiV1DomainBlocksPostRequest
from openapi_server.models.api_v1_featured_tags_post_request import ApiV1FeaturedTagsPostRequest
from openapi_server.models.api_v1_filters_post_request import ApiV1FiltersPostRequest
from openapi_server.models.api_v1_lists_id_accounts_post_request import ApiV1ListsIdAccountsPostRequest
from openapi_server.models.api_v1_lists_post_request import ApiV1ListsPostRequest
from openapi_server.models.api_v1_lists_put_request import ApiV1ListsPutRequest
from openapi_server.models.api_v1_media_post_request import ApiV1MediaPostRequest
from openapi_server.models.api_v1_polls_id_post_request import ApiV1PollsIdPostRequest
from openapi_server.models.api_v1_push_subscription_post_request import ApiV1PushSubscriptionPostRequest
from openapi_server.models.api_v1_push_subscription_put_request import ApiV1PushSubscriptionPutRequest
from openapi_server.models.api_v1_reports_post_request import ApiV1ReportsPostRequest
from openapi_server.models.api_v1_scheduled_statuses_id_put_request import ApiV1ScheduledStatusesIdPutRequest
from openapi_server.models.api_v1_statuses_id_reblog_post_request import ApiV1StatusesIdReblogPostRequest
from openapi_server.models.api_v1_statuses_post200_response import ApiV1StatusesPost200Response
from openapi_server.models.api_v1_statuses_post_request_inner import ApiV1StatusesPostRequestInner
from openapi_server.models.api_v2_search_get200_response import ApiV2SearchGet200Response
from openapi_server.models.attachment import Attachment
from openapi_server.models.card import Card
from openapi_server.models.context import Context
from openapi_server.models.conversation import Conversation
from openapi_server.models.emoji import Emoji
from openapi_server.models.error import Error
from openapi_server.models.featured_tag import FeaturedTag
from openapi_server.models.filter import Filter
from openapi_server.models.identity_proof import IdentityProof
from openapi_server.models.instance import Instance
from openapi_server.models.notification import Notification
from openapi_server.models.poll import Poll
from openapi_server.models.preferences import Preferences
from openapi_server.models.push_subscription import PushSubscription
from openapi_server.models.relationship import Relationship
from openapi_server.models.report import Report
from openapi_server.models.scheduled_status import ScheduledStatus
from openapi_server.models.status import Status
from openapi_server.models.tag import Tag
from openapi_server import util


async def api_oembed_get(request: web.Request, url=None, maxwidth=None, maxheight=None) -> web.Response:
    """api_oembed_get

    OEmbed as JSON

    :param url: URL of a status
    :type url: str
    :param maxwidth: width of the iframe. Defaults to 400
    :type maxwidth: int
    :param maxheight: height of the iframe. Defaults to null
    :type maxheight: int

    """
    return web.Response(status=200)


async def api_proofs_get(request: web.Request, provider=None, username=None) -> web.Response:
    """api_proofs_get

    View identity proof

    :param provider: The identity provider to be looked up. Currently only supports keybase (case-sensitive)
    :type provider: str
    :param username: The username on the selected identity provider
    :type username: str

    """
    return web.Response(status=200)


async def api_v1_admin_accounts_get(request: web.Request, local=None, remote=None, by_domain=None, active=None, pending=None, disabled=None, silenced=None, suspended=None, staff=None, username=None, display_name=None, email=None, ip=None) -> web.Response:
    """api_v1_admin_accounts_get

    View accounts matching certain criteria for filtering, up to 100 at a time. Pagination may be done with the HTTP Link header in the response.

    :param local: Filter for local accounts?
    :type local: bool
    :param remote: Filter for remote accounts?
    :type remote: bool
    :param by_domain: Filter by the given domain
    :type by_domain: str
    :param active: Filter for currently active accounts?
    :type active: bool
    :param pending: Filter for currently pending accounts?
    :type pending: bool
    :param disabled: Filter for currently disabled accounts?
    :type disabled: bool
    :param silenced: Filter for currently silenced accounts?
    :type silenced: bool
    :param suspended: Filter for currently suspended accounts?
    :type suspended: bool
    :param staff: Filter for staff accounts?
    :type staff: bool
    :param username: Username to search for
    :type username: str
    :param display_name: Display name to search for
    :type display_name: str
    :param email: Lookup a user with this email
    :type email: str
    :param ip: Lookup a user with this IP
    :type ip: str

    """
    return web.Response(status=200)


async def api_v1_admin_accounts_id_action_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_admin_accounts_id_action_post

    Perform an action against an account and log this action in the moderation history.

    :param id: ID of the account
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AdminAccountsIdActionPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_admin_accounts_id_approve_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_accounts_id_approve_post

    Approve the given local account if it is currently pending approval.

    :param id: ID of the account
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_accounts_id_enable_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_accounts_id_enable_post

    Re-enable a local account whose login is currently disabled.

    :param id: ID of the account
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_accounts_id_get(request: web.Request, id) -> web.Response:
    """api_v1_admin_accounts_id_get

    View admin-level information about the given account.

    :param id: ID of the account
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_accounts_id_reject_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_accounts_id_reject_post

    Reject the given local account if it is currently pending approval.

    :param id: ID of the account
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_accounts_id_unsilence_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_accounts_id_unsilence_post

    Unsilence a currently silenced account.

    :param id: ID of the account
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_accounts_id_unsuspend_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_accounts_id_unsuspend_post

    Unsuspend a currently suspended account.

    :param id: ID of the account
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_reports_get(request: web.Request, resolved=None, account_id=None, target_account_id=None) -> web.Response:
    """api_v1_admin_reports_get

    View all reports. Pagination may be done with HTTP Link header in the response.

    :param resolved: 
    :type resolved: bool
    :param account_id: 
    :type account_id: str
    :param target_account_id: 
    :type target_account_id: str

    """
    return web.Response(status=200)


async def api_v1_admin_reports_id_assign_to_self_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_reports_id_assign_to_self_post

    Claim the handling of this report to yourself.

    :param id: ID of the report
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_reports_id_get(request: web.Request, id) -> web.Response:
    """api_v1_admin_reports_id_get

    View information about the report with the given ID.

    :param id: ID of the report
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_reports_id_reopen_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_reports_id_reopen_post

    Mark a report as resolved with no further action taken.

    :param id: ID of the report
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_reports_id_resolve_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_reports_id_resolve_post

    Mark a report as resolved with no further action taken.

    :param id: ID of the report
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_admin_reports_id_unassign_post(request: web.Request, id) -> web.Response:
    """api_v1_admin_reports_id_unassign_post

    Unassign a report so that someone else can claim it.

    :param id: ID of the report
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_announcements_get(request: web.Request, with_dismissed=None) -> web.Response:
    """api_v1_announcements_get

    See all currently active announcements set by admins.

    :param with_dismissed: If true, response will include announcements dismissed by the user. Defaults to false.
    :type with_dismissed: bool

    """
    return web.Response(status=200)


async def api_v1_announcements_id_dismiss_post(request: web.Request, id) -> web.Response:
    """api_v1_announcements_id_dismiss_post

    Allows a user to mark the announcement as read.

    :param id: Local ID of an announcement in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_announcements_id_reactions_name_delete(request: web.Request, id, name) -> web.Response:
    """api_v1_announcements_id_reactions_name_delete

    Undo a react emoji to an announcement.

    :param id: Local ID of an announcement in the database.
    :type id: str
    :param name: Unicode emoji, or shortcode of custom emoji
    :type name: str

    """
    return web.Response(status=200)


async def api_v1_announcements_id_reactions_name_put(request: web.Request, id, name) -> web.Response:
    """api_v1_announcements_id_reactions_name_put

    Allows a user to mark the announcement as read.

    :param id: Local ID of an announcement in the database.
    :type id: str
    :param name: Unicode emoji, or shortcode of custom emoji
    :type name: str

    """
    return web.Response(status=200)


async def api_v1_blocks_get(request: web.Request, limit=None, max_id=None, since_id=None) -> web.Response:
    """api_v1_blocks_get

    Get blocked users.

    :param limit: 
    :type limit: int
    :param max_id: 
    :type max_id: str
    :param since_id: 
    :type since_id: str

    """
    return web.Response(status=200)


async def api_v1_bookmarks_get(request: web.Request, limit=None, max_id=None, since_id=None, min_id=None) -> web.Response:
    """api_v1_bookmarks_get

    Statuses the user has bookmarked.

    :param limit: 
    :type limit: int
    :param max_id: 
    :type max_id: str
    :param since_id: 
    :type since_id: str
    :param min_id: 
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_conversations_get(request: web.Request, limit=None, max_id=None, since_id=None, min_id=None) -> web.Response:
    """api_v1_conversations_get

    Show conversation.

    :param limit: Max number of results to return. Defaults to 20.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str
    :param min_id: Return results immediately newer than ID
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_conversations_id_delete(request: web.Request, id) -> web.Response:
    """api_v1_conversations_id_delete

    Remove converstation

    :param id: ID of the conversation in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_conversations_id_read_post(request: web.Request, id) -> web.Response:
    """api_v1_conversations_id_read_post

    Remove converstation

    :param id: ID of the conversation in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_custom_emojis_get(request: web.Request, ) -> web.Response:
    """api_v1_custom_emojis_get

    Returns custom emojis that are available on the server.


    """
    return web.Response(status=200)


async def api_v1_directory_get(request: web.Request, limit=None, offset=None, order=None, local=None) -> web.Response:
    """api_v1_directory_get

    List accounts visible in the directory.

    :param limit: How many accounts to load. Default 40.
    :type limit: int
    :param offset: How many accounts to skip before returning results. Default 0.
    :type offset: int
    :param order: the &#x60;active&#x60; to sort by most recently posted statuses (default) or &#x60;new&#x60; to sort by most recently created profiles.
    :type order: str
    :param local: Only return local accounts.
    :type local: bool

    """
    return web.Response(status=200)


async def api_v1_domain_blocks_delete(request: web.Request, domain) -> web.Response:
    """api_v1_domain_blocks_delete

    Remove a domain block, if it exists in the user&#39;s array of blocked domains.

    :param domain: Domain to unblock.
    :type domain: str

    """
    return web.Response(status=200)


async def api_v1_domain_blocks_get(request: web.Request, limit=None, max_id=None, since_id=None) -> web.Response:
    """api_v1_domain_blocks_get

    View domains the user has blocked.

    :param limit: 
    :type limit: int
    :param max_id: 
    :type max_id: str
    :param since_id: 
    :type since_id: str

    """
    return web.Response(status=200)


async def api_v1_domain_blocks_post(request: web.Request, body=None) -> web.Response:
    """api_v1_domain_blocks_post

    \&quot;Block a domain to: - hide all public posts from it - hide all notifications from it - remove all followers from it - prevent following new users from it (but does not remove existing follows)\&quot; 

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1DomainBlocksPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_endorsements_get(request: web.Request, limit=None, max_id=None, since_id=None) -> web.Response:
    """api_v1_endorsements_get

    Accounts that the user is currently featuring on their profile.

    :param limit: Maximum number of results to return. Defaults to 40. Paginate using the HTTP Link header.
    :type limit: int
    :param max_id: Internal parameter. Use HTTP Link header from response for pagination
    :type max_id: str
    :param since_id: Internal parameter. Use HTTP Link header from response for pagination.
    :type since_id: str

    """
    return web.Response(status=200)


async def api_v1_favourites_get(request: web.Request, limit=None, max_id=None, min_id=None) -> web.Response:
    """api_v1_favourites_get

    Statuses the user has favourited.

    :param limit: 
    :type limit: str
    :param max_id: 
    :type max_id: str
    :param min_id: 
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_featured_tags_get(request: web.Request, ) -> web.Response:
    """api_v1_featured_tags_get

    View your featured tags.


    """
    return web.Response(status=200)


async def api_v1_featured_tags_id_delete(request: web.Request, id) -> web.Response:
    """api_v1_featured_tags_id_delete

    Unfeature a tag

    :param id: The id of the FeaturedTag to be unfeatured.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_featured_tags_post(request: web.Request, body=None) -> web.Response:
    """api_v1_featured_tags_post

    Create a feature a tag.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1FeaturedTagsPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_featured_tags_suggestions_get(request: web.Request, ) -> web.Response:
    """api_v1_featured_tags_suggestions_get

    Shows your 10 most-used tags, with usage history for the past week.


    """
    return web.Response(status=200)


async def api_v1_filters_get(request: web.Request, ) -> web.Response:
    """api_v1_filters_get

    


    """
    return web.Response(status=200)


async def api_v1_filters_id_delete(request: web.Request, id) -> web.Response:
    """api_v1_filters_id_delete

    Delete a filter.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_filters_id_get(request: web.Request, id) -> web.Response:
    """api_v1_filters_id_get

    Get one filter.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_filters_id_put(request: web.Request, id, body=None) -> web.Response:
    """api_v1_filters_id_put

    Update a filter.

    :param id: The id of the account in the database
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1FiltersPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_filters_post(request: web.Request, body=None) -> web.Response:
    """api_v1_filters_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1FiltersPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_follow_requests_get(request: web.Request, limit=None) -> web.Response:
    """api_v1_follow_requests_get

    Pending Follows

    :param limit: Maximum number of results to return. Defaults to 40. Paginate using the HTTP Link header.
    :type limit: int

    """
    return web.Response(status=200)


async def api_v1_follow_requests_id_authorize_post(request: web.Request, id) -> web.Response:
    """api_v1_follow_requests_id_authorize_post

    Accept Follow

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_follow_requests_id_reject_post(request: web.Request, id) -> web.Response:
    """api_v1_follow_requests_id_reject_post

    Accept Follow

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_instance_activity_get(request: web.Request, ) -> web.Response:
    """api_v1_instance_activity_get

    Instance activity over the last 3 months, binned weekly.


    """
    return web.Response(status=200)


async def api_v1_instance_get(request: web.Request, ) -> web.Response:
    """api_v1_instance_get

    Information about the server.


    """
    return web.Response(status=200)


async def api_v1_instance_peers_get(request: web.Request, ) -> web.Response:
    """api_v1_instance_peers_get

    Information about the server.


    """
    return web.Response(status=200)


async def api_v1_lists_delete(request: web.Request, ) -> web.Response:
    """api_v1_lists_delete

    Delete a list


    """
    return web.Response(status=200)


async def api_v1_lists_get(request: web.Request, ) -> web.Response:
    """api_v1_lists_get

    Fetch all lists that the user owns.


    """
    return web.Response(status=200)


async def api_v1_lists_id_accounts_delete(request: web.Request, id, account_ids) -> web.Response:
    """api_v1_lists_id_accounts_delete

    Remove accounts from the given list.

    :param id: ID of the list in the database
    :type id: str
    :param account_ids: Array of account IDs to add to the list.
    :type account_ids: List[str]

    """
    return web.Response(status=200)


async def api_v1_lists_id_accounts_get(request: web.Request, id, limit=None, max_id=None, since_id=None) -> web.Response:
    """api_v1_lists_id_accounts_get

    View accounts in List

    :param id: ID of the list in the database
    :type id: str
    :param limit: Maximum number of results. Defaults to 40. Max 40. Set to 0 in order to get all accounts without pagination. Pagination is done with the HTTP Link header.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str

    """
    return web.Response(status=200)


async def api_v1_lists_id_accounts_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_lists_id_accounts_post

    Add accounts to the given list. Note that the user must be following these accounts.

    :param id: ID of the list in the database
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1ListsIdAccountsPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_lists_id_get(request: web.Request, id) -> web.Response:
    """api_v1_lists_id_get

    Remove converstation

    :param id: ID of the list in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_lists_post(request: web.Request, body=None) -> web.Response:
    """api_v1_lists_post

    Create a new list.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1ListsPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_lists_put(request: web.Request, body=None) -> web.Response:
    """api_v1_lists_put

    Change the title of a list, or which replies to show.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1ListsPutRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_markers_get(request: web.Request, timeline) -> web.Response:
    """api_v1_markers_get

    Get saved timeline position

    :param timeline: Array of markers to fetch. String enum anyOf home, notifications. If not provided, an empty object will be returned.
    :type timeline: List[]

    """
    return web.Response(status=200)


async def api_v1_markers_post(request: web.Request, body=None) -> web.Response:
    """api_v1_markers_post

    Get saved timeline position

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def api_v1_media_id_get(request: web.Request, id) -> web.Response:
    """api_v1_media_id_get

    Get an attachement.

    :param id: The id of the Attachment entity to be updated.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_media_id_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_media_id_post

    Update an Attachment, before it is attached to a status and posted.

    :param id: The id of the Attachment entity to be updated.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1MediaPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_media_post(request: web.Request, body=None) -> web.Response:
    """api_v1_media_post

    Creates an attachment to be used with a new status.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1MediaPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_mutes_get(request: web.Request, limit=None, max_id=None, since_id=None) -> web.Response:
    """api_v1_mutes_get

    Accounts the user has muted.

    :param limit: 
    :type limit: str
    :param max_id: 
    :type max_id: str
    :param since_id: 
    :type since_id: str

    """
    return web.Response(status=200)


async def api_v1_notifications_clear_post(request: web.Request, ) -> web.Response:
    """api_v1_notifications_clear_post

    Clear all notifications from the server.


    """
    return web.Response(status=200)


async def api_v1_notifications_get(request: web.Request, limit=None, max_id=None, since_id=None, min_id=None, exclude_types=None, account_id=None) -> web.Response:
    """api_v1_notifications_get

    Notifications concerning the user. This API returns Link headers containing links to the next/previous page. However, the links can also be constructed dynamically using query params and id values.

    :param limit: Max number of results to return. Defaults to 20.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str
    :param min_id: Return results immediately newer than ID
    :type min_id: str
    :param exclude_types: Array of types to exclude (follow, favourite, reblog, mention, poll, follow_request)
    :type exclude_types: List[str]
    :param account_id: Return only notifications received from this account
    :type account_id: str

    """
    return web.Response(status=200)


async def api_v1_notifications_id_dismiss_post(request: web.Request, id) -> web.Response:
    """api_v1_notifications_id_dismiss_post

    Clear a single notification from the server.

    :param id: ID of the notification in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_notifications_id_get(request: web.Request, id) -> web.Response:
    """api_v1_notifications_id_get

    View information about a notification with a given ID.

    :param id: ID of the notification in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_polls_id_get(request: web.Request, id) -> web.Response:
    """api_v1_polls_id_get

    View a poll.

    :param id: ID of the poll in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_polls_id_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_polls_id_post

    Vote on a poll.

    :param id: ID of the poll in the database.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1PollsIdPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_preferences_get(request: web.Request, ) -> web.Response:
    """api_v1_preferences_get

    Shows your 10 most-used tags, with usage history for the past week.


    """
    return web.Response(status=200)


async def api_v1_push_subscription_delete(request: web.Request, ) -> web.Response:
    """api_v1_push_subscription_delete

    Updates the current push subscription. Only the data part can be updated. To change fundamentals, a new subscription must be created instead.


    """
    return web.Response(status=200)


async def api_v1_push_subscription_get(request: web.Request, ) -> web.Response:
    """api_v1_push_subscription_get

    View the PushSubscription currently associated with this access token.


    """
    return web.Response(status=200)


async def api_v1_push_subscription_post(request: web.Request, body=None) -> web.Response:
    """api_v1_push_subscription_post

    Add a Web Push API subscription to receive notifications. Each access token can have one push subscription. If you create a new subscription, the old subscription is deleted.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1PushSubscriptionPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_push_subscription_put(request: web.Request, body=None) -> web.Response:
    """api_v1_push_subscription_put

    Updates the current push subscription. Only the data part can be updated. To change fundamentals, a new subscription must be created instead.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1PushSubscriptionPutRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_reports_post(request: web.Request, body=None) -> web.Response:
    """api_v1_reports_post

    File a report.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1ReportsPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_scheduled_statuses_get(request: web.Request, limit=None, max_id=None, since_id=None, min_id=None) -> web.Response:
    """api_v1_scheduled_statuses_get

    View scheduled statuses

    :param limit: Max number of results to return. Defaults to 20.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str
    :param min_id: Return results immediately newer than ID
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_scheduled_statuses_id_delete(request: web.Request, id) -> web.Response:
    """api_v1_scheduled_statuses_id_delete

    Cancel a scheduled status

    :param id: ID of the scheduled status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_scheduled_statuses_id_get(request: web.Request, id) -> web.Response:
    """api_v1_scheduled_statuses_id_get

    View a single scheduled status

    :param id: ID of the scheduled status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_scheduled_statuses_id_put(request: web.Request, id, body=None) -> web.Response:
    """api_v1_scheduled_statuses_id_put

    View a single scheduled status

    :param id: ID of the scheduled status in the database.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1ScheduledStatusesIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_statuses_id_bookmark_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_bookmark_post

    Privately bookmark a status.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_context_get(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_context_get

    

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_delete(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_delete

    

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_favourite_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_favourite_post

    Add a status to your favourites list.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_favourited_by_get(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_favourited_by_get

    View who favourited a given status.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_get(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_get

    

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_mute_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_mute_post

    Do not receive notifications for the thread that this status is part of. Must be a thread in which you are a participant.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_pin_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_pin_post

    Feature one of your own public statuses at the top of your profile.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_reblog_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_statuses_id_reblog_post

    Reshare a status.

    :param id: Local ID of a status in the database.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1StatusesIdReblogPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_statuses_id_reblogged_by_get(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_reblogged_by_get

    View who boosted a given status.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_unbookmark_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_unbookmark_post

    Remove a status from your private bookmarks.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_unfavourite_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_unfavourite_post

    Remove a status from your favourites list.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_unmute_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_unmute_post

    Status&#39;s conversation unmuted, or was already unmuted

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_unpin_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_unpin_post

    Unfeature a status from the top of your profile.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_id_unreblog_post(request: web.Request, id) -> web.Response:
    """api_v1_statuses_id_unreblog_post

    Undo a reshare of a status.

    :param id: Local ID of a status in the database.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_statuses_post(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """api_v1_statuses_post

    

    :param idempotency_key: Prevent duplicate submissions of the same status. Idempotency keys are stored for up to 1 hour, and can be any arbitrary string. Consider using a hash or UUID generated client-side.
    :type idempotency_key: str
    :param body: 
    :type body: list | bytes

    """
    body = [ApiV1StatusesPostRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def api_v1_suggestions_get(request: web.Request, limit=None) -> web.Response:
    """api_v1_suggestions_get

    Accounts the user has had past positive interactions with, but is not yet following.

    :param limit: Maximum number of results to return. Defaults to 40.
    :type limit: int

    """
    return web.Response(status=200)


async def api_v1_suggestions_id_delete(request: web.Request, id) -> web.Response:
    """api_v1_suggestions_id_delete

    Delete user suggestion

    :param id: id of the account in the database to be removed from suggestions
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_timelines_home_get(request: web.Request, local=None, limit=None, max_id=None, since_id=None, min_id=None) -> web.Response:
    """api_v1_timelines_home_get

    View statuses from followed users.

    :param local: Show only local statuses? Defaults to false.
    :type local: bool
    :param limit: Max number of results to return. Defaults to 20.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str
    :param min_id: Return results immediately newer than ID
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_timelines_list_list_id_get(request: web.Request, list_id, limit=None, max_id=None, since_id=None, min_id=None) -> web.Response:
    """api_v1_timelines_list_list_id_get

    View statuses in the given list timeline.

    :param list_id: Local ID of the list in the database.
    :type list_id: str
    :param limit: Max number of results to return. Defaults to 20.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str
    :param min_id: Return results immediately newer than ID
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_timelines_public_get(request: web.Request, local=None, remote=None, only_media=None, limit=None, max_id=None, since_id=None, min_id=None) -> web.Response:
    """api_v1_timelines_public_get

    Public timeline

    :param local: Show only local statuses? Defaults to false.
    :type local: bool
    :param remote: Show only local statuses? Defaults to false.
    :type remote: bool
    :param only_media: Show only statuses with media attached? Defaults to false..
    :type only_media: bool
    :param limit: Max number of results to return. Defaults to 20.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str
    :param min_id: Return results immediately newer than ID
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_timelines_tag_hashtag_get(request: web.Request, hashtag, local=None, remote=None, only_media=None, limit=None, max_id=None, since_id=None, min_id=None) -> web.Response:
    """api_v1_timelines_tag_hashtag_get

    View public statuses containing the given hashtag.

    :param hashtag: Content of a &#x60;#hashtag&#x60;&#x60;, not including &#x60;#&#x60; symbol..
    :type hashtag: str
    :param local: Show only local statuses? Defaults to false.
    :type local: bool
    :param remote: Show only local statuses? Defaults to false.
    :type remote: bool
    :param only_media: Show only statuses with media attached? Defaults to false..
    :type only_media: bool
    :param limit: Max number of results to return. Defaults to 20.
    :type limit: int
    :param max_id: Return results older than ID
    :type max_id: str
    :param since_id: Return results newer than ID
    :type since_id: str
    :param min_id: Return results immediately newer than ID
    :type min_id: str

    """
    return web.Response(status=200)


async def api_v1_trends_get(request: web.Request, limit=None) -> web.Response:
    """api_v1_trends_get

    Tags that are being used more frequently within the past week.

    :param limit: Max number of results to return. Defaults to 10.
    :type limit: int

    """
    return web.Response(status=200)


async def api_v2_search_get(request: web.Request, q, limit=None, resolve=None, following=None, account_id=None, max_id=None, min_id=None, type=None, exclude_unreviewed=None, offset=None) -> web.Response:
    """api_v2_search_get

    Search results

    :param q: What to search for
    :type q: str
    :param limit: Maximum number of results. Defaults to 40.
    :type limit: int
    :param resolve: Attempt WebFinger lookup.
    :type resolve: str
    :param following: Only who the user is following. Defaults to false.
    :type following: bool
    :param account_id: If provided, statuses returned will be authored only by this account
    :type account_id: str
    :param max_id: Return results older than this id
    :type max_id: str
    :param min_id: Return results immediately newer than this id
    :type min_id: str
    :param type: Enum(accounts, hashtags, statuses)
    :type type: str
    :param exclude_unreviewed: Filter out unreviewed tags? Defaults to false. Use true when trying to find trending tags.
    :type exclude_unreviewed: bool
    :param offset: Offset in search results. Used for pagination. Defaults to 0.
    :type offset: int

    """
    return web.Response(status=200)
