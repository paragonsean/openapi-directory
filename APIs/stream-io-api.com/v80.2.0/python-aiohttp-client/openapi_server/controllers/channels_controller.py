from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.channel_get_or_create_request import ChannelGetOrCreateRequest
from openapi_server.models.channel_state_response import ChannelStateResponse
from openapi_server.models.channel_stop_watching_request import ChannelStopWatchingRequest
from openapi_server.models.channels_response import ChannelsResponse
from openapi_server.models.delete_channel_response import DeleteChannelResponse
from openapi_server.models.delete_channels_request import DeleteChannelsRequest
from openapi_server.models.delete_channels_response import DeleteChannelsResponse
from openapi_server.models.export_channels_request import ExportChannelsRequest
from openapi_server.models.export_channels_response import ExportChannelsResponse
from openapi_server.models.get_export_channels_status_response import GetExportChannelsStatusResponse
from openapi_server.models.hide_channel_request import HideChannelRequest
from openapi_server.models.hide_channel_response import HideChannelResponse
from openapi_server.models.mark_channels_read_request import MarkChannelsReadRequest
from openapi_server.models.mark_read_request import MarkReadRequest
from openapi_server.models.mark_read_response import MarkReadResponse
from openapi_server.models.mark_unread_request import MarkUnreadRequest
from openapi_server.models.members_response import MembersResponse
from openapi_server.models.mute_channel_request import MuteChannelRequest
from openapi_server.models.mute_channel_response import MuteChannelResponse
from openapi_server.models.query_channels_request import QueryChannelsRequest
from openapi_server.models.query_members_request import QueryMembersRequest
from openapi_server.models.response import Response
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.show_channel_request import ShowChannelRequest
from openapi_server.models.show_channel_response import ShowChannelResponse
from openapi_server.models.stop_watching_response import StopWatchingResponse
from openapi_server.models.sync_request import SyncRequest
from openapi_server.models.sync_response import SyncResponse
from openapi_server.models.truncate_channel_request import TruncateChannelRequest
from openapi_server.models.truncate_channel_response import TruncateChannelResponse
from openapi_server.models.unmute_channel_request import UnmuteChannelRequest
from openapi_server.models.unmute_response import UnmuteResponse
from openapi_server.models.update_channel_partial_request import UpdateChannelPartialRequest
from openapi_server.models.update_channel_partial_response import UpdateChannelPartialResponse
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse
from openapi_server import util


async def delete_channel(request: web.Request, type, id, hard_delete=None) -> web.Response:
    """Delete channel

    Deletes channel  Sends events: - channel.deleted  Required permissions: - DeleteChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param hard_delete: 
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def delete_channels(request: web.Request, body) -> web.Response:
    """Deletes channels asynchronously

    Allows to delete several channels at once asynchronously  Sends events: - channel.deleted  Required permissions: - DeleteChannel 

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def export_channels(request: web.Request, body) -> web.Response:
    """Export channels

    Exports channel data to JSON file 

    :param body: 
    :type body: dict | bytes

    """
    body = ExportChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def get_export_channels_status(request: web.Request, id) -> web.Response:
    """Export channels status

     

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_or_create_channel_type1(request: web.Request, type, body, client_id=None, connection_id=None) -> web.Response:
    """Get or create channel (type)

    This method creates a channel or returns an existing one with matching attributes  Sends events: - channel.created - member.added - member.removed - member.updated - user.watching.start 

    :param type: 
    :type type: str
    :param body: 
    :type body: dict | bytes
    :param client_id: 
    :type client_id: str
    :param connection_id: 
    :type connection_id: str

    """
    body = ChannelGetOrCreateRequest.from_dict(body)
    return web.Response(status=200)


async def get_or_create_channel_type_id0(request: web.Request, type, id, body, client_id=None, connection_id=None) -> web.Response:
    """Get or create channel (type, id)

    This method creates a channel or returns an existing one with matching attributes  Sends events: - channel.created - member.added - member.removed - member.updated - user.watching.start 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param client_id: 
    :type client_id: str
    :param connection_id: 
    :type connection_id: str

    """
    body = ChannelGetOrCreateRequest.from_dict(body)
    return web.Response(status=200)


async def hide_channel(request: web.Request, type, id, body) -> web.Response:
    """Hide channel

    Marks channel as hidden for current user  Sends events: - channel.hidden  Required permissions: - ReadChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HideChannelRequest.from_dict(body)
    return web.Response(status=200)


