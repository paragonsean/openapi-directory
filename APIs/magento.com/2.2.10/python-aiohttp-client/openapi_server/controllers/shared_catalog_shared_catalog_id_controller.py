from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_data_shared_catalog_interface import SharedCatalogDataSharedCatalogInterface
from openapi_server import util


async def shared_catalog_shared_catalog_repository_v1_delete_by_id_delete(request: web.Request, shared_catalog_id) -> web.Response:
    """sharedCatalog/{sharedCatalogId}

    Delete a shared catalog by ID.

    :param shared_catalog_id: 
    :type shared_catalog_id: int

    """
    return web.Response(status=200)


async def shared_catalog_shared_catalog_repository_v1_get_get(request: web.Request, shared_catalog_id) -> web.Response:
    """sharedCatalog/{sharedCatalogId}

    Return the following properties for the selected shared catalog: ID, Store Group ID, Name, Type, Description, Customer Group, Tax Class.

    :param shared_catalog_id: 
    :type shared_catalog_id: int

    """
    return web.Response(status=200)
