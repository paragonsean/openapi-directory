from typing import List, Dict
from aiohttp import web

from openapi_server.models.currently_playing_context_object import CurrentlyPlayingContextObject
from openapi_server.models.currently_playing_object import CurrentlyPlayingObject
from openapi_server.models.cursor_paging_play_history_object import CursorPagingPlayHistoryObject
from openapi_server.models.devices_object import DevicesObject
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.queue_object import QueueObject
from openapi_server.models.start_a_users_playback_request import StartAUsersPlaybackRequest
from openapi_server.models.transfer_a_users_playback_request import TransferAUsersPlaybackRequest
from openapi_server import util


async def add_to_queue(request: web.Request, uri, device_id=None) -> web.Response:
    """Add Item to Playback Queue 

    Add an item to the end of the user&#39;s current playback queue. 

    :param uri: 
    :type uri: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_a_users_available_devices(request: web.Request, ) -> web.Response:
    """Get Available Devices 

    Get information about a user’s available devices. 


    """
    return web.Response(status=200)


async def get_information_about_the_users_current_playback(request: web.Request, market=None, additional_types=None) -> web.Response:
    """Get Playback State 

    Get information about the user’s current playback state, including track or episode, progress, and active device. 

    :param market: 
    :type market: str
    :param additional_types: 
    :type additional_types: str

    """
    return web.Response(status=200)


async def get_queue(request: web.Request, ) -> web.Response:
    """Get the User&#39;s Queue 

    Get the list of objects that make up the user&#39;s queue. 


    """
    return web.Response(status=200)


async def get_recently_played(request: web.Request, limit=None, after=None, before=None) -> web.Response:
    """Get Recently Played Tracks 

    Get tracks from the current user&#39;s recently played tracks. _**Note**: Currently doesn&#39;t support podcast episodes._ 

    :param limit: 
    :type limit: int
    :param after: 
    :type after: int
    :param before: 
    :type before: int

    """
    return web.Response(status=200)


async def get_the_users_currently_playing_track(request: web.Request, market=None, additional_types=None) -> web.Response:
    """Get Currently Playing Track 

    Get the object currently being played on the user&#39;s Spotify account. 

    :param market: 
    :type market: str
    :param additional_types: 
    :type additional_types: str

    """
    return web.Response(status=200)


async def pause_a_users_playback(request: web.Request, device_id=None) -> web.Response:
    """Pause Playback 

    Pause playback on the user&#39;s account. 

    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def seek_to_position_in_currently_playing_track(request: web.Request, position_ms, device_id=None) -> web.Response:
    """Seek To Position 

    Seeks to the given position in the user’s currently playing track. 

    :param position_ms: 
    :type position_ms: int
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def set_repeat_mode_on_users_playback(request: web.Request, state, device_id=None) -> web.Response:
    """Set Repeat Mode 

    Set the repeat mode for the user&#39;s playback. Options are repeat-track, repeat-context, and off. 

    :param state: 
    :type state: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def set_volume_for_users_playback(request: web.Request, volume_percent, device_id=None) -> web.Response:
    """Set Playback Volume 

    Set the volume for the user’s current playback device. 

    :param volume_percent: 
    :type volume_percent: int
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def skip_users_playback_to_next_track(request: web.Request, device_id=None) -> web.Response:
    """Skip To Next 

    Skips to next track in the user’s queue. 

    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def skip_users_playback_to_previous_track(request: web.Request, device_id=None) -> web.Response:
    """Skip To Previous 

    Skips to previous track in the user’s queue. 

    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def start_a_users_playback(request: web.Request, device_id=None, body=None) -> web.Response:
    """Start/Resume Playback 

    Start a new context or resume current playback on the user&#39;s active device. 

    :param device_id: 
    :type device_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = StartAUsersPlaybackRequest.from_dict(body)
    return web.Response(status=200)


async def toggle_shuffle_for_users_playback(request: web.Request, state, device_id=None) -> web.Response:
    """Toggle Playback Shuffle 

    Toggle shuffle on or off for user’s playback. 

    :param state: 
    :type state: bool
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def transfer_a_users_playback(request: web.Request, body=None) -> web.Response:
    """Transfer Playback 

    Transfer playback to a new device and determine if it should start playing. 

    :param body: 
    :type body: dict | bytes

    """
    body = TransferAUsersPlaybackRequest.from_dict(body)
    return web.Response(status=200)