async def mark_channels_read(request: web.Request, body) -> web.Response:
    """Mark channels as read

    Marks channels as read up to the specific message. If no channels is given, mark all channel as read  Sends events: - message.read  Required permissions: - ReadChannel 

    :param body: 
    :type body: dict | bytes

    """
    body = MarkChannelsReadRequest.from_dict(body)
    return web.Response(status=200)


async def mark_read(request: web.Request, type, id, body) -> web.Response:
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


async def mark_unread(request: web.Request, type, id, body) -> web.Response:
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


async def mute_channel(request: web.Request, body) -> web.Response:
    """Mute channel

    Mutes channel for user  Sends events: - channel.muted  Required permissions: - MuteChannel 

    :param body: 
    :type body: dict | bytes

    """
    body = MuteChannelRequest.from_dict(body)
    return web.Response(status=200)


async def query_channels(request: web.Request, body, client_id=None, connection_id=None) -> web.Response:
    """Query channels

    Query channels with filter query  Required permissions: - ReadChannel 

    :param body: Query Channels Request
    :type body: dict | bytes
    :param client_id: 
    :type client_id: str
    :param connection_id: 
    :type connection_id: str

    """
    body = QueryChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def query_members(request: web.Request, payload=None) -> web.Response:
    """Query members

    Find and filter channel members  Required permissions: - ReadChannel 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def search(request: web.Request, payload=None) -> web.Response:
    """Search messages

    Search messages across channels  Required permissions: - ReadChannel 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def show_channel(request: web.Request, type, id, body) -> web.Response:
    """Show channel

    Shows previously hidden channel  Sends events: - channel.visible 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShowChannelRequest.from_dict(body)
    return web.Response(status=200)


async def stop_watching_channel(request: web.Request, type, id, body, client_id=None, connection_id=None) -> web.Response:
    """Stop watching channel

    Call this method to stop receiving channel events  Sends events: - user.watching.stop 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param client_id: 
    :type client_id: str
    :param connection_id: 
    :type connection_id: str

    """
    body = ChannelStopWatchingRequest.from_dict(body)
    return web.Response(status=200)


async def sync(request: web.Request, body, with_inaccessible_cids=None, watch=None, client_id=None, connection_id=None) -> web.Response:
    """Sync

    Returns all events happened since client disconnect in specified channels  Required permissions: - ReadChannel 

    :param body: 
    :type body: dict | bytes
    :param with_inaccessible_cids: 
    :type with_inaccessible_cids: bool
    :param watch: 
    :type watch: bool
    :param client_id: 
    :type client_id: str
    :param connection_id: 
    :type connection_id: str

    """
    body = SyncRequest.from_dict(body)
    return web.Response(status=200)


async def truncate_channel(request: web.Request, type, id, body) -> web.Response:
    """Truncate channel

    Truncates channel  Sends events: - channel.truncated  Required permissions: - DeleteChannel - TruncateChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TruncateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def unmute_channel(request: web.Request, body) -> web.Response:
    """Unmute channel

    Unmutes channel for user  Sends events: - channel.unmuted  Required permissions: - MuteChannel 

    :param body: 
    :type body: dict | bytes

    """
    body = UnmuteChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel(request: web.Request, type, id, body) -> web.Response:
    """Update channel

    Change channel data  Sends events: - channel.updated - member.added - member.removed - member.updated - message.new  Required permissions: - AddOwnChannelMembership - RemoveOwnChannelMembership - UpdateChannel - UpdateChannelCooldown - UpdateChannelFrozen - UpdateChannelMembers 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: Channel update request
    :type body: dict | bytes

    """
    body = UpdateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel_partial(request: web.Request, type, id, body) -> web.Response:
    """Partially update channel

    Updates certain fields of the channel  Sends events: - channel.updated  Required permissions: - UpdateChannel - UpdateChannelCooldown - UpdateChannelFrozen 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateChannelPartialRequest.from_dict(body)
    return web.Response(status=200)
