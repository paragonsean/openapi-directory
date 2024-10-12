from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_setlists import JsonSetlists
from openapi_server import util


async def resource10_venue_venue_id_setlists_get_venue_setlists_get(request: web.Request, venue_id, p=None) -> web.Response:
    """.

    &lt;p&gt; Get setlists for a specific venue. &lt;/p&gt;

    :param venue_id: the id of the venue
    :type venue_id: str
    :param p: the number of the result page
    :type p: int

    """
    return web.Response(status=200)
