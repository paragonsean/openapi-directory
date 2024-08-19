from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_shipments_request_body import CreateShipmentsRequestBody
from openapi_server.models.create_shipments_response_body import CreateShipmentsResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_shipment_by_external_id_response_body import GetShipmentByExternalIdResponseBody
from openapi_server.models.get_shipment_by_id_response_body import GetShipmentByIdResponseBody
from openapi_server.models.list_shipment_rates_response_body import ListShipmentRatesResponseBody
from openapi_server.models.list_shipments_response_body import ListShipmentsResponseBody
from openapi_server.models.parse_shipment_request_body import ParseShipmentRequestBody
from openapi_server.models.parse_shipment_response_body import ParseShipmentResponseBody
from openapi_server.models.shipment_status import ShipmentStatus
from openapi_server.models.shipments_sort_by import ShipmentsSortBy
from openapi_server.models.sort_dir import SortDir
from openapi_server.models.tag_shipment_response_body import TagShipmentResponseBody
from openapi_server.models.update_shipment_request_body import UpdateShipmentRequestBody
from openapi_server.models.update_shipment_response_body import UpdateShipmentResponseBody
from openapi_server import util


async def cancel_shipments(request: web.Request, shipment_id) -> web.Response:
    """Cancel a Shipment

    Mark a shipment cancelled, if it is no longer needed or being used by your organized. Any label associated with the shipment needs to be voided first An example use case would be if a batch label creation job is going to run at a set time and only queries &#x60;pending&#x60; shipments. Marking a shipment as cancelled would remove it from this process 

    :param shipment_id: Shipment ID
    :type shipment_id: str

    """
    return web.Response(status=200)


async def create_shipments(request: web.Request, body) -> web.Response:
    """Create Shipments

    Create one or multiple shipments.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateShipmentsRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_shipment_by_external_id(request: web.Request, external_shipment_id) -> web.Response:
    """Get Shipment By External ID

    Query Shipments created using your own custom ID convention using this endpint

    :param external_shipment_id: 
    :type external_shipment_id: str

    """
    return web.Response(status=200)


async def get_shipment_by_id(request: web.Request, shipment_id) -> web.Response:
    """Get Shipment By ID

    Get an individual shipment based on its ID

    :param shipment_id: Shipment ID
    :type shipment_id: str

    """
    return web.Response(status=200)


async def list_shipment_rates(request: web.Request, shipment_id, created_at_start=None) -> web.Response:
    """Get Shipment Rates

    Get Rates for the shipment information associated with the shipment ID

    :param shipment_id: Shipment ID
    :type shipment_id: str
    :param created_at_start: Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
    :type created_at_start: str

    """
    created_at_start = util.deserialize_datetime(created_at_start)
    return web.Response(status=200)


async def list_shipments(request: web.Request, shipment_status=None, batch_id=None, tag=None, created_at_start=None, created_at_end=None, modified_at_start=None, modified_at_end=None, page=None, page_size=None, sales_order_id=None, sort_dir=None, sort_by=None) -> web.Response:
    """List Shipments

    Get list of Shipments

    :param shipment_status: 
    :type shipment_status: dict | bytes
    :param batch_id: Batch ID
    :type batch_id: str
    :param tag: Search for shipments based on the custom tag added to the shipment object
    :type tag: str
    :param created_at_start: Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
    :type created_at_start: str
    :param created_at_end: Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)
    :type created_at_end: str
    :param modified_at_start: Used to create a filter for when a resource was modified (ex. A shipment that was modified after a certain time)
    :type modified_at_start: str
    :param modified_at_end: Used to create a filter for when a resource was modified (ex. A shipment that was modified before a certain time)
    :type modified_at_end: str
    :param page: Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned. 
    :type page: int
    :param page_size: The number of results to return per response.
    :type page_size: int
    :param sales_order_id: Sales Order ID
    :type sales_order_id: str
    :param sort_dir: Controls the sort order of the query.
    :type sort_dir: dict | bytes
    :param sort_by: 
    :type sort_by: dict | bytes

    """
    shipment_status = .from_dict(shipment_status)
    created_at_start = util.deserialize_datetime(created_at_start)
    created_at_end = util.deserialize_datetime(created_at_end)
    modified_at_start = util.deserialize_datetime(modified_at_start)
    modified_at_end = util.deserialize_datetime(modified_at_end)
    sort_dir = .from_dict(sort_dir)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def parse_shipment(request: web.Request, body) -> web.Response:
    """Parse shipping info

    The shipment-recognition API makes it easy for you to extract shipping data from unstructured text, including people&#39;s names, addresses, package weights and dimensions, insurance and delivery requirements, and more.  Data often enters your system as unstructured text (for example: emails, SMS messages, support tickets, or other documents). ShipEngine&#39;s shipment-recognition API helps you extract meaningful, structured data from this unstructured text. The parsed shipment data is returned in the same structure that&#39;s used for other ShipEngine APIs, so you can easily use the parsed data to create a shipping label.  &gt; **Note:** Shipment recognition is currently supported for the United States, Canada, Australia, New Zealand, the United Kingdom, and Ireland. 

    :param body: The only required field is &#x60;text&#x60;, which is the text to be parsed. You can optionally also provide a &#x60;shipment&#x60; containing any already-known values. For example, you probably already know the &#x60;ship_from&#x60; address, and you may also already know what carrier and service you want to use. 
    :type body: dict | bytes

    """
    body = ParseShipmentRequestBody.from_dict(body)
    return web.Response(status=200)


async def tag_shipment(request: web.Request, shipment_id, tag_name) -> web.Response:
    """Add Tag to Shipment

    Add a tag to the shipment object

    :param shipment_id: Shipment ID
    :type shipment_id: str
    :param tag_name: 
    :type tag_name: str

    """
    return web.Response(status=200)


async def untag_shipment(request: web.Request, shipment_id, tag_name) -> web.Response:
    """Remove Tag from Shipment

    Remove an existing tag from the Shipment object

    :param shipment_id: Shipment ID
    :type shipment_id: str
    :param tag_name: 
    :type tag_name: str

    """
    return web.Response(status=200)


async def update_shipment(request: web.Request, shipment_id, body) -> web.Response:
    """Update Shipment By ID

    Update a shipment object based on its ID

    :param shipment_id: Shipment ID
    :type shipment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateShipmentRequestBody.from_dict(body)
    return web.Response(status=200)
