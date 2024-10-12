from typing import List, Dict
from aiohttp import web

from openapi_server.models.done import Done
from openapi_server.models.import_export import ImportExport
from openapi_server import util


async def full_export(request: web.Request, ) -> web.Response:
    """Export the full state of Otoroshi

    Export the full state of Otoroshi


    """
    return web.Response(status=200)


async def full_import(request: web.Request, body=None) -> web.Response:
    """Import the full state of Otoroshi

    Import the full state of Otoroshi

    :param body: 
    :type body: dict | bytes

    """
    body = ImportExport.from_dict(body)
    return web.Response(status=200)


async def full_import_from_file(request: web.Request, body=None) -> web.Response:
    """Import the full state of Otoroshi as a file

    Import the full state of Otoroshi as a file

    :param body: 
    :type body: dict | bytes

    """
    body = ImportExport.from_dict(body)
    return web.Response(status=200)
