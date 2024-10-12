from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation import Conversation
from openapi_server.models.conversation_details import ConversationDetails
from openapi_server.models.conversation_item import ConversationItem
from openapi_server.models.conversation_participants_list import ConversationParticipantsList
from openapi_server.models.conversation_search_result import ConversationSearchResult
from openapi_server.models.conversations_page import ConversationsPage
from openapi_server.models.label import Label
from openapi_server.models.pinned_topic import PinnedTopic
from openapi_server.models.user import User
from openapi_server import util


async def add_favorite(request: web.Request, conv_id) -> web.Response:
    """Adds a conversation to the favorites

    Adds a conversation to the favorites. Favorites can be displayed in a separate side tab inside of the Circuit client to have a better overview of important conversations. OauthScopes: WRITE_CONVERSATIONS

    :param conv_id: The ID of the conversation which will be marked as favorite
    :type conv_id: str

    """
    return web.Response(status=200)


async def add_label(request: web.Request, label) -> web.Response:
    """Add a user label

    Add a label to the list of user labels OauthScopes: WRITE_USER_PROFILE, ORGANIZE_CONVERSATIONS

    :param label: The label value to add
    :type label: str

    """
    return web.Response(status=200)


async def add_moderators(request: web.Request, conv_id, moderators) -> web.Response:
    """Add moderators

    Adds a list of moderators to a conversation OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the moderators are added
    :type conv_id: str
    :param moderators: The list of moderator ids to add 
    :type moderators: List[str]

    """
    return web.Response(status=200)


async def add_participant_community(request: web.Request, conv_id, participants) -> web.Response:
    """Adds participants to a community

    Adds one or more participants to the given community. This operation can only be performed by a user who is already a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the participant has to be added.
    :type conv_id: str
    :param participants: The IDs or the unique email addresses of the Circuit users that should to be added.
    :type participants: List[str]

    """
    return web.Response(status=200)


async def add_participant_group(request: web.Request, conv_id, participants) -> web.Response:
    """Adds participants to a group conversation

    Adds one or more participants to the given group conversation. This operation can only be performed by a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the participant has to be added.
    :type conv_id: str
    :param participants: The IDs or the unique email addresses of the Circuit users that should to be added.
    :type participants: List[str]

    """
    return web.Response(status=200)


async def add_text_item(request: web.Request, conv_id, attachments=None, content=None, form_meta_data=None, subject=None) -> web.Response:
    """Adds a message to a conversation

    Adds a message to the given conversation. This operation can be only performed on behalf of a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, CREATE_CONVERSATIONS_CONTENT

    :param conv_id: The ID of the conversation to which the new item has to be added
    :type conv_id: str
    :param attachments: A comma separated list of attachment IDs from the file API.
    :type attachments: List[str]
    :param content: The actual content of the item, is mandatory unless an attachment is added
    :type content: str
    :param form_meta_data: The form meta data of the new text item
    :type form_meta_data: str
    :param subject: The subject (headline) of the new text item
    :type subject: str

    """
    return web.Response(status=200)


async def add_text_item_with_parent(request: web.Request, conv_id, item_id, attachments=None, content=None, form_meta_data=None, subject=None) -> web.Response:
    """Adds a message to an item

    Adds a message to the existing item. The added message will be a child item of the message with the given itemId. OauthScopes: WRITE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the new item has to be added
    :type conv_id: str
    :param item_id: The ID of the item to which the new one has to be added as child
    :type item_id: str
    :param attachments: A comma separated list of attachment IDs from the file API.
    :type attachments: List[str]
    :param content: The actual content of the item
    :type content: str
    :param form_meta_data: The form meta data of the new text item
    :type form_meta_data: str
    :param subject: The subject (headline) of the new text item
    :type subject: str

    """
    return web.Response(status=200)


async def archive_conversation(request: web.Request, conv_id) -> web.Response:
    """Archives conversation

    Archives a conversation by muting it OauthScopes: WRITE_CONVERSATIONS

    :param conv_id: The ID of the conversation which will be archived
    :type conv_id: str

    """
    return web.Response(status=200)


async def assign_label(request: web.Request, conv_id, label) -> web.Response:
    """Adds a label to a conversation

    Adds a label to a conversation, you can search and organize your conversations based on these labels OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the label is added
    :type conv_id: str
    :param label: The actual label 
    :type label: str

    """
    return web.Response(status=200)


