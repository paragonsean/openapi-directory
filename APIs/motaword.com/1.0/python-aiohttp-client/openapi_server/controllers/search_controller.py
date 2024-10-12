from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_operation_status import AsyncOperationStatus
from openapi_server.models.search_everywhere_result import SearchEverywhereResult
from openapi_server import util


async def check_documents_reindex(request: web.Request, async_request_key) -> web.Response:
    """Check reindex status of the client source and translation documents.

    

    :param async_request_key: Async operation key
    :type async_request_key: str

    """
    return web.Response(status=200)


async def reindex_documents(request: web.Request, ) -> web.Response:
    """Reindex for search all of the client source and translation documents.

    


    """
    return web.Response(status=200)


async def search_everywhere(request: web.Request, query, include=None, page=None, per_page=None) -> web.Response:
    """Search everything in your account

    Search through everything in your account, from projects to documents, from source strings to translations...

    :param query: Search query term
    :type query: str
    :param include: Search in these entities. Current oprions are projects, documents, strings. Can be multiple. When not provided, we&#39;ll search through all entities.
    :type include: List[str]
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)
