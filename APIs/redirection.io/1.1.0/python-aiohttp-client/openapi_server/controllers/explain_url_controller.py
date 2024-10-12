from typing import List, Dict
from aiohttp import web

from openapi_server.models.explain_url import ExplainUrl
from openapi_server.models.explain_url_write import ExplainUrlWrite
from openapi_server import util


async def get_explain_url_item(request: web.Request, id) -> web.Response:
    """Retrieves a ExplainUrl resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_explain_url_collection(request: web.Request, explain_url=None) -> web.Response:
    """Creates a ExplainUrl resource.

    

    :param explain_url: The new ExplainUrl resource
    :type explain_url: dict | bytes

    """
    explain_url = ExplainUrlWrite.from_dict(explain_url)
    return web.Response(status=200)