async def create_community_conversation(request: web.Request, topic, description=None, participants=None) -> web.Response:
    """Creates a community conversation

    Creates a community. Communities are open conversations that anyone in a Circuit domain (tenant) can join without having to be added by another user. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param topic: An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    :type topic: str
    :param description: An optional description for the community conversation
    :type description: str
    :param participants: list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added
    :type participants: List[str]

    """
    return web.Response(status=200)


async def create_direct_conversation(request: web.Request, participant) -> web.Response:
    """Creates a 1-to-1 conversation

    Creates a 1-to-1 conversation between the authenticated user and the user with the provided userId. In case there is already an existing 1-to-1 conversation between these users, the endpoint returns the existing conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param participant: The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address
    :type participant: str

    """
    return web.Response(status=200)


async def create_group_conversation(request: web.Request, participants, topic=None) -> web.Response:
    """Creates a group conversation

    Creates a group conversation between three or more users. The authenticated user is directly added to this conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param participants: A list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added
    :type participants: List[str]
    :param topic: An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    :type topic: str

    """
    return web.Response(status=200)


async def delete_favorite(request: web.Request, conv_id) -> web.Response:
    """Removes a conversation from favorites

    Removes a conversation from favorites. Favorites can be displayed in a separate side tab inside of the Circuit client to have a better overview of important conversations. OauthScopes: WRITE_CONVERSATIONS

    :param conv_id: The ID of the conversation which will be unmarked as favorite
    :type conv_id: str

    """
    return web.Response(status=200)


async def delete_text_item(request: web.Request, conv_id, item_id) -> web.Response:
    """Deletes a message from a conversation

    Marks a message in the given conversation as deleted. Deleted messages are still part of the conversation, but their content is no more visible. This operation can only be performed on behalf of the message&#39;s creator. OauthScopes: WRITE_CONVERSATIONS, DELETE_CONVERSATIONS_CONTENT

    :param conv_id: The ID of the conversation to which the item belongs
    :type conv_id: str
    :param item_id: The ID of the item that will be deleted
    :type item_id: str

    """
    return web.Response(status=200)


async def flag_item(request: web.Request, conv_id, item_id, item_creation_time=None, parent_id=None) -> web.Response:
    """Adds a flag to a message in a conversation

    Adds a flag to the given message in the given conversation. OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the item belongs
    :type conv_id: str
    :param item_id: The ID of the item that will be flagged
    :type item_id: str
    :param item_creation_time: The time when the item was created
    :type item_creation_time: str
    :param parent_id: The ID of the item&#39;s parent
    :type parent_id: str

    """
    return web.Response(status=200)


async def get_community_conversations(request: web.Request, sort=None, order=None, include_own=None, start_index=None, results=None) -> web.Response:
    """Gets a list of communities

    Gets a list of communities. This endpoint can be used to explore the communities the authenticated user could join. OauthScopes: READ_CONVERSATIONS

    :param sort: Defines the type of sorting for the community conversations (default is alphabetical)
    :type sort: str
    :param order: Defines the ordering of the conversations (default is ascending)
    :type order: str
    :param include_own: If set to false only conversations are returned where the user is no member of, otherwise all community conversations are returned
    :type include_own: bool
    :param start_index: The index of the conversation that is the first one that has to be returned. E.g. if a request starts with startIndex 40 and results 20 the conversations 40 to 60 are returned
    :type start_index: 
    :param results: The maximum number of returned results (default 25). The maximum allowed value is 100.
    :type results: 

    """
    return web.Response(status=200)


async def get_conversation_items(request: web.Request, conv_id, mod_time=None, direction=None, results=None) -> web.Response:
    """Gets a list of conversation items

    Gets a list of conversation items. OauthScopes: READ_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the items belong
    :type conv_id: str
    :param mod_time: The modification time of the item in UTC format. During the query the items before (default) or after this timestamps are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified items are returned
    :type mod_time: str
    :param direction: The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER
    :type direction: str
    :param results: The maximum number of returned results (default 25). The maximum allowed value is 100.
    :type results: 

    """
    mod_time = util.deserialize_datetime(mod_time)
    return web.Response(status=200)


async def get_conversationby_id(request: web.Request, conv_id) -> web.Response:
    """Gets a conversation

    Gets a conversation based on the given ID. OauthScopes: READ_CONVERSATIONS

    :param conv_id: The ID of the conversation which should be updated
    :type conv_id: str

    """
    return web.Response(status=200)


