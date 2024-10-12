from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_participants_search_result import AddParticipantsSearchResult
from openapi_server.models.basic_search_result import BasicSearchResult
from openapi_server.models.directory_result import DirectoryResult
from openapi_server.models.flagged_items_result import FlaggedItemsResult
from openapi_server.models.label_ids import LabelIds
from openapi_server.models.participants_import_data_result import ParticipantsImportDataResult
from openapi_server.models.participants_like_result import ParticipantsLikeResult
from openapi_server.models.participants_search_result import ParticipantsSearchResult
from openapi_server.models.participants_search_result_large import ParticipantsSearchResultLarge
from openapi_server.models.space_pinned_topic import SpacePinnedTopic
from openapi_server.models.space_reply import SpaceReply
from openapi_server.models.space_search_result_detailed_back import SpaceSearchResultDetailedBack
from openapi_server.models.space_topic import SpaceTopic
from openapi_server.models.space_topic_with_replies import SpaceTopicWithReplies
from openapi_server.models.spaces_search_term_result import SpacesSearchTermResult
from openapi_server import util


async def add_participants_to_space(request: web.Request, id, role, user_id) -> web.Response:
    """Add Participant to Space

    Add a participant to a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

    :param id: The id of the space
    :type id: str
    :param role: The name of the role of the participant
    :type role: str
    :param user_id: The user id of the participant
    :type user_id: List[str]

    """
    return web.Response(status=200)


