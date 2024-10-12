from typing import List, Dict
from aiohttp import web

from openapi_server.models.composition_hook_enum_format import CompositionHookEnumFormat
from openapi_server.models.list_composition_hook_response import ListCompositionHookResponse
from openapi_server.models.video_v1_composition_hook import VideoV1CompositionHook
from openapi_server import util


async def create_composition_hook(request: web.Request, friendly_name, audio_sources=None, audio_sources_excluded=None, enabled=None, format=None, resolution=None, status_callback=None, status_callback_method=None, trim=None, video_layout=None) -> web.Response:
    """create_composition_hook

    

    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to  100 characters long and it must be unique within the account.
    :type friendly_name: str
    :param audio_sources: An array of track names from the same group room to merge into the compositions created by the composition hook. Can include zero or more track names. A composition triggered by the composition hook includes all audio sources specified in &#x60;audio_sources&#x60; except those specified in &#x60;audio_sources_excluded&#x60;. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; includes tracks named &#x60;student&#x60; as well as &#x60;studentTeam&#x60;.
    :type audio_sources: List[str]
    :param audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook includes all audio sources specified in &#x60;audio_sources&#x60; except for those specified in &#x60;audio_sources_excluded&#x60;. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; excludes &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. This parameter can also be empty.
    :type audio_sources_excluded: List[str]
    :param enabled: Whether the composition hook is active. When &#x60;true&#x60;, the composition hook will be triggered for every completed Group Room in the account. When &#x60;false&#x60;, the composition hook will never be triggered.
    :type enabled: bool
    :param format: 
    :type format: str
    :param resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to &#x60;640x480&#x60;.  The string&#39;s format is &#x60;{width}x{height}&#x60; where:   * 16 &lt;&#x3D; &#x60;{width}&#x60; &lt;&#x3D; 1280 * 16 &lt;&#x3D; &#x60;{height}&#x60; &lt;&#x3D; 1280 * &#x60;{width}&#x60; * &#x60;{height}&#x60; &lt;&#x3D; 921,600  Typical values are:   * HD &#x3D; &#x60;1280x720&#x60; * PAL &#x3D; &#x60;1024x576&#x60; * VGA &#x3D; &#x60;640x480&#x60; * CIF &#x3D; &#x60;320x240&#x60;  Note that the &#x60;resolution&#x60; imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type resolution: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;.
    :type status_callback_method: str
    :param trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the composition hook. The default is &#x60;true&#x60;. Compositions with &#x60;trim&#x60; enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type trim: bool
    :param video_layout: An object that describes the video layout of the composition hook in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type video_layout: dict | bytes

    """
    video_layout = object.from_dict(video_layout)
    return web.Response(status=200)


async def delete_composition_hook(request: web.Request, sid) -> web.Response:
    """delete_composition_hook

    Delete a Recording CompositionHook resource identified by a &#x60;CompositionHook SID&#x60;.

    :param sid: The SID of the CompositionHook resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_composition_hook(request: web.Request, sid) -> web.Response:
    """fetch_composition_hook

    Returns a single CompositionHook resource identified by a CompositionHook SID.

    :param sid: The SID of the CompositionHook resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_composition_hook(request: web.Request, enabled=None, date_created_after=None, date_created_before=None, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_composition_hook

    List of all Recording CompositionHook resources.

    :param enabled: Read only CompositionHook resources with an &#x60;enabled&#x60; value that matches this parameter.
    :type enabled: bool
    :param date_created_after: Read only CompositionHook resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
    :type date_created_after: str
    :param date_created_before: Read only CompositionHook resources created before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
    :type date_created_before: str
    :param friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is not case sensitive and can include asterisk &#x60;*&#x60; characters as wildcard match.
    :type friendly_name: str
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


async def update_composition_hook(request: web.Request, sid, friendly_name, audio_sources=None, audio_sources_excluded=None, enabled=None, format=None, resolution=None, status_callback=None, status_callback_method=None, trim=None, video_layout=None) -> web.Response:
    """update_composition_hook

    

    :param sid: The SID of the CompositionHook resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to  100 characters long and it must be unique within the account.
    :type friendly_name: str
    :param audio_sources: An array of track names from the same group room to merge into the compositions created by the composition hook. Can include zero or more track names. A composition triggered by the composition hook includes all audio sources specified in &#x60;audio_sources&#x60; except those specified in &#x60;audio_sources_excluded&#x60;. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; includes tracks named &#x60;student&#x60; as well as &#x60;studentTeam&#x60;.
    :type audio_sources: List[str]
    :param audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook includes all audio sources specified in &#x60;audio_sources&#x60; except for those specified in &#x60;audio_sources_excluded&#x60;. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; excludes &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. This parameter can also be empty.
    :type audio_sources_excluded: List[str]
    :param enabled: Whether the composition hook is active. When &#x60;true&#x60;, the composition hook will be triggered for every completed Group Room in the account. When &#x60;false&#x60;, the composition hook never triggers.
    :type enabled: bool
    :param format: 
    :type format: str
    :param resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to &#x60;640x480&#x60;.  The string&#39;s format is &#x60;{width}x{height}&#x60; where:   * 16 &lt;&#x3D; &#x60;{width}&#x60; &lt;&#x3D; 1280 * 16 &lt;&#x3D; &#x60;{height}&#x60; &lt;&#x3D; 1280 * &#x60;{width}&#x60; * &#x60;{height}&#x60; &lt;&#x3D; 921,600  Typical values are:   * HD &#x3D; &#x60;1280x720&#x60; * PAL &#x3D; &#x60;1024x576&#x60; * VGA &#x3D; &#x60;640x480&#x60; * CIF &#x3D; &#x60;320x240&#x60;  Note that the &#x60;resolution&#x60; imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type resolution: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;.
    :type status_callback_method: str
    :param trim: Whether to clip the intervals where there is no active media in the compositions triggered by the composition hook. The default is &#x60;true&#x60;. Compositions with &#x60;trim&#x60; enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type trim: bool
    :param video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :type video_layout: dict | bytes

    """
    video_layout = object.from_dict(video_layout)
    return web.Response(status=200)
