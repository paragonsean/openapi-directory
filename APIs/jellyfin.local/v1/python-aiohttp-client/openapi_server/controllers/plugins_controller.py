from typing import List, Dict
from aiohttp import web

from openapi_server.models.plugin_info import PluginInfo
from openapi_server.models.plugin_security_info import PluginSecurityInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.version import Version
from openapi_server import util


async def disable_plugin(request: web.Request, plugin_id, version) -> web.Response:
    """Disable a plugin.

    

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str
    :param version: Plugin version.
    :type version: dict | bytes

    """
    version = .from_dict(version)
    return web.Response(status=200)


async def enable_plugin(request: web.Request, plugin_id, version) -> web.Response:
    """Enables a disabled plugin.

    

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str
    :param version: Plugin version.
    :type version: dict | bytes

    """
    version = .from_dict(version)
    return web.Response(status=200)


async def get_plugin_configuration(request: web.Request, plugin_id) -> web.Response:
    """Gets plugin configuration.

    

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str

    """
    return web.Response(status=200)


async def get_plugin_image(request: web.Request, plugin_id, version) -> web.Response:
    """Gets a plugin&#39;s image.

    

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str
    :param version: Plugin version.
    :type version: dict | bytes

    """
    version = .from_dict(version)
    return web.Response(status=200)


async def get_plugin_manifest(request: web.Request, plugin_id) -> web.Response:
    """Gets a plugin&#39;s manifest.

    

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str

    """
    return web.Response(status=200)


async def get_plugins(request: web.Request, ) -> web.Response:
    """Gets a list of currently installed plugins.

    


    """
    return web.Response(status=200)


async def uninstall_plugin(request: web.Request, plugin_id) -> web.Response:
    """Uninstalls a plugin.

    

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str

    """
    return web.Response(status=200)


async def uninstall_plugin_by_version(request: web.Request, plugin_id, version) -> web.Response:
    """Uninstalls a plugin by version.

    

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str
    :param version: Plugin version.
    :type version: dict | bytes

    """
    version = .from_dict(version)
    return web.Response(status=200)


async def update_plugin_configuration(request: web.Request, plugin_id) -> web.Response:
    """Updates plugin configuration.

    Accepts plugin configuration as JSON body.

    :param plugin_id: Plugin id.
    :type plugin_id: str
    :type plugin_id: str

    """
    return web.Response(status=200)


async def update_plugin_security_info(request: web.Request, body) -> web.Response:
    """Updates plugin security info.

    

    :param body: Plugin security info.
    :type body: dict | bytes

    """
    body = PluginSecurityInfo.from_dict(body)
    return web.Response(status=200)
