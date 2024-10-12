from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_setlists import JsonSetlists
from openapi_server import util


async def resource10_user_user_id_edited_get_user_edited_setlists_get(request: web.Request, user_id, p=None) -> web.Response:
    """.

    &lt;p&gt; Get a list of setlists of concerts edited by a user. The list contains the current version, not the version edited. &lt;/p&gt;

    :param user_id: the user&#39;s userId
    :type user_id: str
    :param p: the number of the result page
    :type p: int

    """
    return web.Response(status=200)
