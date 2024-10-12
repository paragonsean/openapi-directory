from typing import List, Dict
from aiohttp import web

from openapi_server.models.buffer_request_dto import BufferRequestDto
from openapi_server.models.group_info_dto import GroupInfoDto
from openapi_server.models.ignore_wait_request_dto import IgnoreWaitRequestDto
from openapi_server.models.join_group_request_dto import JoinGroupRequestDto
from openapi_server.models.move_playlist_item_request_dto import MovePlaylistItemRequestDto
from openapi_server.models.new_group_request_dto import NewGroupRequestDto
from openapi_server.models.next_item_request_dto import NextItemRequestDto
from openapi_server.models.ping_request_dto import PingRequestDto
from openapi_server.models.play_request_dto import PlayRequestDto
from openapi_server.models.previous_item_request_dto import PreviousItemRequestDto
from openapi_server.models.queue_request_dto import QueueRequestDto
from openapi_server.models.ready_request_dto import ReadyRequestDto
from openapi_server.models.remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto
from openapi_server.models.seek_request_dto import SeekRequestDto
from openapi_server.models.set_playlist_item_request_dto import SetPlaylistItemRequestDto
from openapi_server.models.set_repeat_mode_request_dto import SetRepeatModeRequestDto
from openapi_server.models.set_shuffle_mode_request_dto import SetShuffleModeRequestDto
from openapi_server import util


async def sync_play_buffering(request: web.Request, body) -> web.Response:
    """Notify SyncPlay group that member is buffering.

    

    :param body: The player status.
    :type body: dict | bytes

    """
    body = BufferRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_create_group(request: web.Request, body) -> web.Response:
    """Create a new SyncPlay group.

    

    :param body: The settings of the new group.
    :type body: dict | bytes

    """
    body = NewGroupRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_get_groups(request: web.Request, ) -> web.Response:
    """Gets all SyncPlay groups.

    


    """
    return web.Response(status=200)


async def sync_play_join_group(request: web.Request, body) -> web.Response:
    """Join an existing SyncPlay group.

    

    :param body: The group to join.
    :type body: dict | bytes

    """
    body = JoinGroupRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_leave_group(request: web.Request, ) -> web.Response:
    """Leave the joined SyncPlay group.

    


    """
    return web.Response(status=200)


async def sync_play_move_playlist_item(request: web.Request, body) -> web.Response:
    """Request to move an item in the playlist in SyncPlay group.

    

    :param body: The new position for the item.
    :type body: dict | bytes

    """
    body = MovePlaylistItemRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_next_item(request: web.Request, body) -> web.Response:
    """Request next item in SyncPlay group.

    

    :param body: The current item information.
    :type body: dict | bytes

    """
    body = NextItemRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_pause(request: web.Request, ) -> web.Response:
    """Request pause in SyncPlay group.

    


    """
    return web.Response(status=200)


async def sync_play_ping(request: web.Request, body) -> web.Response:
    """Update session ping.

    

    :param body: The new ping.
    :type body: dict | bytes

    """
    body = PingRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_previous_item(request: web.Request, body) -> web.Response:
    """Request previous item in SyncPlay group.

    

    :param body: The current item information.
    :type body: dict | bytes

    """
    body = PreviousItemRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_queue(request: web.Request, body) -> web.Response:
    """Request to queue items to the playlist of a SyncPlay group.

    

    :param body: The items to add.
    :type body: dict | bytes

    """
    body = QueueRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_ready(request: web.Request, body) -> web.Response:
    """Notify SyncPlay group that member is ready for playback.

    

    :param body: The player status.
    :type body: dict | bytes

    """
    body = ReadyRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_remove_from_playlist(request: web.Request, body) -> web.Response:
    """Request to remove items from the playlist in SyncPlay group.

    

    :param body: The items to remove.
    :type body: dict | bytes

    """
    body = RemoveFromPlaylistRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_seek(request: web.Request, body) -> web.Response:
    """Request seek in SyncPlay group.

    

    :param body: The new playback position.
    :type body: dict | bytes

    """
    body = SeekRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_set_ignore_wait(request: web.Request, body) -> web.Response:
    """Request SyncPlay group to ignore member during group-wait.

    

    :param body: The settings to set.
    :type body: dict | bytes

    """
    body = IgnoreWaitRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_set_new_queue(request: web.Request, body) -> web.Response:
    """Request to set new playlist in SyncPlay group.

    

    :param body: The new playlist to play in the group.
    :type body: dict | bytes

    """
    body = PlayRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_set_playlist_item(request: web.Request, body) -> web.Response:
    """Request to change playlist item in SyncPlay group.

    

    :param body: The new item to play.
    :type body: dict | bytes

    """
    body = SetPlaylistItemRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_set_repeat_mode(request: web.Request, body) -> web.Response:
    """Request to set repeat mode in SyncPlay group.

    

    :param body: The new repeat mode.
    :type body: dict | bytes

    """
    body = SetRepeatModeRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_set_shuffle_mode(request: web.Request, body) -> web.Response:
    """Request to set shuffle mode in SyncPlay group.

    

    :param body: The new shuffle mode.
    :type body: dict | bytes

    """
    body = SetShuffleModeRequestDto.from_dict(body)
    return web.Response(status=200)


async def sync_play_stop(request: web.Request, ) -> web.Response:
    """Request stop in SyncPlay group.

    


    """
    return web.Response(status=200)


async def sync_play_unpause(request: web.Request, ) -> web.Response:
    """Request unpause in SyncPlay group.

    


    """
    return web.Response(status=200)
