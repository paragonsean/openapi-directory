from typing import List, Dict
from aiohttp import web

from openapi_server.models.grafana import Grafana
from openapi_server.models.grafana_board import GrafanaBoard
from openapi_server.models.grafana_config_params import GrafanaConfigParams
from openapi_server.models.service import Service
from openapi_server import util


async def id_delete_grafana_config(request: web.Request, ) -> web.Response:
    """Handle DELETE request for Grafana configuration

    Used for Delete Grafana configuration


    """
    return web.Response(status=200)


async def id_get_grafana(request: web.Request, ) -> web.Response:
    """Handle GET request for Grafana

    Fetches and returns Grafana


    """
    return web.Response(status=200)


async def id_get_grafana_boards(request: web.Request, dashboard_search=None) -> web.Response:
    """Handle GET request for Grafana boards

    Used for fetching Grafana boards and panels

    :param dashboard_search: 
    :type dashboard_search: str

    """
    return web.Response(status=200)


async def id_get_grafana_config(request: web.Request, ) -> web.Response:
    """Handle GET request for Grafana configuration

    Used for fetching Grafana configuration


    """
    return web.Response(status=200)


async def id_get_grafana_ping(request: web.Request, ) -> web.Response:
    """Handle GET request for Grafana ping

    Used to initiate a Grafana ping


    """
    return web.Response(status=200)


async def id_get_grafana_query(request: web.Request, ) -> web.Response:
    """Handle GET request for Grafana queries

    Used for handling Grafana queries


    """
    return web.Response(status=200)


async def id_post_grafana_boards(request: web.Request, ) -> web.Response:
    """Handle POST request for Grafana boards

    Used for persist Grafana boards and panel selections


    """
    return web.Response(status=200)


async def id_post_grafana_config(request: web.Request, body) -> web.Response:
    """Handle POST request for Grafana configuration

    Used for persisting Grafana configuration

    :param body: 
    :type body: dict | bytes

    """
    body = GrafanaConfigParams.from_dict(body)
    return web.Response(status=200)
