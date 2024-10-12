from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_vod_promotion_request import CreateVodPromotionRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_promotion import OnDemandPromotion
from openapi_server.models.on_demand_promotion_code import OnDemandPromotionCode
from openapi_server import util


async def create_vod_promotion(request: web.Request, ondemand_id, body) -> web.Response:
    """Add a promotion to an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateVodPromotionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_vod_promotion(request: web.Request, ondemand_id, promotion_id) -> web.Response:
    """Remove a promotion from an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param promotion_id: The ID of the promotion.
    :type promotion_id: 

    """
    return web.Response(status=200)


async def get_vod_promotion(request: web.Request, ondemand_id, promotion_id) -> web.Response:
    """Get a specific promotion on an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param promotion_id: The ID of the promotion.
    :type promotion_id: 

    """
    return web.Response(status=200)


async def get_vod_promotion_codes(request: web.Request, ondemand_id, promotion_id, page=None, per_page=None) -> web.Response:
    """Get all the codes of a promotion on an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param promotion_id: The ID of the promotion.
    :type promotion_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_vod_promotions(request: web.Request, ondemand_id, filter, page=None, per_page=None) -> web.Response:
    """Get all the promotions on an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param filter: The filter to apply to the results.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)
