from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.file_delete_response import FileDeleteResponse
from openapi_server.models.file_upload_response import FileUploadResponse
from openapi_server.models.flag_request import FlagRequest
from openapi_server.models.flag_response import FlagResponse
from openapi_server.models.get_many_messages_response import GetManyMessagesResponse
from openapi_server.models.get_og_response import GetOGResponse
from openapi_server.models.get_reactions_response import GetReactionsResponse
from openapi_server.models.get_replies_response import GetRepliesResponse
from openapi_server.models.image_size_request import ImageSizeRequest
from openapi_server.models.image_upload_response import ImageUploadResponse
from openapi_server.models.mark_channels_read_request import MarkChannelsReadRequest
from openapi_server.models.mark_read_request import MarkReadRequest
from openapi_server.models.mark_read_response import MarkReadResponse
from openapi_server.models.mark_unread_request import MarkUnreadRequest
from openapi_server.models.message_action_request import MessageActionRequest
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.message_with_pending_metadata_response import MessageWithPendingMetadataResponse
from openapi_server.models.only_user_id_request import OnlyUserIDRequest
from openapi_server.models.query_message_flags_request import QueryMessageFlagsRequest
from openapi_server.models.query_message_flags_response import QueryMessageFlagsResponse
from openapi_server.models.reaction_removal_response import ReactionRemovalResponse
from openapi_server.models.reaction_response import ReactionResponse
from openapi_server.models.response import Response
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.send_message_request import SendMessageRequest
from openapi_server.models.send_reaction_request import SendReactionRequest
from openapi_server.models.translate_message_request import TranslateMessageRequest
from openapi_server.models.update_message_partial_request import UpdateMessagePartialRequest
from openapi_server.models.update_message_request import UpdateMessageRequest
from openapi_server import util


async def delete_file(request: web.Request, type, id, url=None) -> web.Response:
    """Delete file

    Deletes previously uploaded file  Required permissions: - DeleteAttachment 

    :param type: Automatically added
    :type type: str
    :param id: Automatically added
    :type id: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def delete_image(request: web.Request, type, id, url=None) -> web.Response:
    """Delete image

    Deletes previously uploaded image  Required permissions: - DeleteAttachment 

    :param type: Automatically added
    :type type: str
    :param id: Automatically added
    :type id: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def delete_message(request: web.Request, id, hard=None) -> web.Response:
    """Delete message

    Deletes message  Sends events: - message.deleted  Required permissions: - DeleteMessage 

    :param id: 
    :type id: str
    :param hard: 
    :type hard: bool

    """
    return web.Response(status=200)


async def delete_reaction(request: web.Request, id, type, user_id=None) -> web.Response:
    """Delete reaction

    Removes user reaction from the message  Sends events: - reaction.deleted  Required permissions: - DeleteReaction 

    :param id: 
    :type id: str
    :param type: 
    :type type: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def flag_0(request: web.Request, body) -> web.Response:
    """Flag

    Reports message or user for review by moderators  Sends events: - message.flagged - user.flagged  Required permissions: - FlagMessage - FlagUser 

    :param body: 
    :type body: dict | bytes

    """
    body = FlagRequest.from_dict(body)
    return web.Response(status=200)


async def get_many_messages(request: web.Request, type, id, ids=None) -> web.Response:
    """Get many messages

    Returns list messages found by IDs  Required permissions: - ReadChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param ids: 
    :type ids: List[str]

    """
    return web.Response(status=200)


async def get_message(request: web.Request, id) -> web.Response:
    """Get message

    Returns message by ID  Required permissions: - ReadChannel 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_og(request: web.Request, url=None) -> web.Response:
    """Get OG

    Get an OpenGraph attachment for a link 

    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def get_reactions(request: web.Request, id, limit=None, offset=None) -> web.Response:
    """Get reactions

    Returns list of reactions of specific message  Required permissions: - ReadChannel 

    :param id: 
    :type id: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_replies(request: web.Request, parent_id, id_gte=None, id_gt=None, id_lte=None, id_lt=None, created_at_after_or_equal=None, created_at_after=None, created_at_before_or_equal=None, created_at_before=None, id_around=None, created_at_around=None) -> web.Response:
    """Get replies

    Returns replies (thread) of the message  Required permissions: - ReadChannel 

    :param parent_id: 
    :type parent_id: str
    :param id_gte: 
    :type id_gte: str
    :param id_gt: 
    :type id_gt: str
    :param id_lte: 
    :type id_lte: str
    :param id_lt: 
    :type id_lt: str
    :param created_at_after_or_equal: 
    :type created_at_after_or_equal: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_before_or_equal: 
    :type created_at_before_or_equal: str
    :param created_at_before: 
    :type created_at_before: str
    :param id_around: 
    :type id_around: str
    :param created_at_around: 
    :type created_at_around: str

    """
    created_at_after_or_equal = util.deserialize_datetime(created_at_after_or_equal)
    created_at_after = util.deserialize_datetime(created_at_after)
    created_at_before_or_equal = util.deserialize_datetime(created_at_before_or_equal)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_around = util.deserialize_datetime(created_at_around)
    return web.Response(status=200)


