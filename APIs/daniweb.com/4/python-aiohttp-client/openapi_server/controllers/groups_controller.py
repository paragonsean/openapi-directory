from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_delete_groups_id_memberships import EndpointDeleteGroupsIDMemberships
from openapi_server.models.endpoint_delete_groups_messages_id import EndpointDeleteGroupsMessagesID
from openapi_server.models.endpoint_get_groups import EndpointGetGroups
from openapi_server.models.endpoint_get_groups_id import EndpointGetGroupsID
from openapi_server.models.endpoint_get_groups_id_memberships import EndpointGetGroupsIDMemberships
from openapi_server.models.endpoint_get_groups_id_messages import EndpointGetGroupsIDMessages
from openapi_server.models.endpoint_get_groups_id_statuses import EndpointGetGroupsIDStatuses
from openapi_server.models.endpoint_get_groups_messages_id import EndpointGetGroupsMessagesID
from openapi_server.models.endpoint_get_groups_messages_id_metadata import EndpointGetGroupsMessagesIDMetadata
from openapi_server.models.endpoint_get_groups_messages_id_metadata_collections import EndpointGetGroupsMessagesIDMetadataCollections
from openapi_server.models.endpoint_get_groups_statuses import EndpointGetGroupsStatuses
from openapi_server.models.endpoint_patch_groups_id import EndpointPatchGroupsID
from openapi_server.models.endpoint_patch_groups_id_memberships import EndpointPatchGroupsIDMemberships
from openapi_server.models.endpoint_post_groups import EndpointPostGroups
from openapi_server.models.endpoint_post_groups_id_memberships import EndpointPostGroupsIDMemberships
from openapi_server.models.endpoint_post_groups_id_messages import EndpointPostGroupsIDMessages
from openapi_server.models.endpoint_post_groups_id_schedules import EndpointPostGroupsIDSchedules
from openapi_server.models.endpoint_post_groups_messages_id_metadata import EndpointPostGroupsMessagesIDMetadata
from openapi_server.models.endpoint_post_groups_messages_metadata_filters import EndpointPostGroupsMessagesMetadataFilters
from openapi_server.models.endpoint_post_groups_schedules import EndpointPostGroupsSchedules
from openapi_server import util


async def groups_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """groups_get

    Fetch an array of all groups that were created by users existing within the current access token&#39;s bubble. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed.

    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def groups_id_memberships_delete(request: web.Request, id) -> web.Response:
    """groups_id_memberships_delete

    Leave a group that you are a member of and that was created by a user who exists within the current access token&#39;s bubble.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def groups_id_memberships_get(request: web.Request, id, moderators_only=None, offset=None) -> web.Response:
    """groups_id_memberships_get

    Fetch an array of users who are members of specific groups that you are also a member of. You can only retrieve users existing within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]
    :param moderators_only: 
    :type moderators_only: bool
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def groups_id_memberships_patch(request: web.Request, id, user_id, moderator=None) -> web.Response:
    """groups_id_memberships_patch

    Promote or demote a member&#39;s privileges within a group that you created. The user must exist within the current access token&#39;s bubble and be an existing member of the group.

    :param id: 
    :type id: int
    :param user_id: 
    :type user_id: int
    :param moderator: 
    :type moderator: bool

    """
    return web.Response(status=200)


async def groups_id_memberships_post(request: web.Request, id, passphrase=None, user_id=None) -> web.Response:
    """groups_id_memberships_post

    Join a group that was created by a user who exists within the current access token&#39;s bubble, or join other users into a group that you created. If you are the group owner, you can pass in a user_id to create membership records for a user you are in a conversation with. The user must exist within the current access token&#39;s bubble. If the group is private, you must successfully pass in its passphrase in order to join. You can obtain the passphrase from the group&#39;s owner.

    :param id: 
    :type id: int
    :param passphrase: 
    :type passphrase: str
    :param user_id: 
    :type user_id: int

    """
    return web.Response(status=200)


async def groups_id_messages_get(request: web.Request, id, gt_message_id=None, exclude_self=None, include_deleted=None, _date=None, bubbled=None, record_seen=None, timeout=None, offset=None, limit=None) -> web.Response:
    """groups_id_messages_get

    Retrieve the last {limit} messages in the group, for messages authored by users within the current access token&#39;s bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you&#39;ve seen with other group members. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by other members of the group, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token&#39;s bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the group is reset to zero.

    :param id: 
    :type id: int
    :param gt_message_id: 
    :type gt_message_id: int
    :param exclude_self: 
    :type exclude_self: bool
    :param include_deleted: 
    :type include_deleted: bool
    :param _date: 
    :type _date: str
    :param bubbled: 
    :type bubbled: bool
    :param record_seen: 
    :type record_seen: bool
    :param timeout: 
    :type timeout: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def groups_id_messages_post(request: web.Request, id, text_raw, metadata_0_key=None, metadata_0_privacy=None, metadata_0_values=None, metadata_1_key=None, metadata_1_privacy=None, metadata_1_values=None, metadata_2_key=None, metadata_2_privacy=None, metadata_2_values=None, text_emoticons=None) -> web.Response:
    """groups_id_messages_post

    Post a message to a group that you are a member of and that was created by a user who exists within the current access token&#39;s bubble. Optionally specify whether emoticons should be parsed into smiley images. Additionally, optionally attach a single metadata key/value pair to the group message upon submission.

    :param id: 
    :type id: int
    :param text_raw: 
    :type text_raw: str
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_privacy: 
    :type metadata_0_privacy: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_privacy: 
    :type metadata_1_privacy: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_privacy: 
    :type metadata_2_privacy: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]
    :param text_emoticons: 
    :type text_emoticons: bool

    """
    return web.Response(status=200)


