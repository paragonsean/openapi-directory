from typing import List, Dict
from aiohttp import web

from openapi_server.models.import_read import ImportRead
from openapi_server.models.import_write import ImportWrite
from openapi_server import util


async def get_import_collection(request: web.Request, project_id, page=None) -> web.Response:
    """Retrieves the collection of Import resources.

    

    :param project_id: 
    :type project_id: str
    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_import_item(request: web.Request, id) -> web.Response:
    """Retrieves a Import resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_import_collection(request: web.Request, _import=None) -> web.Response:
    """Creates a Import resource.

    

    :param _import: The new Import resource
    :type _import: dict | bytes

    """
    _import = ImportWrite.from_dict(_import)
    return web.Response(status=200)