async def mark_channels_read_0(request: web.Request, body) -> web.Response:
    """Mark channels as read

    Marks channels as read up to the specific message. If no channels is given, mark all channel as read  Sends events: - message.read  Required permissions: - ReadChannel 

    :param body: 
    :type body: dict | bytes

    """
    body = MarkChannelsReadRequest.from_dict(body)
    return web.Response(status=200)


async def mark_read_0(request: web.Request, type, id, body) -> web.Response:
    """Mark read

    Marks channel as read up to the specific message  Sends events: - message.read  Required permissions: - ReadChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MarkReadRequest.from_dict(body)
    return web.Response(status=200)


async def mark_unread_0(request: web.Request, type, id, body) -> web.Response:
    """Mark unread

    Marks channel as unread from a specific message  Required permissions: - ReadChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MarkUnreadRequest.from_dict(body)
    return web.Response(status=200)


async def query_message_flags(request: web.Request, payload=None) -> web.Response:
    """Query Message Flags

    Find and filter message flags  Required permissions: - ReadMessageFlags 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def run_message_action(request: web.Request, id, body) -> web.Response:
    """Run message command action

    Executes message command action with given parameters  Sends events: - message.new  Required permissions: - RunMessageAction 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MessageActionRequest.from_dict(body)
    return web.Response(status=200)


async def search_0(request: web.Request, payload=None) -> web.Response:
    """Search messages

    Search messages across channels  Required permissions: - ReadChannel 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def send_message(request: web.Request, type, id, body) -> web.Response:
    """Send new message

    Sends new message to the specified channel  Sends events: - message.new - message.updated  Required permissions: - AddLinks - CreateMessage - PinMessage - SkipChannelCooldown - SkipMessageModeration - UseFrozenChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: Send Message Request
    :type body: dict | bytes

    """
    body = SendMessageRequest.from_dict(body)
    return web.Response(status=200)


async def send_reaction(request: web.Request, id, body) -> web.Response:
    """Send reaction

    Sends reaction to specified message  Sends events: - reaction.new - reaction.updated  Required permissions: - CreateReaction - UseFrozenChannel 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendReactionRequest.from_dict(body)
    return web.Response(status=200)


async def translate_message(request: web.Request, id, body) -> web.Response:
    """Translate message

    Translates message to a given language using automated translation software  Sends events: - message.updated  Required permissions: - ReadChannel 

    :param id: Automatically added
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TranslateMessageRequest.from_dict(body)
    return web.Response(status=200)


async def unflag_0(request: web.Request, body) -> web.Response:
    """Unflag

    Removes previously created user or message flag  Required permissions: - FlagMessage - FlagUser 

    :param body: 
    :type body: dict | bytes

    """
    body = FlagRequest.from_dict(body)
    return web.Response(status=200)


async def update_message(request: web.Request, id, body) -> web.Response:
    """Update message

    Updates message with new data  Sends events: - message.updated  Required permissions: - AddLinks - PinMessage - SkipMessageModeration - UpdateMessage 

    :param id: Automatically added
    :type id: str
    :param body: Update Message Request
    :type body: dict | bytes

    """
    body = UpdateMessageRequest.from_dict(body)
    return web.Response(status=200)


async def update_message_partial(request: web.Request, id, body) -> web.Response:
    """Partially message update

    Updates certain fields of the message  Sends events: - message.updated  Required permissions: - AddLinks - PinMessage - SkipMessageModeration - UpdateMessage 

    :param id: Automatically added
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateMessagePartialRequest.from_dict(body)
    return web.Response(status=200)


async def upload_file(request: web.Request, type, id, file=None, user=None) -> web.Response:
    """Upload file

    Uploads file  Required permissions: - UploadAttachment 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param file: file field
    :type file: str
    :param user: 
    :type user: dict | bytes

    """
    user = OnlyUserIDRequest.from_dict(user)
    return web.Response(status=200)


async def upload_image(request: web.Request, type, id, file=None, upload_sizes=None, user=None) -> web.Response:
    """Upload image

    Uploads image  Required permissions: - UploadAttachment 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param file: 
    :type file: str
    :param upload_sizes: field with JSON-encoded array of image size configurations
    :type upload_sizes: list | bytes
    :param user: 
    :type user: dict | bytes

    """
    upload_sizes = [ImageSizeRequest.from_dict(d) for d in upload_sizes]
    user = OnlyUserIDRequest.from_dict(user)
    return web.Response(status=200)
