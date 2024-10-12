from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_setlists import JsonSetlists
from openapi_server import util


async def resource10_artist_mbid_setlists_get_artist_setlists_get(request: web.Request, mbid, p=None) -> web.Response:
    """.

    &lt;p&gt; Get a list of an artist&#39;s setlists. &lt;/p&gt;

    :param mbid: the Musicbrainz MBID of the artist
    :type mbid: str
    :param p: the number of the result page
    :type p: int

    """
    return web.Response(status=200)
