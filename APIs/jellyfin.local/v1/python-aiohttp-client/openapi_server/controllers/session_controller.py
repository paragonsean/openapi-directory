from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_capabilities_dto import ClientCapabilitiesDto
from openapi_server.models.general_command import GeneralCommand
from openapi_server.models.general_command_type import GeneralCommandType
from openapi_server.models.name_id_pair import NameIdPair
from openapi_server.models.play_command import PlayCommand
from openapi_server.models.playstate_command import PlaystateCommand
from openapi_server.models.session_info import SessionInfo
from openapi_server import util


async def add_user_to_session(request: web.Request, session_id, user_id) -> web.Response:
    """Adds an additional user to a session.

    

    :param session_id: The session id.
    :type session_id: str
    :param user_id: The user id.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def display_content(request: web.Request, session_id, item_type, item_id, item_name) -> web.Response:
    """Instructs a session to browse to an item or view.

    

    :param session_id: The session Id.
    :type session_id: str
    :param item_type: The type of item to browse to.
    :type item_type: str
    :param item_id: The Id of the item.
    :type item_id: str
    :param item_name: The name of the item.
    :type item_name: str

    """
    return web.Response(status=200)


async def get_auth_providers(request: web.Request, ) -> web.Response:
    """Get all auth providers.

    


    """
    return web.Response(status=200)


async def get_password_reset_providers(request: web.Request, ) -> web.Response:
    """Get all password reset providers.

    


    """
    return web.Response(status=200)


async def get_sessions(request: web.Request, controllable_by_user_id=None, device_id=None, active_within_seconds=None) -> web.Response:
    """Gets a list of sessions.

    

    :param controllable_by_user_id: Filter by sessions that a given user is allowed to remote control.
    :type controllable_by_user_id: str
    :type controllable_by_user_id: str
    :param device_id: Filter by device Id.
    :type device_id: str
    :param active_within_seconds: Optional. Filter by sessions that were active in the last n seconds.
    :type active_within_seconds: int

    """
    return web.Response(status=200)


async def play(request: web.Request, session_id, play_command, item_ids, start_position_ticks=None) -> web.Response:
    """Instructs a session to play an item.

    

    :param session_id: The session id.
    :type session_id: str
    :param play_command: The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now.
    :type play_command: dict | bytes
    :param item_ids: The ids of the items to play, comma delimited.
    :type item_ids: List[str]
    :param start_position_ticks: The starting position of the first item.
    :type start_position_ticks: int

    """
    play_command = .from_dict(play_command)
    return web.Response(status=200)


async def post_capabilities(request: web.Request, id=None, playable_media_types=None, supported_commands=None, supports_media_control=None, supports_sync=None, supports_persistent_identifier=None) -> web.Response:
    """Updates capabilities for a device.

    

    :param id: The session id.
    :type id: str
    :param playable_media_types: A list of playable media types, comma delimited. Audio, Video, Book, Photo.
    :type playable_media_types: List[str]
    :param supported_commands: A list of supported remote control commands, comma delimited.
    :type supported_commands: list | bytes
    :param supports_media_control: Determines whether media can be played remotely..
    :type supports_media_control: bool
    :param supports_sync: Determines whether sync is supported.
    :type supports_sync: bool
    :param supports_persistent_identifier: Determines whether the device supports a unique identifier.
    :type supports_persistent_identifier: bool

    """
    supported_commands = [GeneralCommandType.from_dict(d) for d in supported_commands]
    return web.Response(status=200)


async def post_full_capabilities(request: web.Request, body, id=None) -> web.Response:
    """Updates capabilities for a device.

    

    :param body: The MediaBrowser.Model.Session.ClientCapabilities.
    :type body: dict | bytes
    :param id: The session id.
    :type id: str

    """
    body = ClientCapabilitiesDto.from_dict(body)
    return web.Response(status=200)


async def remove_user_from_session(request: web.Request, session_id, user_id) -> web.Response:
    """Removes an additional user from a session.

    

    :param session_id: The session id.
    :type session_id: str
    :param user_id: The user id.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def report_session_ended(request: web.Request, ) -> web.Response:
    """Reports that a session has ended.

    


    """
    return web.Response(status=200)


async def report_viewing(request: web.Request, item_id, session_id=None) -> web.Response:
    """Reports that a session is viewing an item.

    

    :param item_id: The item id.
    :type item_id: str
    :param session_id: The session id.
    :type session_id: str

    """
    return web.Response(status=200)


async def send_full_general_command(request: web.Request, session_id, body) -> web.Response:
    """Issues a full general command to a client.

    

    :param session_id: The session id.
    :type session_id: str
    :param body: The MediaBrowser.Model.Session.GeneralCommand.
    :type body: dict | bytes

    """
    body = GeneralCommand.from_dict(body)
    return web.Response(status=200)


async def send_general_command(request: web.Request, session_id, command) -> web.Response:
    """Issues a general command to a client.

    

    :param session_id: The session id.
    :type session_id: str
    :param command: The command to send.
    :type command: dict | bytes

    """
    command = .from_dict(command)
    return web.Response(status=200)


async def send_message_command(request: web.Request, session_id, text, header=None, timeout_ms=None) -> web.Response:
    """Issues a command to a client to display a message to the user.

    

    :param session_id: The session id.
    :type session_id: str
    :param text: The message test.
    :type text: str
    :param header: The message header.
    :type header: str
    :param timeout_ms: The message timeout. If omitted the user will have to confirm viewing the message.
    :type timeout_ms: int

    """
    return web.Response(status=200)


async def send_playstate_command(request: web.Request, session_id, command, seek_position_ticks=None, controlling_user_id=None) -> web.Response:
    """Issues a playstate command to a client.

    

    :param session_id: The session id.
    :type session_id: str
    :param command: The MediaBrowser.Model.Session.PlaystateCommand.
    :type command: dict | bytes
    :param seek_position_ticks: The optional position ticks.
    :type seek_position_ticks: int
    :param controlling_user_id: The optional controlling user id.
    :type controlling_user_id: str

    """
    command = .from_dict(command)
    return web.Response(status=200)


async def send_system_command(request: web.Request, session_id, command) -> web.Response:
    """Issues a system command to a client.

    

    :param session_id: The session id.
    :type session_id: str
    :param command: The command to send.
    :type command: dict | bytes

    """
    command = .from_dict(command)
    return web.Response(status=200)
