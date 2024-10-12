from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_vod_regions_request import DeleteVodRegionsRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_region import OnDemandRegion
from openapi_server.models.set_vod_regions_request import SetVodRegionsRequest
from openapi_server import util


async def add_vod_region(request: web.Request, country, ondemand_id) -> web.Response:
    """Add a specific region to an On Demand page

    

    :param country: The country code.
    :type country: str
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def delete_vod_region(request: web.Request, country, ondemand_id) -> web.Response:
    """Remove a specific region from an On Demand page

    

    :param country: The country code.
    :type country: str
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def delete_vod_regions(request: web.Request, ondemand_id, body=None) -> web.Response:
    """Remove a list of regions from an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteVodRegionsRequest.from_dict(body)
    return web.Response(status=200)


async def get_region(request: web.Request, country) -> web.Response:
    """Get a specific On Demand region

    

    :param country: The country code.
    :type country: str

    """
    return web.Response(status=200)


async def get_regions(request: web.Request, ) -> web.Response:
    """Get all the On Demand regions

    


    """
    return web.Response(status=200)


async def get_vod_region(request: web.Request, country, ondemand_id) -> web.Response:
    """Get a specific region of an On Demand page

    Checks whether an On Demand page belongs to a region.

    :param country: The country code.
    :type country: str
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def get_vod_regions(request: web.Request, ondemand_id) -> web.Response:
    """Get all the regions of an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def set_vod_regions(request: web.Request, ondemand_id, body) -> web.Response:
    """Add a list of regions to an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = SetVodRegionsRequest.from_dict(body)
    return web.Response(status=200)
