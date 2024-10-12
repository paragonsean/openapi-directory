from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v20_get(request: web.Request, name=None, prefix=None, description=None) -> web.Response:
    """api_v20_get

    Top level information about EnteroBase databases

    :param name: Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    :type name: str
    :param prefix: Database prefix, e.g. SAL for Salmonella
    :type prefix: str
    :param description: Database description
    :type description: str

    """
    return web.Response(status=200)
