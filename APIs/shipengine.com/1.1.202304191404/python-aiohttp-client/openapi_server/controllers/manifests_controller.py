from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_manifest_request_body import CreateManifestRequestBody
from openapi_server.models.create_manifest_response_body import CreateManifestResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_manifest_by_id_response_body import GetManifestByIdResponseBody
from openapi_server.models.list_manifests_response_body import ListManifestsResponseBody
from openapi_server import util


async def create_manifest(request: web.Request, body) -> web.Response:
    """Create Manifest

    Each ShipEngine manifest is created for a specific warehouse, so you&#39;ll need to provide the warehouse_id rather than the ship_from address. You can create a warehouse for each location that you want to create manifests for. 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateManifestRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_manifest_by_id(request: web.Request, manifest_id) -> web.Response:
    """Get Manifest By Id

    Get Manifest By Id

    :param manifest_id: The Manifest Id
    :type manifest_id: str

    """
    return web.Response(status=200)


async def get_manifest_request_by_id(request: web.Request, manifest_request_id) -> web.Response:
    """Get Manifest Request By Id

    Get Manifest Request By Id

    :param manifest_request_id: The Manifest Request Id
    :type manifest_request_id: str

    """
    return web.Response(status=200)


async def list_manifests(request: web.Request, warehouse_id=None, ship_date_start=None, ship_date_end=None, created_at_start=None, created_at_end=None, carrier_id=None, page=None, page_size=None, label_ids=None) -> web.Response:
    """List Manifests

    Similar to querying shipments, we allow you to query manifests since there will likely be a large number over a long period of time.

    :param warehouse_id: Warehouse ID
    :type warehouse_id: str
    :param ship_date_start: ship date start range
    :type ship_date_start: str
    :param ship_date_end: ship date end range
    :type ship_date_end: str
    :param created_at_start: Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
    :type created_at_start: str
    :param created_at_end: Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)
    :type created_at_end: str
    :param carrier_id: Carrier ID
    :type carrier_id: str
    :param page: Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned. 
    :type page: int
    :param page_size: The number of results to return per response.
    :type page_size: int
    :param label_ids: 
    :type label_ids: List[str]

    """
    ship_date_start = util.deserialize_datetime(ship_date_start)
    ship_date_end = util.deserialize_datetime(ship_date_end)
    created_at_start = util.deserialize_datetime(created_at_start)
    created_at_end = util.deserialize_datetime(created_at_end)
    return web.Response(status=200)
