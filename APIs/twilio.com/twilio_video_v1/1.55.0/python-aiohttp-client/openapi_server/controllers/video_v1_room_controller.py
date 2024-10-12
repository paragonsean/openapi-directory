from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_room_response import ListRoomResponse
from openapi_server.models.room_enum_room_status import RoomEnumRoomStatus
from openapi_server.models.room_enum_room_type import RoomEnumRoomType
from openapi_server.models.room_enum_video_codec import RoomEnumVideoCodec
from openapi_server.models.video_v1_room import VideoV1Room
from openapi_server import util


async def create_room(request: web.Request, audio_only=None, empty_room_timeout=None, enable_turn=None, large_room=None, max_participant_duration=None, max_participants=None, media_region=None, record_participants_on_connect=None, recording_rules=None, status_callback=None, status_callback_method=None, type=None, unique_name=None, unused_room_timeout=None, video_codecs=None) -> web.Response:
    """create_room

    

    :param audio_only: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
    :type audio_only: bool
    :param empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
    :type empty_room_timeout: int
    :param enable_turn: Deprecated, now always considered to be true.
    :type enable_turn: bool
    :param large_room: When set to true, indicated that this is the large room.
    :type large_room: bool
    :param max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
    :type max_participant_duration: int
    :param max_participants: The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants.
    :type max_participants: int
    :param media_region: The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers). ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.***
    :type media_region: str
    :param record_participants_on_connect: Whether to start recording when Participants connect. ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.***
    :type record_participants_on_connect: bool
    :param recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for recording
    :type recording_rules: dict | bytes
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be &#x60;POST&#x60; or &#x60;GET&#x60;.
    :type status_callback_method: str
    :param type: 
    :type type: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used as a &#x60;room_sid&#x60; in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for &#x60;in-progress&#x60; rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is &#x60;in-progress&#x60;.
    :type unique_name: str
    :param unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
    :type unused_room_timeout: int
    :param video_codecs: An array of the video codecs that are supported when publishing a track in the room.  Can be: &#x60;VP8&#x60; and &#x60;H264&#x60;.  ***This feature is not available in &#x60;peer-to-peer&#x60; rooms***
    :type video_codecs: list | bytes

    """
    recording_rules = object.from_dict(recording_rules)
    video_codecs = [RoomEnumVideoCodec.from_dict(d) for d in video_codecs]
    return web.Response(status=200)


async def fetch_room(request: web.Request, sid) -> web.Response:
    """fetch_room

    

    :param sid: The SID of the Room resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_room(request: web.Request, status=None, unique_name=None, date_created_after=None, date_created_before=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_room

    

    :param status: Read only the rooms with this status. Can be: &#x60;in-progress&#x60; (default) or &#x60;completed&#x60;
    :type status: str
    :param unique_name: Read only rooms with the this &#x60;unique_name&#x60;.
    :type unique_name: str
    :param date_created_after: Read only rooms that started on or after this date, given as &#x60;YYYY-MM-DD&#x60;.
    :type date_created_after: str
    :param date_created_before: Read only rooms that started before this date, given as &#x60;YYYY-MM-DD&#x60;.
    :type date_created_before: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    date_created_after = util.deserialize_datetime(date_created_after)
    date_created_before = util.deserialize_datetime(date_created_before)
    return web.Response(status=200)


async def update_room(request: web.Request, sid, status) -> web.Response:
    """update_room

    

    :param sid: The SID of the Room resource to update.
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
