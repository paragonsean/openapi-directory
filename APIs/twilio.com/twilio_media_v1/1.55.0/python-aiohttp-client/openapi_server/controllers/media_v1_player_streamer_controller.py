from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_player_streamer_response import ListPlayerStreamerResponse
from openapi_server.models.media_v1_player_streamer import MediaV1PlayerStreamer
from openapi_server.models.player_streamer_enum_order import PlayerStreamerEnumOrder
from openapi_server.models.player_streamer_enum_status import PlayerStreamerEnumStatus
from openapi_server.models.player_streamer_enum_update_status import PlayerStreamerEnumUpdateStatus
from openapi_server import util


async def create_player_streamer(request: web.Request, max_duration=None, status_callback=None, status_callback_method=None, video=None) -> web.Response:
    """create_player_streamer

    

    :param max_duration: The maximum time, in seconds, that the PlayerStreamer is active (&#x60;created&#x60; or &#x60;started&#x60;) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming.
    :type max_duration: int
    :param status_callback: The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details.
    :type status_callback: str
    :param status_callback_method: The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;.
    :type status_callback_method: str
    :param video: Specifies whether the PlayerStreamer is configured to stream video. Defaults to &#x60;true&#x60;.
    :type video: bool

    """
    return web.Response(status=200)


async def fetch_player_streamer(request: web.Request, sid) -> web.Response:
    """fetch_player_streamer

    Returns a single PlayerStreamer resource identified by a SID.

    :param sid: The SID of the PlayerStreamer resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_player_streamer(request: web.Request, order=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_player_streamer

    Returns a list of PlayerStreamers.

    :param order: The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default.
    :type order: str
    :param status: Status to filter by, with possible values &#x60;created&#x60;, &#x60;started&#x60;, &#x60;ended&#x60;, or &#x60;failed&#x60;.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_player_streamer(request: web.Request, sid, status) -> web.Response:
    """update_player_streamer

    Updates a PlayerStreamer resource identified by a SID.

    :param sid: The SID of the PlayerStreamer resource to update.
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
