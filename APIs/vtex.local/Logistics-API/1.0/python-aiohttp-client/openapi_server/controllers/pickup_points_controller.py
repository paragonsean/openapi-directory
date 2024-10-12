from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_update import CreateUpdate
from openapi_server.models.create_update_pickup_point_request import CreateUpdatePickupPointRequest
from openapi_server.models.get_by_id1 import GetById1
from openapi_server.models.list_all_pickup_ppoints200_response_inner import ListAllPickupPpoints200ResponseInner
from openapi_server import util


async def create_update_pickup_point(request: web.Request, content_type, accept, pickup_point_id, body) -> web.Response:
    """Create/Update Pickup Point

    Creates or updates [pickup points](https://help.vtex.com/en/subcategory/pickup-points--1c5Btie9ou2Gg2iUo0ggqM#) in your store by Pickup Point ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param pickup_point_id: Pickup Point ID. Cannot contain spaces.
    :type pickup_point_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateUpdatePickupPointRequest.from_dict(body)
    return web.Response(status=200)


async def delete(request: web.Request, content_type, accept, pickup_point_id) -> web.Response:
    """Delete Pickup Point

    Deletes a given pickup point for your store, by pickup point ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param pickup_point_id: 
    :type pickup_point_id: str

    """
    return web.Response(status=200)


async def get_by_id(request: web.Request, content_type, accept, pickup_point_id) -> web.Response:
    """List Pickup Point By ID

    Lists your store&#39;s pickup points while searching by ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param pickup_point_id: 
    :type pickup_point_id: str

    """
    return web.Response(status=200)


async def getpaged(request: web.Request, page, page_size, keyword, content_type, accept) -> web.Response:
    """List paged Pickup Points

    Lists paged pickup points in your store.

    :param page: 
    :type page: str
    :param page_size: 
    :type page_size: str
    :param keyword: 
    :type keyword: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def list_all_pickup_ppoints(request: web.Request, content_type, accept) -> web.Response:
    """List all pickup points

    Lists all of your store&#39;s pickup points.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)
