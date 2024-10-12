from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.plugin import Plugin
from openapi_server.models.plugin_params import PluginParams
from openapi_server.models.plugin_run import PluginRun
from openapi_server.models.plugin_run_data import PluginRunData
from openapi_server import util


async def create_plugin_run(request: web.Request, deploy_id, plugin_run=None) -> web.Response:
    """create_plugin_run

    This is an internal-only endpoint.

    :param deploy_id: 
    :type deploy_id: str
    :param plugin_run: 
    :type plugin_run: dict | bytes

    """
    plugin_run = PluginRunData.from_dict(plugin_run)
    return web.Response(status=200)


async def get_latest_plugin_runs(request: web.Request, site_id, packages, state=None) -> web.Response:
    """get_latest_plugin_runs

    This is an internal-only endpoint.

    :param site_id: 
    :type site_id: str
    :param packages: 
    :type packages: List[str]
    :param state: 
    :type state: str

    """
    return web.Response(status=200)


async def update_plugin(request: web.Request, site_id, package, plugin_params=None) -> web.Response:
    """update_plugin

    This is an internal-only endpoint.

    :param site_id: 
    :type site_id: str
    :param package: 
    :type package: str
    :param plugin_params: 
    :type plugin_params: dict | bytes

    """
    plugin_params = PluginParams.from_dict(plugin_params)
    return web.Response(status=200)