async def get_conversations(request: web.Request, mod_time=None, direction=None, results=None) -> web.Response:
    """Gets a list of conversations

    Gets a list of conversations and communities the authenticated user participates in. OauthScopes: READ_CONVERSATIONS

    :param mod_time: The modification time of the conversation in UTC format. During the query the conversations before (&lt;i&gt;default&lt;/i&gt;) or after this timestamp are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified conversations are returned
    :type mod_time: str
    :param direction: The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER
    :type direction: str
    :param results: The maximum number of returned results (default 25). The maximum allowed value is 100.
    :type results: 

    """
    mod_time = util.deserialize_datetime(mod_time)
    return web.Response(status=200)


async def get_conversations_by_id(request: web.Request, conv_ids) -> web.Response:
    """Gets conversations

    Gets conversation based on the given IDs. OauthScopes: READ_CONVERSATIONS

    :param conv_ids: The array of IDs of the conversations which should be retrieved
    :type conv_ids: List[str]

    """
    return web.Response(status=200)


async def get_conversations_by_label(request: web.Request, label_id, next_page_pointer=None, page_size=None) -> web.Response:
    """Returns conversations with a certain label

    Returns conversations with matching labels and paginated  OauthScopes: READ_CONVERSATIONS

    :param label_id: Id of the label to look for
    :type label_id: str
    :param next_page_pointer: Pointer to the next page of conversations if there are any
    :type next_page_pointer: str
    :param page_size: Numbers of max conversations per page
    :type page_size: 

    """
    return web.Response(status=200)


async def get_direct_conversation(request: web.Request, participant) -> web.Response:
    """Checks for a 1-to-1 conversation

    Checks if a 1-to-1 conversation between the authenticated user and the user with the provided userId exists. OauthScopes: READ_CONVERSATIONS

    :param participant: The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address
    :type participant: str

    """
    return web.Response(status=200)


async def get_favorite_conversations(request: web.Request, ) -> web.Response:
    """Gets favorite conversations

    Gets the conversationIds which are marked as favorites. OauthScopes: READ_CONVERSATIONS


    """
    return web.Response(status=200)


async def get_flag_item(request: web.Request, conv_id) -> web.Response:
    """Gets a list of the flagged messages of a conversation

    Gets a list of all the flagged messages in the given conversation. OauthScopes: READ_CONVERSATIONS, ORGANIZE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the item belongs
    :type conv_id: str

    """
    return web.Response(status=200)


async def get_flag_item_conv(request: web.Request, ) -> web.Response:
    """Gets a list of the flagged messages

    Gets a list of all the messages the authenticated user has flagged. This endpoint should be used carefully in case where the authenticated user has a lot of flagged messages. OauthScopes: READ_CONVERSATIONS


    """
    return web.Response(status=200)


async def get_join_details(request: web.Request, conv_id) -> web.Response:
    """Gets the conference details of a conversation

    Gets the conference details of the given conversation. Conference details include the URL, which is used to join the conference through a web or mobile application, as well as the dial-in phone numbers and conference PIN, which are used to join the conference by phone. OauthScopes: READ_CONVERSATIONS

    :param conv_id: The ID of the conversation for which the join details should be returned
    :type conv_id: str

    """
    return web.Response(status=200)


async def get_join_details_multiple(request: web.Request, conv_ids) -> web.Response:
    """Gets the conference details for multiple conversations

    Gets the conference details of the given conversations. Conference details include the URL, which is used to join the conference through a web or mobile application, as well as the dial-in phone numbers and conference PIN, which are used to join the conference by phone. OauthScopes: READ_CONVERSATIONS

    :param conv_ids: An array of IDs of the conversations for which the join details should be returned
    :type conv_ids: List[str]

    """
    return web.Response(status=200)


async def get_participants_by_conv_id(request: web.Request, conv_id, page_size, name=None, type=None, search_pointer=None) -> web.Response:
    """Performs a list of participants

    Performs a search for participants. The max number of participants is configurable. If more participants are available a search pointer is returned for consecutive calls. OauthScopes: READ_CONVERSATIONS

    :param conv_id: The id of the conversation the participants are searched for.
    :type conv_id: str
    :param page_size: The page size of the hit list
    :type page_size: 
    :param name: Part of name to filter the results
    :type name: str
    :param type: Type of participant to filter the results
    :type type: str
    :param search_pointer: Pointer for paged output. Add to consecutive request to get next page
    :type search_pointer: str

    """
    return web.Response(status=200)


