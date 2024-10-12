from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.store_tracking_status import StoreTrackingStatus
from openapi_server.models.tracked_clicks import TrackedClicks
from openapi_server.models.tracked_external_orders import TrackedExternalOrders
from openapi_server.models.tracked_orders import TrackedOrders
from openapi_server.models.tracking_status import TrackingStatus
from openapi_server import util


async def get_store_tracked_clicks(request: web.Request, store_id, count=None) -> web.Response:
    """Get the latest tracked clicks

    

    :param store_id: Your store identifier
    :type store_id: str
    :param count: The amount of clicks to retrieve
    :type count: int

    """
    return web.Response(status=200)


async def get_store_tracked_external_orders(request: web.Request, store_id, count=None) -> web.Response:
    """Get the latest tracked external orders

    

    :param store_id: Your store identifier
    :type store_id: str
    :param count: The amount of external orders to retrieve
    :type count: int

    """
    return web.Response(status=200)


async def get_store_tracked_orders(request: web.Request, store_id, count=None) -> web.Response:
    """Get the latest tracked orders

    

    :param store_id: Your store identifier
    :type store_id: str
    :param count: The amount of orders to retrieve
    :type count: int

    """
    return web.Response(status=200)


async def get_store_tracking_status(request: web.Request, store_id) -> web.Response:
    """Get the synchronization status of clicks and orders of a store

    Clicks and orders are eventually consistent. \\ This operation gets the current state of projections for a store. 

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def get_tracking_status(request: web.Request, ) -> web.Response:
    """Get the global synchronization status of clicks and orders

    Clicks and orders are eventually consistent. \\ This operation gets the current global state of projections. 


    """
    return web.Response(status=200)
