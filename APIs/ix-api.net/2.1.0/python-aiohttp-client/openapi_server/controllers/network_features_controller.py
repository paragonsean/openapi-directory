from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.network_feature import NetworkFeature
from openapi_server import util


async def network_features_list(request: web.Request, id=None, type=None, required=None, network_service=None, name=None) -> web.Response:
    """network_features_list

    List available network features.

    :param id: Filter by id
    :type id: List[str]
    :param type: Filter by type
    :type type: str
    :param required: Filter by required
    :type required: str
    :param network_service: Filter by network_service
    :type network_service: str
    :param name: Filter by name
    :type name: str

    """
    return web.Response(status=200)


async def network_features_read(request: web.Request, id) -> web.Response:
    """network_features_read

    Get a single network feature by it&#39;s id.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