async def get_pinned_conversations(request: web.Request, conv_id) -> web.Response:
    """Returns pinned topics of a conversation

    Returns pinned topics of a conversation OauthScopes: READ_CONVERSATIONS

    :param conv_id: ID of the conversation
    :type conv_id: str

    """
    return web.Response(status=200)


async def get_single_conversationtem(request: web.Request, item_id) -> web.Response:
    """Returns a text item

    Returns a text item for a given item id OauthScopes: READ_CONVERSATIONS

    :param item_id: The ID of the item that will be returned
    :type item_id: str

    """
    return web.Response(status=200)


async def join_community_conversation(request: web.Request, conv_id) -> web.Response:
    """Adds the authenticated user to a community

    Adds the authenticated user to the given community (i.e., allows the user to join this community). Contrary to the operation of adding a new participant, this operation can only be performed by a user who is not yet a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation which the user will join
    :type conv_id: str

    """
    return web.Response(status=200)


async def like_item(request: web.Request, conv_id, item_id) -> web.Response:
    """Adds a \&quot;like\&quot; to a message

    Adds a \&quot;like\&quot; to the given message in the given conversation OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

    :param conv_id: The ID of the conversation to which the item belongs
    :type conv_id: str
    :param item_id: The ID of the item that will be liked
    :type item_id: str

    """
    return web.Response(status=200)


async def moderate_conversation(request: web.Request, conv_id) -> web.Response:
    """Set conversation moderated

    Set a conversation in moderatd mode. Moderators can be added and removed OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

    :param conv_id: The ID of the conversation which will be set to moderated state
    :type conv_id: str

    """
    return web.Response(status=200)


async def pin_a_conversation(request: web.Request, conv_id, item_id) -> web.Response:
    """Pins a topic of a conversation

    Pins a topic of a conversation OauthScopes: READ_CONVERSATIONS

    :param conv_id: The ID of the conversation
    :type conv_id: str
    :param item_id: The ID of the topic
    :type item_id: str

    """
    return web.Response(status=200)


async def remove_label(request: web.Request, label_id) -> web.Response:
    """Remove a user label

    Remove a label from the list of user labels OauthScopes: WRITE_USER_PROFILE, ORGANIZE_CONVERSATIONS

    :param label_id: The label value to remove, either the unique ID or the label value
    :type label_id: str

    """
    return web.Response(status=200)


async def remove_moderators(request: web.Request, conv_id, moderators) -> web.Response:
    """Remove moderators

    Removes a list of moderators from a conversation OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

    :param conv_id: The ID of the conversation where the moderators are removed
    :type conv_id: str
    :param moderators: The list of moderator ids to remove
    :type moderators: List[str]

    """
    return web.Response(status=200)


async def remove_participant_community(request: web.Request, conv_id, participants) -> web.Response:
    """Removes participants from a community

    Removes one or more participants from the given community. The last participant of a community cannot be removed. This operation can only be performed by a user who is already a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation from which the participant have to be removed
    :type conv_id: str
    :param participants: The IDs or the unique email addresses of the Circuit users that have to be removed
    :type participants: List[str]

    """
    return web.Response(status=200)


async def remove_participant_group(request: web.Request, conv_id, participants) -> web.Response:
    """Removes participants from a group conversation

    Removes one or more participants from the given group conversation. The last participant of a group conversation cannot be removed. This operation can only be performed on behalf of a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation from which the participant have to be removed
    :type conv_id: str
    :param participants: The IDs or the unique email addresses of the Circuit users that have to be removed
    :type participants: List[str]

    """
    return web.Response(status=200)


async def resolve_invitation_token(request: web.Request, token) -> web.Response:
    """Resolves an invite token to a conversation

    Resolves an invite token to a conversation OauthScopes: READ_CONVERSATIONS

    :param token: The invite token to resolve
    :type token: str

    """
    return web.Response(status=200)


async def search_conversations(request: web.Request, term, include_item_ids=None, scope=None) -> web.Response:
    """Performs a conversation search

    Performs a search for conversation content. A maximum of 100 conversations is returned. If you hit this limit you should refine the search term. OauthScopes: READ_CONVERSATIONS

    :param term: The search term
    :type term: str
    :param include_item_ids: Optional parameter to specify if a deep or normal search is executed. In a deep search all matching item IDs inside every conversation are returned (up to a maximum of 100). For a normal search only the conversation IDs are returned. Default is a normal search (without item IDs).
    :type include_item_ids: bool
    :param scope: The search scope, FILES||PEOPLE||MEMBERS||MESSAGES||SENTBY||ALL||CONVERSATIONS||LABEL||FILTER
    :type scope: str

    """
    return web.Response(status=200)


