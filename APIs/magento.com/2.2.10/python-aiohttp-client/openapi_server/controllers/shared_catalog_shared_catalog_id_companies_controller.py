from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def shared_catalog_company_management_v1_get_companies_get(request: web.Request, shared_catalog_id) -> web.Response:
    """sharedCatalog/{sharedCatalogId}/companies

    Return the list of company IDs for the companies assigned to the selected catalog.

    :param shared_catalog_id: 
    :type shared_catalog_id: int

    """
    return web.Response(status=200)
