from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.shipment_expand_vo import ShipmentExpandVO
from openapi_server.models.shipment_list_vo import ShipmentListVO
from openapi_server.models.shipment_location_persist_vo import ShipmentLocationPersistVO
from openapi_server.models.shipment_location_post_persist_vo import ShipmentLocationPostPersistVO
from openapi_server.models.shipment_locations_post_result_vo import ShipmentLocationsPOSTResultVO
from openapi_server import util


async def get_shipment(request: web.Request, workgroup_id, project_id, shipment_id) -> web.Response:
    """Get a specific shipment.

    Get a specific shipment.

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param shipment_id: 
    :type shipment_id: str

    """
    return web.Response(status=200)


async def get_shipment_list(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List shipments of project

    List shipments of project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def post_shipment(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Create a shipment

    Create a shipment

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShipmentLocationPostPersistVO.from_dict(body)
    return web.Response(status=200)


async def put_shipment_location(request: web.Request, workgroup_id, project_id, shipment_id, location_id, body=None) -> web.Response:
    """Update a specific shipment location

    Update a specific shipment location

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param shipment_id: 
    :type shipment_id: str
    :param location_id: 
    :type location_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShipmentLocationPersistVO.from_dict(body)
    return web.Response(status=200)
