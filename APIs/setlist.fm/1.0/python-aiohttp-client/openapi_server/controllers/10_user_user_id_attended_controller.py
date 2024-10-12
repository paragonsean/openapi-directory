from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_setlists import JsonSetlists
from openapi_server import util


async def resource10_user_user_id_attended_get_user_attended_setlists_get(request: web.Request, user_id, p=None) -> web.Response:
    """.

    &lt;p&gt; Get a list of setlists of concerts attended by a user. &lt;/p&gt;

    :param user_id: the user&#39;s userId
    :type user_id: str
    :param p: the number of the result page
    :type p: int

    """
    return web.Response(status=200)
