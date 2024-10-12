from typing import List, Dict
from aiohttp import web

from openapi_server.models.connect_modules import ConnectModules
from openapi_server.models.error_message import ErrorMessage
from openapi_server import util


async def dynamic_modules_resource_get_modules_get(request: web.Request, ) -> web.Response:
    """Get modules

    Returns all modules registered dynamically by the calling app.  **[Permissions](#permissions) required:** Only Connect apps can make this request.


    """
    return web.Response(status=200)


async def dynamic_modules_resource_register_modules_post(request: web.Request, body) -> web.Response:
    """Register modules

    Registers a list of modules.  **[Permissions](#permissions) required:** Only Connect apps can make this request.

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectModules.from_dict(body)
    return web.Response(status=200)


async def dynamic_modules_resource_remove_modules_delete(request: web.Request, module_key=None) -> web.Response:
    """Remove modules

    Remove all or a list of modules registered by the calling app.  **[Permissions](#permissions) required:** Only Connect apps can make this request.

    :param module_key: The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter. For example, &#x60;moduleKey&#x3D;dynamic-attachment-entity-property&amp;moduleKey&#x3D;dynamic-select-field&#x60;. Nonexistent keys are ignored.
    :type module_key: List[str]

    """
    return web.Response(status=200)
