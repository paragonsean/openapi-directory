from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_update_polygon_request import CreateUpdatePolygonRequest
from openapi_server import util


async def create_update_polygon(request: web.Request, content_type, accept, body) -> web.Response:
    """Create/update polygon

    Creates or updates your store&#39;s polygons by geoshape coordinates and polygon name.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateUpdatePolygonRequest.from_dict(body)
    return web.Response(status=200)


async def delete_polygon(request: web.Request, content_type, accept, polygon_name) -> web.Response:
    """Delete polygon

    Deletes polygon set up in your store, by polygon name.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param polygon_name: 
    :type polygon_name: str

    """
    return web.Response(status=200)


async def paged_polygons(request: web.Request, page, per_page, content_type, accept) -> web.Response:
    """List paged polygons

    Lists stored polygons.

    :param page: 
    :type page: str
    :param per_page: 
    :type per_page: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def polygonby_id(request: web.Request, content_type, accept, polygon_name) -> web.Response:
    """List polygon by ID

    Lists your store&#39;s polygons by searching through polygon name

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param polygon_name: 
    :type polygon_name: str

    """
    return web.Response(status=200)
