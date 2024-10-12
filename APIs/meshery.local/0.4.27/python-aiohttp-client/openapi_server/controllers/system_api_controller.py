from typing import List, Dict
from aiohttp import web

from openapi_server.models.adapter import Adapter
from openapi_server.models.k8_s_config import K8SConfig
from openapi_server.models.k8_s_context import K8SContext
from openapi_server.models.preference import Preference
from openapi_server.models.service import Service
from openapi_server.models.version import Version
from openapi_server import util


async def id_delete_adapter_config(request: web.Request, adapter=None) -> web.Response:
    """Handle DELETE requests to delete adapter config

    Used to delete adapter configuration

    :param adapter: 
    :type adapter: str

    """
    return web.Response(status=200)


async def id_delete_k8_s_config(request: web.Request, ) -> web.Response:
    """Handle DELETE request for Kubernetes Config

    Used to delete kubernetes config to System


    """
    return web.Response(status=200)


async def id_get_kubernetes_ping(request: web.Request, ) -> web.Response:
    """Handle GET request for Kubernetes ping

    Fetches server version to simulate ping


    """
    return web.Response(status=200)


async def id_get_system_adapters(request: web.Request, adapter=None) -> web.Response:
    """Handle GET request for adapters

    Fetches and returns all the adapters and ping adapters

    :param adapter: 
    :type adapter: str

    """
    return web.Response(status=200)


async def id_get_system_version(request: web.Request, ) -> web.Response:
    """Handle GET request for system/server version

    Returns the running Meshery version


    """
    return web.Response(status=200)


async def id_mesh_sync_grafana(request: web.Request, ) -> web.Response:
    """Handle GET request for mesh-sync grafana

    Fetches Prometheus and Grafana


    """
    return web.Response(status=200)


async def id_mesh_sync_prometheus(request: web.Request, ) -> web.Response:
    """Handle GET request for fetching prometheus

    Fetches Prometheus


    """
    return web.Response(status=200)


async def id_post_adapter_config(request: web.Request, body=None) -> web.Response:
    """Handle POST requests to persist adapter config

    Used to persist adapter config

    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def id_post_adapter_operation(request: web.Request, adapter=None, query=None, custom_body=None, namespace=None, delete_op=None) -> web.Response:
    """Handle POST requests for Adapter Operations

    Used to send operations to the adapters

    :param adapter: 
    :type adapter: str
    :param query: 
    :type query: str
    :param custom_body: 
    :type custom_body: str
    :param namespace: 
    :type namespace: str
    :param delete_op: 
    :type delete_op: str

    """
    return web.Response(status=200)


async def id_post_k8_s_config(request: web.Request, ) -> web.Response:
    """Handle POST request for Kubernetes Config

    Used to add kubernetes config to System


    """
    return web.Response(status=200)


async def id_post_k8_s_contexts(request: web.Request, ) -> web.Response:
    """Handle POST requests for Kubernetes Context list

    Returns the context list for a given k8s config


    """
    return web.Response(status=200)


async def id_system_sync(request: web.Request, ) -> web.Response:
    """Handle GET request for config sync

    Used to send session data to the UI for initial sync


    """
    return web.Response(status=200)
