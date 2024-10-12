from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_shared_catalog_repository_v1_save_post_request import SharedCatalogSharedCatalogRepositoryV1SavePostRequest
from openapi_server import util


async def shared_catalog_shared_catalog_repository_v1_save_put(request: web.Request, id, body=None) -> web.Response:
    """sharedCatalog/{id}

    Create or update Shared Catalog service.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SharedCatalogSharedCatalogRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
