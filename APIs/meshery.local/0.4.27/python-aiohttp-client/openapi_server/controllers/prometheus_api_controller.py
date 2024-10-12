from typing import List, Dict
from aiohttp import web

from openapi_server.models.grafana_board import GrafanaBoard
from openapi_server.models.prometheus import Prometheus
from openapi_server.models.selected_grafana_config import SelectedGrafanaConfig
from openapi_server import util


async def id_delete_prometheus_config(request: web.Request, ) -> web.Response:
    """Handle DELETE for Prometheus configuration

    Used for deleting Prometheus configuration


    """
    return web.Response(status=200)


async def id_get_prometheus_config(request: web.Request, ) -> web.Response:
    """Handle GET for Prometheus configuration

    Used for fetching Prometheus configuration


    """
    return web.Response(status=200)


async def id_get_prometheus_ping(request: web.Request, ) -> web.Response:
    """Handle GET request for Prometheus Ping

    Used to ping prometheus


    """
    return web.Response(status=200)


async def id_get_prometheus_query(request: web.Request, ) -> web.Response:
    """Handle GET request for Prometheus Query

    Used to prometheus queries


    """
    return web.Response(status=200)


async def id_get_prometheus_static_board(request: web.Request, ) -> web.Response:
    """Handle GET request for Prometheus static board

    Used to fetch the static board


    """
    return web.Response(status=200)


async def id_post_prometheus_board(request: web.Request, body) -> web.Response:
    """Handle POST request for Prometheus board

    Used to persist selected board and panels

    :param body: 
    :type body: list | bytes

    """
    body = [SelectedGrafanaConfig.from_dict(d) for d in body]
    return web.Response(status=200)


async def id_post_prometheus_board_import(request: web.Request, ) -> web.Response:
    """Handle POST request for Prometheus board import

    Used for importing Grafana board for Prometheus


    """
    return web.Response(status=200)


async def id_post_prometheus_config(request: web.Request, body=None) -> web.Response:
    """Handle POST for Prometheus configuration

    Used for persisting Prometheus configuration

    :param body: 
    :type body: str

    """
    return web.Response(status=200)
