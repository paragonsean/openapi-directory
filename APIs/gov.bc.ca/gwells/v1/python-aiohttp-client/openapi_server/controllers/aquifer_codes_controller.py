from typing import List, Dict
from aiohttp import web

from openapi_server.models.aquifer_codes_demand_list200_response import AquiferCodesDemandList200Response
from openapi_server.models.aquifer_codes_materials_list200_response import AquiferCodesMaterialsList200Response
from openapi_server.models.aquifer_codes_productivity_list200_response import AquiferCodesProductivityList200Response
from openapi_server.models.aquifer_codes_quality_concerns_list200_response import AquiferCodesQualityConcernsList200Response
from openapi_server.models.aquifer_codes_subtypes_list200_response import AquiferCodesSubtypesList200Response
from openapi_server.models.aquifer_codes_vulnerability_list200_response import AquiferCodesVulnerabilityList200Response
from openapi_server.models.aquifer_codes_water_use_list200_response import AquiferCodesWaterUseList200Response
from openapi_server import util


async def aquifer_codes_demand_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """aquifer_codes_demand_list

    return a list of aquifer demand codes

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def aquifer_codes_materials_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """aquifer_codes_materials_list

    return a list of aquifer material codes

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def aquifer_codes_productivity_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """aquifer_codes_productivity_list

    return a list of aquifer productivity codes

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def aquifer_codes_quality_concerns_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """aquifer_codes_quality_concerns_list

    return a list of quality concern codes

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def aquifer_codes_subtypes_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """aquifer_codes_subtypes_list

    return a list of aquifer subtype codes

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def aquifer_codes_vulnerability_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """aquifer_codes_vulnerability_list

    return a list of aquifer vulnerability codes

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def aquifer_codes_water_use_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """aquifer_codes_water_use_list

    return a list of water use codes

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)
