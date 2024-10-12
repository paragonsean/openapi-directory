from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.service_credential import ServiceCredential
from openapi_server.models.service_credentials_collection import ServiceCredentialsCollection
from openapi_server import util


async def list_service_credentials(request: web.Request, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceCredentials

    Returns an array of ServiceCredential objects

    :param limit: The numbers of items to return per page.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param filter: Filter for querying collections.
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param sort_by: The list of attribute and order to sort the result set by.
    :type sort_by: dict | bytes
    :type sort_by: Dict[str, ]

    """
    filter = .from_dict(filter)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def show_service_credential(request: web.Request, id) -> web.Response:
    """Show an existing ServiceCredential

    Returns a ServiceCredential object

    :param id: ID of the resource
    :type id: str

    """
    return web.Response(status=200)
