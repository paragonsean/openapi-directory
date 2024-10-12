from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_setlist import JsonSetlist
from openapi_server import util


async def resource10_setlist_setlist_id_get_setlist_get(request: web.Request, setlist_id) -> web.Response:
    """.

    &lt;p&gt; Returns the current version of a setlist. E.g. if you pass the id of a setlist that got edited since you last accessed it, you&#39;ll get the current version. &lt;/p&gt;

    :param setlist_id: the setlist id
    :type setlist_id: str

    """
    return web.Response(status=200)
