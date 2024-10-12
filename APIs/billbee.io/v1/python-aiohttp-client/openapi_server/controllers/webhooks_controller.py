from typing import List, Dict
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_web_hook_api_model import RechnungsdruckWebAppControllersApiWebHookApiModel
from openapi_server import util


async def web_hook_management_delete(request: web.Request, id) -> web.Response:
    """Deletes an existing WebHook registration.

    

    :param id: The WebHook ID.
    :type id: str

    """
    return web.Response(status=200)


async def web_hook_management_delete_all(request: web.Request, ) -> web.Response:
    """Deletes all existing WebHook registrations.

    


    """
    return web.Response(status=200)


async def web_hook_management_get(request: web.Request, ) -> web.Response:
    """Gets all registered WebHooks for a given user.

    


    """
    return web.Response(status=200)


async def web_hook_management_get_filters(request: web.Request, ) -> web.Response:
    """Returns a list of all known filters you can use to register webhooks

    


    """
    return web.Response(status=200)


async def web_hook_management_lookup(request: web.Request, id) -> web.Response:
    """Looks up a registered WebHook with the given {id} for a given user.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def web_hook_management_post(request: web.Request, body) -> web.Response:
    """Registers a new WebHook for a given user.

    

    :param body: The webhook to create. Attach ?noecho to the uri to prevent echo test.
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiWebHookApiModel.from_dict(body)
    return web.Response(status=200)


async def web_hook_management_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing WebHook registration.

    

    :param id: The WebHook ID.
    :type id: str
    :param body: The new webhook to use.
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiWebHookApiModel.from_dict(body)
    return web.Response(status=200)
