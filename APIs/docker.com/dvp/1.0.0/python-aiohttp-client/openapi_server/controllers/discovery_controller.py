from typing import List, Dict
from aiohttp import web

from openapi_server.models.namespace_data import NamespaceData
from openapi_server.models.namespace_metadata import NamespaceMetadata
from openapi_server import util


async def get_namespace(request: web.Request, namespace) -> web.Response:
    """Get namespace

    Gets metadata associated with specified namespace, including extra repos associated with the namespace

    :param namespace: Namespace to fetch data for
    :type namespace: str

    """
    return web.Response(status=200)


async def get_namespaces(request: web.Request, ) -> web.Response:
    """Get namespaces and repos

    Gets a list of your namespaces and repos which have data available


    """
    return web.Response(status=200)