async def un_flag_item(request: web.Request, conv_id, item_id) -> web.Response:
    """Removes the flag from a message

    Removes the flag from a given message that is posted to the given conversation. OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

    :param conv_id: The ID of the conversation to which the item belongs
    :type conv_id: str
    :param item_id: The ID of the item that will be flagged
    :type item_id: str

    """
    return web.Response(status=200)


async def un_pin_a_conversation(request: web.Request, conv_id, item_id) -> web.Response:
    """Unpins a topic of a conversation

    Unpins a topic of a conversation OauthScopes: READ_CONVERSATIONS

    :param conv_id: The ID of the conversation
    :type conv_id: str
    :param item_id: The ID of the topic
    :type item_id: str

    """
    return web.Response(status=200)


async def unassign_label(request: web.Request, conv_id, label_id) -> web.Response:
    """Removes a label from a conversation

    Removes a label from a conversation, you can search and organize your conversations based on these labels OauthScopes: WRITE_CONVERSATIONS

    :param conv_id: The ID of the conversation from which the label is removed
    :type conv_id: str
    :param label_id: The actual label 
    :type label_id: str

    """
    return web.Response(status=200)


async def undo_archive_conversation(request: web.Request, conv_id) -> web.Response:
    """Unmute conversation

    The conversation will no longer be archived but active again OauthScopes: WRITE_CONVERSATIONS

    :param conv_id: The ID of the conversation which will be unmarked as muted
    :type conv_id: str

    """
    return web.Response(status=200)


async def unlike_item(request: web.Request, conv_id, item_id) -> web.Response:
    """Removes a \&quot;like\&quot; from a message

    Removes a \&quot;like\&quot; from the given message in the given conversation OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

    :param conv_id: The ID of the conversation to which the item belongs
    :type conv_id: str
    :param item_id: The ID of the item that will be unliked
    :type item_id: str

    """
    return web.Response(status=200)


async def unmoderate_conversation(request: web.Request, conv_id) -> web.Response:
    """Set conversation unmoderated

    Set a conversation to unmoderatd mode OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

    :param conv_id: The ID of the conversation which will be set to unmoderated state
    :type conv_id: str

    """
    return web.Response(status=200)


async def update_conversation_community(request: web.Request, conv_id, description=None, topic=None) -> web.Response:
    """Updates the information of a community

    Updates the information of the given community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation which should be updated
    :type conv_id: str
    :param description: An optional description for the community conversation
    :type description: str
    :param topic: An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    :type topic: str

    """
    return web.Response(status=200)


async def update_conversation_group(request: web.Request, conv_id, topic=None) -> web.Response:
    """Updates the information of a group conversation

    Updates the information of the given group conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

    :param conv_id: The ID of the conversation which should be updated
    :type conv_id: str
    :param topic: An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    :type topic: str

    """
    return web.Response(status=200)


async def update_profile(request: web.Request, firstname=None, job_title=None, lastname=None, locale=None) -> web.Response:
    """Updates the user profile

    Updates the user profile of the authenticated user OauthScopes: WRITE_USER_PROFILE

    :param firstname: The new firstname of the user
    :type firstname: str
    :param job_title: The new job title of the user
    :type job_title: str
    :param lastname: The new lastname of the user
    :type lastname: str
    :param locale: The new locale of the user. One of EN_US, DE_DE, EN_GB, ES_ES, FR_FR, IT_IT, RU_RU, ZH_HANS_CN.
    :type locale: str

    """
    return web.Response(status=200)


async def update_text_item(request: web.Request, conv_id, item_id, attachments=None, content=None, form_meta_data=None, subject=None) -> web.Response:
    """Updates a message

    Updates the content or subject of the existing message. Only the creator of the message is allowed to perform this operation. OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

    :param conv_id: The ID of the conversation to which the item belongs
    :type conv_id: str
    :param item_id: The ID of the item to update
    :type item_id: str
    :param attachments: A comma separated list of attachment IDs from the file API.
    :type attachments: List[str]
    :param content: The actual content of the item
    :type content: str
    :param form_meta_data: The form meta data of the new text item
    :type form_meta_data: str
    :param subject: The subject (headline) of the new text item
    :type subject: str

    """
    return web.Response(status=200)
