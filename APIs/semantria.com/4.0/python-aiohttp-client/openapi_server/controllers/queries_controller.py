from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_response_version import QueryResponseVersion
from openapi_server import util


async def add_queries(request: web.Request, content_type, queries, config_id=None) -> web.Response:
    """Add or update queries

    This method adds queries on Semantria side.

    :param content_type: 
    :type content_type: str
    :param queries: List of parametrized JSON or XML objects.
    :type queries: 
    :param config_id: Identifier of configuration queries linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def delete_queries(request: web.Request, content_type, query_ids, config_id=None) -> web.Response:
    """Remove queries

    This method removes certain queries by their IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param query_ids: List of query identifiers.
    :type query_ids: List[str]
    :param config_id: Identifier of configuration queries linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def get_queries(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve queries

    This method retrieves list of queries available on Semantria side.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration queries linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def update_queries(request: web.Request, content_type, queries, config_id=None) -> web.Response:
    """Update queries

    This method updates queries by unique IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param queries: List of parametrized JSON or XML objects.
    :type queries: 
    :param config_id: Identifier of configuration queries linked to.
    :type config_id: str

    """
    return web.Response(status=200)
