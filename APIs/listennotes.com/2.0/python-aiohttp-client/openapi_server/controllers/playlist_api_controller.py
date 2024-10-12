from typing import List, Dict
from aiohttp import web

from openapi_server.models.playlist_response import PlaylistResponse
from openapi_server.models.playlists_response import PlaylistsResponse
from openapi_server import util


async def get_playlist_by_id(request: web.Request, x_listen_api_key, id, type=None, last_timestamp_ms=None, sort=None) -> web.Response:
    """Fetch a playlist&#39;s info and items (i.e., episodes or podcasts).

    A playlist can be an episode list (i.e., all items are episodes) or a podcast list (i.e., all items are podcasts), which is essentially the same as those created via listennotes.com/listen/. This endpoint fetches a list of items (i.e., episodes or podcasts) in the playlist. You can use the **last_pub_date_ms** parameter to do pagination and fetch more items. A playlist can be **public** (discoverable on ListenNotes.com), **unlisted** (accessible to anyone who knows the playlist id), or **private** (accessible to its owner). You can fetch all playlists created by you, and **public** / **unlisted** playlists created by others. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param id: Playlist id (always 11 characters, e.g., m1pe7z60bsw). You can get the podcast id from the url of a playlist, e.g., m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw 
    :type id: str
    :param type: The type of this playlist, which should be either **episode_list** or **podcast_list**. 
    :type type: str
    :param last_timestamp_ms: For playlist items pagination. It&#39;s the value of **last_timestamp_ms** from the response of last request. If it&#39;s 0 or not specified, just return the latest or the oldest 20 items, depending on the value of the **sort** parameter. 
    :type last_timestamp_ms: int
    :param sort: How do you want to sort playlist items? 
    :type sort: str

    """
    return web.Response(status=200)


async def get_playlists(request: web.Request, x_listen_api_key, sort=None, page=None) -> web.Response:
    """Fetch a list of your playlists.

    This endpoint returns same data as listennotes.com/listen under your account. You can use the **page** parameter to do pagination and fetch more playlists. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param sort: How do you want to sort playlists? 
    :type sort: str
    :param page: Page number of playlists. 
    :type page: int

    """
    return web.Response(status=200)