async def groups_id_schedules_post(request: web.Request, id, _date=None, limit=None, offset=None, roll_up=None, sort=None) -> web.Response:
    """groups_id_schedules_post

    Paginated report of information about group messages contributed by conversation and date. Only groups you&#39;re a member of and group messages authored by users existing within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the group discussion(s).

    :param id: 
    :type id: List[int]
    :param _date: 
    :type _date: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param roll_up: 
    :type roll_up: bool
    :param sort: 
    :type sort: str

    """
    return web.Response(status=200)


async def groups_id_statuses_get(request: web.Request, id) -> web.Response:
    """groups_id_statuses_get

    Status information about your current relationship with one or more groups you are a member of, provided the users who created the groups exist within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def groups_idget(request: web.Request, id) -> web.Response:
    """groups_idget

    Fetch an array of groups. You can only retrieve groups created by users existing within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def groups_idpatch(request: web.Request, id, description=None, name=None, passphrase=None, privacy=None, slug=None) -> web.Response:
    """groups_idpatch

    Modify a group you previously created.

    :param id: 
    :type id: int
    :param description: 
    :type description: str
    :param name: 
    :type name: str
    :param passphrase: 
    :type passphrase: str
    :param privacy: 
    :type privacy: str
    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def groups_messages_id_metadata_collections_get(request: web.Request, id) -> web.Response:
    """groups_messages_id_metadata_collections_get

    Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def groups_messages_id_metadata_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """groups_messages_id_metadata_get

    Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

    :param id: 
    :type id: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def groups_messages_id_metadata_post(request: web.Request, id, metadata_0_key=None, metadata_0_privacy=None, metadata_0_values=None, metadata_1_key=None, metadata_1_privacy=None, metadata_1_values=None, metadata_2_key=None, metadata_2_privacy=None, metadata_2_values=None) -> web.Response:
    """groups_messages_id_metadata_post

    Attach one-to-many key/value pairs of metadata to a group message, so long as the user who authored the message exists within the current access token&#39;s bubble and you are a member of their group. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user who authored the message and who is also a member of the group the message belongs to; Bubbled metadata by anyone using an access token existing within the current bubble who is also a member of the group the message belongs to; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message and you remain a member of the group; Private metadata by you, so long as you are using an access token existing within the current bubble and you remain a member of the group.

    :param id: 
    :type id: int
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_privacy: 
    :type metadata_0_privacy: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_privacy: 
    :type metadata_1_privacy: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_privacy: 
    :type metadata_2_privacy: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]

    """
    return web.Response(status=200)


async def groups_messages_iddelete(request: web.Request, id) -> web.Response:
    """groups_messages_iddelete

    Delete an array of group messages. You must be the owner or moderator of the group.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def groups_messages_idget(request: web.Request, id) -> web.Response:
    """groups_messages_idget

    Fetch an array of group messages. You can only retrieve messages authored by you or by users existing within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def groups_messages_metadata_filters_post(request: web.Request, limit=None, metadata_0_key=None, metadata_0_values=None, metadata_1_key=None, metadata_1_values=None, metadata_2_key=None, metadata_2_values=None, offset=None) -> web.Response:
    """groups_messages_metadata_filters_post

    Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

    :param limit: 
    :type limit: int
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def groups_post(request: web.Request, description, name, privacy, slug, passphrase=None) -> web.Response:
    """groups_post

    Create a new group for other members to join. Any user who is using an access token whose bubble you exist in can join your group provided it is not a private group. Private groups can only be joined by members who know its passphrase. Unlisted groups can be joined by anybody as long as they know the Group ID, but they are not referenced anywhere to non-members. Public groups can be joined by anybody, are discoverable, and anyone can see the public groups a user is a member of, provided the group owner exists in their access token&#39;s bubble. Groups each have their own discussions, transcripts, schedules, and ability to list and search their members.

    :param description: 
    :type description: str
    :param name: 
    :type name: str
    :param privacy: 
    :type privacy: str
    :param slug: 
    :type slug: str
    :param passphrase: 
    :type passphrase: str

    """
    return web.Response(status=200)


async def groups_schedules_post(request: web.Request, _date=None, limit=None, offset=None, roll_up=None, sort=None) -> web.Response:
    """groups_schedules_post

    Paginated report of information about messages contributed by group and date. Only groups you&#39;re a member of and group messages authored by users the current access token has access to are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

    :param _date: 
    :type _date: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param roll_up: 
    :type roll_up: bool
    :param sort: 
    :type sort: str

    """
    return web.Response(status=200)


async def groups_statuses_get(request: web.Request, existing_membership=None, offset=None, limit=None) -> web.Response:
    """groups_statuses_get

    Retrieve groups that were created by users within the current access token&#39;s bubble, along with your current relationship with the groups. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed. Optionally only retrieve groups that you are a member of.

    :param existing_membership: 
    :type existing_membership: bool
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)
