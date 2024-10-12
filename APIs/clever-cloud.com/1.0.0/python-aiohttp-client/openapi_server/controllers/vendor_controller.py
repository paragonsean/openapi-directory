from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.wannabe_addon_billing import WannabeAddonBilling
from openapi_server import util


async def get_vendor_apps_0(request: web.Request, offset=None) -> web.Response:
    """get_vendor_apps_0

    

    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_vendor_apps_addon_id_0(request: web.Request, addon_id) -> web.Response:
    """get_vendor_apps_addon_id_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def post_vendor_billing_owner_id_0(request: web.Request, addon_id, body) -> web.Response:
    """post_vendor_billing_owner_id_0

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddonBilling.from_dict(body)
    return web.Response(status=200)


async def put_vendor_apps_addon_id_0(request: web.Request, addon_id) -> web.Response:
    """put_vendor_apps_addon_id_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def vendor_addons_post_1(request: web.Request, ) -> web.Response:
    """vendor_addons_post_1

    


    """
    return web.Response(status=200)


async def vendor_apps_addon_id_logscollector_get_0(request: web.Request, addon_id) -> web.Response:
    """vendor_apps_addon_id_logscollector_get_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def vendor_apps_addon_id_migration_callback_put_0(request: web.Request, addon_id, plan_id=None, region=None) -> web.Response:
    """vendor_apps_addon_id_migration_callback_put_0

    

    :param addon_id: 
    :type addon_id: str
    :param plan_id: 
    :type plan_id: str
    :param region: 
    :type region: str

    """
    return web.Response(status=200)
