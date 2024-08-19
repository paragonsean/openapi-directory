from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.search200_response import Search200Response
from openapi_server import util


async def search(request: web.Request, q, type, market=None, limit=None, offset=None, include_external=None) -> web.Response:
    """Search for Item 

    Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks that match a keyword string.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

    :param q: 
    :type q: str
    :param type: 
    :type type: List[str]
    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param include_external: 
    :type include_external: str

    """
    return web.Response(status=200)
