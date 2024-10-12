from typing import List, Dict
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.instance import Instance
from openapi_server.models.provider import Provider
from openapi_server.models.zone import Zone
from openapi_server import util


async def get_products_addon_providers_0(request: web.Request, ) -> web.Response:
    """get_products_addon_providers_0

    


    """
    return web.Response(status=200)


async def get_products_addon_providers_provider_id_0(request: web.Request, provider_id) -> web.Response:
    """get_products_addon_providers_provider_id_0

    

    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_products_countries_0(request: web.Request, ) -> web.Response:
    """get_products_countries_0

    


    """
    return web.Response(status=200)


async def get_products_countrycodes_0(request: web.Request, ) -> web.Response:
    """get_products_countrycodes_0

    


    """
    return web.Response(status=200)


async def get_products_instances_0(request: web.Request, _for=None) -> web.Response:
    """get_products_instances_0

    

    :param _for: 
    :type _for: str

    """
    return web.Response(status=200)


async def get_products_instances_type_version_0(request: web.Request, type, version, _for=None, app=None) -> web.Response:
    """get_products_instances_type_version_0

    

    :param type: 
    :type type: str
    :param version: 
    :type version: str
    :param _for: 
    :type _for: str
    :param app: 
    :type app: str

    """
    return web.Response(status=200)


async def get_products_packages_0(request: web.Request, coupon=None, orga_id=None, currency=None) -> web.Response:
    """get_products_packages_0

    

    :param coupon: 
    :type coupon: str
    :param orga_id: 
    :type orga_id: str
    :param currency: 
    :type currency: str

    """
    return web.Response(status=200)


async def get_products_prices_0(request: web.Request, ) -> web.Response:
    """get_products_prices_0

    


    """
    return web.Response(status=200)


async def get_products_zones_0(request: web.Request, ) -> web.Response:
    """get_products_zones_0

    


    """
    return web.Response(status=200)


async def products_addonproviders_provider_id_versions_get_0(request: web.Request, provider_id) -> web.Response:
    """products_addonproviders_provider_id_versions_get_0

    

    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def products_mfa_kinds_get_0(request: web.Request, ) -> web.Response:
    """products_mfa_kinds_get_0

    


    """
    return web.Response(status=200)
