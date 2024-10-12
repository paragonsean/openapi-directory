from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_artists import JsonArtists
from openapi_server import util


async def resource10_search_artists_get_artists_get(request: web.Request, artist_mbid=None, artist_name=None, artist_tmid=None, p=None, sort=None) -> web.Response:
    """Search for artists.

    Search for artists.

    :param artist_mbid: the artist&#39;s Musicbrainz Identifier (mbid)
    :type artist_mbid: str
    :param artist_name: the artist&#39;s name
    :type artist_name: str
    :param artist_tmid: the artist&#39;s Ticketmaster Identifier (tmid)
    :type artist_tmid: int
    :param p: the number of the result page you&#39;d like to have
    :type p: int
    :param sort: the sort of the result, either sortName (default) or relevance
    :type sort: str

    """
    return web.Response(status=200)
