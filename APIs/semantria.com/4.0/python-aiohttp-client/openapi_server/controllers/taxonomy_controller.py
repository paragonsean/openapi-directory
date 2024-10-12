from typing import List, Dict
from aiohttp import web

from openapi_server.models.taxonomy_node_response_version import TaxonomyNodeResponseVersion
from openapi_server import util


async def add_taxonomy(request: web.Request, content_type, taxonomy, config_id=None) -> web.Response:
    """Add taxonomy nodes

    This method adds taxonomy nodes on Semantria side.

    :param content_type: 
    :type content_type: str
    :param taxonomy: List of parametrized JSON or XML objects.
    :type taxonomy: 
    :param config_id: Identifier of configuration queries linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def delete_taxonomy(request: web.Request, content_type, taxonomy_node_ids, config_id=None) -> web.Response:
    """Remove taxonomy nodes

    This method removes certain taxonomy nodes by their IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param taxonomy_node_ids: List of taxonomy node identifiers.
    :type taxonomy_node_ids: List[str]
    :param config_id: Identifier of configuration queries linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def get_taxonomy(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve taxonomy

    This method retrieves list of taxonomy available on Semantria side.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration taxonomy linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def update_taxonomy(request: web.Request, content_type, taxonomy, config_id=None) -> web.Response:
    """Update taxonomy nodes

    This method updates taxonomy nodes on Semantria side.

    :param content_type: 
    :type content_type: str
    :param taxonomy: List of parametrized JSON or XML objects.
    :type taxonomy: 
    :param config_id: Identifier of configuration queries linked to.
    :type config_id: str

    """
    return web.Response(status=200)
