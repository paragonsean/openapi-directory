from typing import List, Dict
from aiohttp import web

from openapi_server.models.composition_enum_format import CompositionEnumFormat
from openapi_server.models.composition_enum_status import CompositionEnumStatus
from openapi_server.models.list_composition_response import ListCompositionResponse
from openapi_server.models.video_v1_composition import VideoV1Composition
from openapi_server import util


async def create_composition(request: web.Request, room_sid, audio_sources=None, audio_sources_excluded=None, format=None, resolution=None, status_callback=None, status_callback_method=None, trim=None, video_layout=None) -> web.Response:
    """create_composition

    

    :param room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
    :type room_sid: str
    :param audio_sources: An array of track names from the same group room to merge into the new composition. Can include zero or more track names. The new composition includes all audio sources specified in &#x60;audio_sources&#x60; except for those specified in &#x60;audio_sources_excluded&#x60;. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, &#x60;student*&#x60; includes &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
    :type audio_sources: List[str]
    :param audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources specified in &#x60;audio_sources&#x60; except for those specified in &#x60;audio_sources_excluded&#x60;. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, &#x60;student*&#x60; excludes &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. This parameter can also be empty.
    :type audio_sources_excluded: List[str]
    :param format: 
    :type format: str
    :param resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to &#x60;640x480&#x60;.  The string&#39;s format is &#x60;{width}x{height}&#x60; where:   * 16 &lt;&#x3D; &#x60;{width}&#x60; &lt;&#x3D; 1280 * 16 &lt;&#x3D; &#x60;{height}&#x60; &lt;&#x3D; 1280 * &#x60;{width}&#x60; * &#x60;{height}&#x60; &lt;&#x3D; 921,600  Typical values are:   * HD &#x3D; &#x60;1280x720&#x60; * PAL &#x3D; &#x60;1024x576&#x60; * VGA &#x3D; &#x60;640x480&#x60; * CIF &#x3D; &#x60;320x240&#x60;  Note that the &#x60;resolution&#x60; imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type resolution: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;.
    :type status_callback_method: str
    :param trim: Whether to clip the intervals where there is no active media in the composition. The default is &#x60;true&#x60;. Compositions with &#x60;trim&#x60; enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type trim: bool
    :param video_layout: An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
    :type video_layout: dict | bytes

    """
    video_layout = object.from_dict(video_layout)
    return web.Response(status=200)


async def delete_composition(request: web.Request, sid) -> web.Response:
    """delete_composition

    Delete a Recording Composition resource identified by a Composition SID.

    :param sid: The SID of the Composition resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_composition(request: web.Request, sid) -> web.Response:
    """fetch_composition

    Returns a single Composition resource identified by a Composition SID.

    :param sid: The SID of the Composition resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_composition(request: web.Request, status=None, date_created_after=None, date_created_before=None, room_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_composition

    List of all Recording compositions.

    :param status: Read only Composition resources with this status. Can be: &#x60;enqueued&#x60;, &#x60;processing&#x60;, &#x60;completed&#x60;, &#x60;deleted&#x60;, or &#x60;failed&#x60;.
    :type status: str
    :param date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
    :type date_created_after: str
    :param date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
    :type date_created_before: str
    :param room_sid: Read only Composition resources with this Room SID.
    :type room_sid: str
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