async def add_recent_space_search(request: web.Request, scope, search_term, end_time=None, start_time=None) -> web.Response:
    """Add recent search 

    Add recent search of a client to search controller. OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

    :param scope: The scope of the search.
    :type scope: str
    :param search_term: The term to search for.
    :type search_term: str
    :param end_time: The end time.
    :type end_time: str
    :param start_time: The start time.
    :type start_time: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def assign_labels(request: web.Request, id, labels) -> web.Response:
    """Assign labels

    Assign labels to space OauthScopes: WRITE_SPACE, ORGANIZE_SPACE

    :param id: The id of the space.
    :type id: str
    :param labels: The labels to assign to the space
    :type labels: List[str]

    """
    return web.Response(status=200)


async def cancel_space_search(request: web.Request, search_id) -> web.Response:
    """Cancels a space search of a client.

    Cancels a space search of a client. OauthScopes: WRITE_SPACE, MANAGE_SPACE

    :param search_id: The id of the search to cancel
    :type search_id: str

    """
    return web.Response(status=200)


async def create_reply(request: web.Request, space_id, topic_id, attachments=None, complex=None, content=None, form_meta_data=None, mentioned_user=None) -> web.Response:
    """creates a reply to a topic

    creates a reply to a topic OauthScopes: WRITE_SPACE

    :param space_id: ID of the space
    :type space_id: str
    :param topic_id: ID of the topic
    :type topic_id: str
    :param attachments: the attached files
    :type attachments: List[str]
    :param complex: complex or not
    :type complex: bool
    :param content: Content of the reply
    :type content: str
    :param form_meta_data: formMetaData used in the reply
    :type form_meta_data: str
    :param mentioned_user: the user mentioned in the reply
    :type mentioned_user: str

    """
    return web.Response(status=200)


async def create_space(request: web.Request, access_mode_type, name, role, status, type, description=None, large_picture_base64=None, small_picture_base64=None, tags=None) -> web.Response:
    """Create a space

    Create a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, CREATE_SPACE_CONTENT

    :param access_mode_type: Access mode
    :type access_mode_type: str
    :param name: name of the space
    :type name: str
    :param role: role
    :type role: str
    :param status: status
    :type status: str
    :param type: type
    :type type: str
    :param description: description of the space
    :type description: str
    :param large_picture_base64: large picture
    :type large_picture_base64: str
    :param small_picture_base64: small picture
    :type small_picture_base64: str
    :param tags: tags of the space
    :type tags: List[str]

    """
    return web.Response(status=200)


async def create_space_topic(request: web.Request, space_id, subject, attachments=None, complex=None, content=None, content_tags=None, form_meta_data=None, mentioned_user=None, tags=None) -> web.Response:
    """creates a new space topic

    creates a new space topic OauthScopes: WRITE_SPACE, MANAGE_SPACE, CREATE_SPACE_CONTENT

    :param space_id: The ID of the space
    :type space_id: str
    :param subject: The subject of the topic
    :type subject: str
    :param attachments: the attached files
    :type attachments: List[str]
    :param complex: complex or not
    :type complex: bool
    :param content: The content of this topic
    :type content: str
    :param content_tags: the content tags
    :type content_tags: List[str]
    :param form_meta_data: The formMetaData
    :type form_meta_data: str
    :param mentioned_user: A list of mentioned users
    :type mentioned_user: str
    :param tags: the tags
    :type tags: List[str]

    """
    return web.Response(status=200)


async def delete_space(request: web.Request, id) -> web.Response:
    """Delete a space

    Delete a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, DELETE_SPACE_CONTENT

    :param id: id of the space
    :type id: str

    """
    return web.Response(status=200)


async def delete_space_item(request: web.Request, item_id) -> web.Response:
    """deletes a space item

    deletes a space item OauthScopes: WRITE_SPACE, DELETE_SPACE_CONTENT

    :param item_id: the id of the spaceItem
    :type item_id: str

    """
    return web.Response(status=200)


async def deny_space_acces(request: web.Request, space_id, participant_id, reason=None) -> web.Response:
    """Deny access for a space

    Deny access for a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

    :param space_id: Id of the space
    :type space_id: str
    :param participant_id: Id of the participant
    :type participant_id: str
    :param reason: Reason why the request has been denied
    :type reason: str

    """
    return web.Response(status=200)


async def exists_space_name(request: web.Request, name) -> web.Response:
    """Space name exists

    Find out if a space name already exists for non-secret spaces. OauthScopes: READ_SPACE

    :param name: The name to check for existence.
    :type name: str

    """
    return web.Response(status=200)


async def flag_space_item(request: web.Request, item_id) -> web.Response:
    """flag a space item

    flag a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param item_id: the id of the item you want to flag
    :type item_id: str

    """
    return web.Response(status=200)


async def get_directory(request: web.Request, sort_by, sort_order, filter, query=None, page_pointer=None, number_of_results=None) -> web.Response:
    """Get the directory

    Get the directory by a search query in ordered way OauthScopes: READ_SPACE

    :param sort_by: sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE
    :type sort_by: str
    :param sort_order: ascending or descending
    :type sort_order: str
    :param filter: filter for spaces (JOINED, REQUESTED, OPEN, CLOSED or NOT_JOINED_REQUESTED)
    :type filter: str
    :param query: some sort of query
    :type query: str
    :param page_pointer: page pointer, start with nothing and for next query use returned pointer
    :type page_pointer: str
    :param number_of_results: number of results to return, 25 by default.
    :type number_of_results: 

    """
    return web.Response(status=200)


async def get_flagged_items(request: web.Request, search_direction, timestamp, search_pointer=None, number_of_results=None) -> web.Response:
    """Get flagged items

    Get flagged items OauthScopes: READ_SPACE

    :param search_direction: before or after the time stamp
    :type search_direction: str
    :param timestamp: The timestamp according to which you want to retrieve the flagged items
    :type timestamp: str
    :param search_pointer: The searchpointer for the search (initially not set).
    :type search_pointer: str
    :param number_of_results: The number of results you want to retrieve.
    :type number_of_results: 

    """
    timestamp = util.deserialize_datetime(timestamp)
    return web.Response(status=200)


async def get_likes(request: web.Request, item_id, search_pointer=None, number_of_results=None) -> web.Response:
    """Get the likes of an item

    Get the likes of an item OauthScopes: READ_SPACE

    :param item_id: The id of the item to retrieve the likes from
    :type item_id: str
    :param search_pointer: The searchpointer for the search (initially not set).
    :type search_pointer: str
    :param number_of_results: The number of results you want to retrieve.
    :type number_of_results: 

    """
    return web.Response(status=200)


async def get_participants_import_data(request: web.Request, space_id) -> web.Response:
    """missing documentation

    missing documentation OauthScopes: READ_SPACE

    :param space_id: missing documentation
    :type space_id: str

    """
    return web.Response(status=200)


async def get_pending_participants(request: web.Request, id, search_pointer=None, number_of_results=None) -> web.Response:
    """Get the pending participants of a space

    Get the pending participants of a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

    :param id: The id of the space.
    :type id: str
    :param search_pointer: The search pointer (leave empty initially).
    :type search_pointer: str
    :param number_of_results: number of results to return, 25 by default.
    :type number_of_results: 

    """
    return web.Response(status=200)


async def get_pinned_topics(request: web.Request, id) -> web.Response:
    """Retrieve pinned topics

    Retrieve pinned topics of a space OauthScopes: READ_SPACE

    :param id: The id of the space.
    :type id: str

    """
    return web.Response(status=200)


async def get_recent_searches(request: web.Request, ) -> web.Response:
    """Retrieve recent space searches

    Retrieve recent space searches for a user. OauthScopes: READ_SPACE


    """
    return web.Response(status=200)


async def get_space_participants(request: web.Request, id, sort_by, sort_order, filter_type, filter_value=None, query=None, search_pointer=None, number_of_results=None) -> web.Response:
    """Get the participants of a space

    Get the participants of a space OauthScopes: READ_SPACE

    :param id: The id of the space.
    :type id: str
    :param sort_by: sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE
    :type sort_by: str
    :param sort_order: ascending or descending
    :type sort_order: str
    :param filter_type: filtertype for participants (ACCESS_TYPE, ROLE or STATE)
    :type filter_type: str
    :param filter_value: value for the filter
    :type filter_value: str
    :param query: some sort of query
    :type query: str
    :param search_pointer: The search pointer (leave empty initially).
    :type search_pointer: str
    :param number_of_results: number of results to return, 25 by default.
    :type number_of_results: 

    """
    return web.Response(status=200)


async def get_space_replies(request: web.Request, space_id, topic_id, search_direction, timestamp=None, number_of_results=None) -> web.Response:
    """Gets space replies

    Gets a number of Space replies OauthScopes: READ_SPACE

    :param space_id: Id of the containing space
    :type space_id: str
    :param topic_id: Id of the topic
    :type topic_id: str
    :param search_direction: Search before or after a certain timestamp
    :type search_direction: str
    :param timestamp: Timestamp to start the search from
    :type timestamp: str
    :param number_of_results: The number of results that should be returned
    :type number_of_results: 

    """
    timestamp = util.deserialize_datetime(timestamp)
    return web.Response(status=200)


async def get_space_topics(request: web.Request, space_id, search_direction, timestamp=None, number_of_results=None) -> web.Response:
    """Gets space topics

    Gets a number of Space topics OauthScopes: READ_SPACE

    :param space_id: Id of the space
    :type space_id: str
    :param search_direction: Search before or after a certain timestamp
    :type search_direction: str
    :param timestamp: Timestamp to start the search from
    :type timestamp: str
    :param number_of_results: The number of results that should be returned
    :type number_of_results: 

    """
    timestamp = util.deserialize_datetime(timestamp)
    return web.Response(status=200)


async def get_spaces(request: web.Request, timestamp=None, number_of_results=None) -> web.Response:
    """Get the spaces

    Get the spaces OauthScopes: READ_SPACE

    :param timestamp: a beautiful timestamp
    :type timestamp: str
    :param number_of_results: the number of results you want
    :type number_of_results: 

    """
    timestamp = util.deserialize_datetime(timestamp)
    return web.Response(status=200)


async def get_spaces_by_ids(request: web.Request, ids) -> web.Response:
    """Get the spaces by their ids

    Get the spaces by their ids OauthScopes: READ_SPACE

    :param ids: an array of ids
    :type ids: List[str]

    """
    return web.Response(status=200)


async def grant_space_acces(request: web.Request, space_id, participant_id) -> web.Response:
    """grant access for a space

    grant access for a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

    :param space_id: Id of the space
    :type space_id: str
    :param participant_id: Id of the participant
    :type participant_id: str

    """
    return web.Response(status=200)


async def join_space(request: web.Request, id) -> web.Response:
    """Join a space

    Join a space OauthScopes: WRITE_SPACE

    :param id: The id of the space
    :type id: str

    """
    return web.Response(status=200)


async def leave_space(request: web.Request, id) -> web.Response:
    """Leave a space

    Leave a space OauthScopes: WRITE_SPACE

    :param id: The id of the space
    :type id: str

    """
    return web.Response(status=200)


async def like_space_item(request: web.Request, item_id) -> web.Response:
    """Like a space item

    Like a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param item_id: The id of the item you want to like
    :type item_id: str

    """
    return web.Response(status=200)


async def pin_topic(request: web.Request, topic_id, position) -> web.Response:
    """Pin a topic

    Pin a topic OauthScopes: WRITE_SPACE, MANAGE_SPACE

    :param topic_id: The id of the topic
    :type topic_id: str
    :param position: The position to pin to
    :type position: 

    """
    return web.Response(status=200)


async def request_space_acces(request: web.Request, space_id, reason=None) -> web.Response:
    """request access for a space

    request access for a space OauthScopes: READ_SPACE

    :param space_id: Id of the space
    :type space_id: str
    :param reason: Reason why the Access has been requested
    :type reason: str

    """
    return web.Response(status=200)


async def search_participants_to_add(request: web.Request, id, query) -> web.Response:
    """Finds participants to add to add to a space 

    Finds participants to add to a space  OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

    :param id: The id of the space
    :type id: str
    :param query: The query 
    :type query: str

    """
    return web.Response(status=200)


async def search_space_participants(request: web.Request, id, query) -> web.Response:
    """Get the participants of a space

    Get the participants of a space OauthScopes: READ_SPACE

    :param id: The id of the space.
    :type id: str
    :param query: The query to search with. If searchpointer/hasMotre is returned, refine query.
    :type query: str

    """
    return web.Response(status=200)


async def start_basic_spaces_search(request: web.Request, scope, search_term, start_time=None, end_time=None, priority_spaces=None) -> web.Response:
    """starts a basic search in spaces

    starts a basic search in spaces OauthScopes: READ_SPACE

    :param scope: the scope of the search
    :type scope: str
    :param search_term: the term to search for
    :type search_term: str
    :param start_time: the starttime
    :type start_time: str
    :param end_time: the end time
    :type end_time: str
    :param priority_spaces: list of prioritized spaces
    :type priority_spaces: List[str]

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def start_detailed_space_search(request: web.Request, scope, search_term, space_id, start_time=None, end_time=None, search_id=None) -> web.Response:
    """starts a detailed search in a space

    starts a detailed search in a space OauthScopes: READ_SPACE

    :param scope: the scope of the search
    :type scope: str
    :param search_term: the term to search for
    :type search_term: str
    :param space_id: missing documentation
    :type space_id: str
    :param start_time: the starttime
    :type start_time: str
    :param end_time: the end time
    :type end_time: str
    :param search_id: missing documentation
    :type search_id: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def unassign_labels(request: web.Request, id, label_ids) -> web.Response:
    """Unassign labels

    Unassign labels from a space OauthScopes: WRITE_SPACE, ORGANIZE_SPACE

    :param id: The id of the space.
    :type id: str
    :param label_ids: missing documentation
    :type label_ids: List[str]

    """
    return web.Response(status=200)


async def unflag_space_item(request: web.Request, item_id) -> web.Response:
    """Unflag a space item

    Unflag a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param item_id: the id of the item you want to unflag
    :type item_id: str

    """
    return web.Response(status=200)


async def unlike_space_item(request: web.Request, item_id) -> web.Response:
    """Unlike a space item

    Unlike a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param item_id: The id of the item you want to unlike
    :type item_id: str

    """
    return web.Response(status=200)


async def unpin_topic(request: web.Request, topic_id) -> web.Response:
    """Unpin a topic

    Unpin a topic OauthScopes: WRITE_SPACE, MANAGE_SPACE

    :param topic_id: The id of the topic to unpin
    :type topic_id: str

    """
    return web.Response(status=200)


async def update_participant_in_space(request: web.Request, space_id, role, user_id) -> web.Response:
    """Update participant

    Update participant in space OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

    :param space_id: Id of the space
    :type space_id: str
    :param role: updated role of participant
    :type role: str
    :param user_id: The id of the participant to update
    :type user_id: str

    """
    return web.Response(status=200)


async def update_read_timestamp(request: web.Request, id, timestamp) -> web.Response:
    """Update read timestamp

    Update read timestamp OauthScopes: READ_SPACE, WRITE_SPACE

    :param id: Id of a space
    :type id: str
    :param timestamp: The new timestamp
    :type timestamp: str

    """
    timestamp = util.deserialize_datetime(timestamp)
    return web.Response(status=200)


async def update_space(request: web.Request, id, access_mode_type=None, description=None, large_picture_base64=None, name=None, owner_id=None, role=None, small_picture_base64=None, status=None, tags=None, type=None) -> web.Response:
    """Update a space

    Update a space OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param id: id of the space
    :type id: str
    :param access_mode_type: Access mode
    :type access_mode_type: str
    :param description: description of the space
    :type description: str
    :param large_picture_base64: large picture
    :type large_picture_base64: str
    :param name: name of the space
    :type name: str
    :param owner_id: ownerid of the space
    :type owner_id: str
    :param role: role
    :type role: str
    :param small_picture_base64: small picture
    :type small_picture_base64: str
    :param status: status
    :type status: str
    :param tags: tags of the space
    :type tags: List[str]
    :param type: type
    :type type: str

    """
    return web.Response(status=200)


async def update_space_reply(request: web.Request, space_id, topic_id, reply_id, attachments=None, complex=None, content=None, form_meta_data=None, mentioned_users=None) -> web.Response:
    """Updates a space reply

    Updates a space reply OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param space_id: ID of the space
    :type space_id: str
    :param topic_id: ID of the topic
    :type topic_id: str
    :param reply_id: id of the reply
    :type reply_id: str
    :param attachments: the attached files
    :type attachments: List[str]
    :param complex: complex or not
    :type complex: bool
    :param content: the content of the reply
    :type content: str
    :param form_meta_data: formMetaData of the reply
    :type form_meta_data: str
    :param mentioned_users: the mentioned users in the reply
    :type mentioned_users: List[str]

    """
    return web.Response(status=200)


async def update_space_topic(request: web.Request, space_id, topic_id, attachments=None, complex=None, content=None, content_tags=None, form_meta_data=None, mentioned_users=None, subject=None, tags=None) -> web.Response:
    """Updates a topic

    Updates a topic OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param space_id: ID of the space
    :type space_id: str
    :param topic_id: Id of the topic to update
    :type topic_id: str
    :param attachments: the attached files
    :type attachments: List[str]
    :param complex: complex or not
    :type complex: bool
    :param content: content of the topic
    :type content: str
    :param content_tags: the content tags
    :type content_tags: List[str]
    :param form_meta_data: formMetaData to update
    :type form_meta_data: str
    :param mentioned_users: the updated mentioned users
    :type mentioned_users: List[str]
    :param subject: the subject of the topic
    :type subject: str
    :param tags: the tags
    :type tags: List[str]

    """
    return web.Response(status=200)


async def update_topic_tags(request: web.Request, topic_id, tags) -> web.Response:
    """Update tags

    Update the tags of a topic   OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

    :param topic_id: The id of the topic
    :type topic_id: str
    :param tags: The tags to update
    :type tags: List[str]

    """
    return web.Response(status=200)


async def v2_get_topic_with_replies(request: web.Request, space_id, topic_id, number_of_replies=None) -> web.Response:
    """Gets space replies and a topic

    Gets a number of Space replies with a matching topic OauthScopes: READ_SPACE

    :param space_id: Id of the topic
    :type space_id: str
    :param topic_id: ID of the topic
    :type topic_id: str
    :param number_of_replies: The number of replies
    :type number_of_replies: 

    """
    return web.Response(status=200)


async def v2_remove_participants_from_space(request: web.Request, id, user_ids) -> web.Response:
    """Removes participants from a space

    removes Participants from a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

    :param id: The id of the space
    :type id: str
    :param user_ids: The ids of the participants to remove 
    :type user_ids: List[str]

    """
    return web.Response(status=200)


async def v2_update_welcome_box_content(request: web.Request, space_id, content, display_welcome_box=None) -> web.Response:
    """Update content of welcome box

    Update content of the welcome box of a space OauthScopes: MANAGE_SPACE, WRITE_SPACE

    :param space_id: Id of the space
    :type space_id: str
    :param content: The new content
    :type content: str
    :param display_welcome_box: True, false, default:false
    :type display_welcome_box: bool

    """
    return web.Response(status=200)
