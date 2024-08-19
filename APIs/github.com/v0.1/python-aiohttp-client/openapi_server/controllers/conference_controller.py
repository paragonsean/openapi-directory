from typing import List, Dict
from aiohttp import web

from openapi_server.models.conference_deaf_response import ConferenceDeafResponse
from openapi_server.models.conference_hangup_response import ConferenceHangupResponse
from openapi_server.models.conference_kick_response import ConferenceKickResponse
from openapi_server.models.conference_list_members_response import ConferenceListMembersResponse
from openapi_server.models.conference_list_response import ConferenceListResponse
from openapi_server.models.conference_mute_response import ConferenceMuteResponse
from openapi_server.models.conference_play_response import ConferencePlayResponse
from openapi_server.models.conference_record_start_response import ConferenceRecordStartResponse
from openapi_server.models.conference_record_stop_response import ConferenceRecordStopResponse
from openapi_server.models.conference_speak_response import ConferenceSpeakResponse
from openapi_server.models.conference_undeaf_response import ConferenceUndeafResponse
from openapi_server.models.conference_unmute_response import ConferenceUnmuteResponse
from openapi_server import util


async def v01_conference_deaf_post(request: web.Request, conference_name, member_id) -> web.Response:
    """/v0.1/ConferenceDeaf/

    Blocks audio to one or more conference members

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str

    """
    return web.Response(status=200)


async def v01_conference_hangup_post(request: web.Request, conference_name, member_id) -> web.Response:
    """/v0.1/ConferenceHangup/

    Kicks one or more conference members, without playing the kick sound

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str

    """
    return web.Response(status=200)


async def v01_conference_kick_post(request: web.Request, conference_name, member_id) -> web.Response:
    """/v0.1/ConferenceKick/

    Kicks one or more conference members

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str

    """
    return web.Response(status=200)


async def v01_conference_list_members_post(request: web.Request, conference_name, call_uuid_filter=None, deaf_filter=None, member_filter=None, muted_filter=None) -> web.Response:
    """/v0.1/ConferenceListMembers/

    Retrieves the member list for a given conference

    :param conference_name: Name of the conference
    :type conference_name: str
    :param call_uuid_filter: Restricts listed calls to the provided values (comma separated call UUID list)
    :type call_uuid_filter: str
    :param deaf_filter: Restricts listed members to deaf ones
    :type deaf_filter: bool
    :param member_filter: Restricts listed members to the provided values (comma separated member ID list)
    :type member_filter: str
    :param muted_filter: Restricts listed members to muted ones
    :type muted_filter: bool

    """
    return web.Response(status=200)


async def v01_conference_list_post(request: web.Request, call_uuid_filter=None, deaf_filter=None, member_filter=None, muted_filter=None) -> web.Response:
    """/v0.1/ConferenceList/

    Returns a list of all established conferences

    :param call_uuid_filter: Restricts listed calls to the provided values (comma separated call UUID list)
    :type call_uuid_filter: str
    :param deaf_filter: Restricts listed members to deaf ones
    :type deaf_filter: bool
    :param member_filter: Restricts listed members to the provided values (comma separated member ID list)
    :type member_filter: str
    :param muted_filter: Restricts listed members to muted ones
    :type muted_filter: bool

    """
    return web.Response(status=200)


async def v01_conference_mute_post(request: web.Request, conference_name, member_id) -> web.Response:
    """/v0.1/ConferenceMute/

    Blocks audio from one or more conference members

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str

    """
    return web.Response(status=200)


async def v01_conference_play_post(request: web.Request, conference_name, file_path, member_id) -> web.Response:
    """/v0.1/ConferencePlay/

    Plays media to one or more conference members

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param file_path: Path/URI of the media file to be played
    :type file_path: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str

    """
    return web.Response(status=200)


async def v01_conference_record_start_post(request: web.Request, conference_name, file_format=None, file_name=None, file_path=None) -> web.Response:
    """/v0.1/ConferenceRecordStart/

    Initiates a conference recording

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param file_format: File format (extension)
    :type file_format: str
    :param file_name: Recording file name (without extension); if empty, a timestamp based file name will be generated
    :type file_name: str
    :param file_path: Directory path/URI where the recording file will be saved
    :type file_path: str

    """
    return web.Response(status=200)


async def v01_conference_record_stop_post(request: web.Request, conference_name, record_file) -> web.Response:
    """/v0.1/ConferenceRecordStop/

    Stops a conference recording

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param record_file: Full path to recording file, as returned by ConferenceRecordStart; &#x60;all&#x60; shorthand is also available
    :type record_file: str

    """
    return web.Response(status=200)


async def v01_conference_speak_post(request: web.Request, conference_name, member_id, text) -> web.Response:
    """/v0.1/ConferenceSpeak/

    Plays synthesized speech into a conference

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str
    :param text: Text to be synthesized
    :type text: str

    """
    return web.Response(status=200)


async def v01_conference_undeaf_post(request: web.Request, conference_name, member_id) -> web.Response:
    """/v0.1/ConferenceUndeaf/

    Restores audio to one or more conference members

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str

    """
    return web.Response(status=200)


async def v01_conference_unmute_post(request: web.Request, conference_name, member_id) -> web.Response:
    """/v0.1/ConferenceUnmute/

    Restores audio from one or more conference members

    :param conference_name: Name of the conference in question
    :type conference_name: str
    :param member_id: List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too.
    :type member_id: str

    """
    return web.Response(status=200)
