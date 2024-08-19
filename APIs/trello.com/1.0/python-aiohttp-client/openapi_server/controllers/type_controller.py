from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_types_by_id(request: web.Request, id, key, token) -> web.Response:
    """getTypesById()

    

    :param id: id
    :type id: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)
