from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_label_from_rate_request_body import CreateLabelFromRateRequestBody
from openapi_server.models.create_label_from_rate_response_body import CreateLabelFromRateResponseBody
from openapi_server.models.create_label_from_shipment_request_body import CreateLabelFromShipmentRequestBody
from openapi_server.models.create_label_from_shipment_response_body import CreateLabelFromShipmentResponseBody
from openapi_server.models.create_label_request_body import CreateLabelRequestBody
from openapi_server.models.create_label_response_body import CreateLabelResponseBody
from openapi_server.models.create_return_label_request_body import CreateReturnLabelRequestBody
from openapi_server.models.create_return_label_response_body import CreateReturnLabelResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_label_by_external_shipment_id_response_body import GetLabelByExternalShipmentIdResponseBody
from openapi_server.models.get_label_by_id_response_body import GetLabelByIdResponseBody
from openapi_server.models.get_tracking_log_from_label_response_body import GetTrackingLogFromLabelResponseBody
from openapi_server.models.label_download_type import LabelDownloadType
from openapi_server.models.label_status import LabelStatus
from openapi_server.models.list_labels_response_body import ListLabelsResponseBody
from openapi_server.models.sort_dir import SortDir
from openapi_server.models.void_label_response_body import VoidLabelResponseBody
from openapi_server import util


async def create_label(request: web.Request, body) -> web.Response:
    """Purchase Label

    Purchase and print a label for shipment

    :param body: 
    :type body: dict | bytes

    """
    body = CreateLabelRequestBody.from_dict(body)
    return web.Response(status=200)


async def create_label_from_rate(request: web.Request, rate_id, body) -> web.Response:
    """Purchase Label with Rate ID

    When retrieving rates for shipments using the &#x60;/rates&#x60; endpoint, the returned information contains a &#x60;rate_id&#x60; property that can be used to generate a label without having to refill in the shipment information repeatedly. 

    :param rate_id: Rate ID
    :type rate_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateLabelFromRateRequestBody.from_dict(body)
    return web.Response(status=200)


async def create_label_from_shipment(request: web.Request, shipment_id, body) -> web.Response:
    """Purchase Label with Shipment ID

    Purchase a label using a shipment ID that has already been created with the desired address and package info. 

    :param shipment_id: Shipment ID
    :type shipment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateLabelFromShipmentRequestBody.from_dict(body)
    return web.Response(status=200)


async def create_return_label(request: web.Request, label_id, body) -> web.Response:
    """Create a return label

    Create a return label

    :param label_id: Label ID
    :type label_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateReturnLabelRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_label_by_external_shipment_id(request: web.Request, external_shipment_id, label_download_type=None) -> web.Response:
    """Get Label By External Shipment ID

    Find a label by using the external shipment id that was used during label creation 

    :param external_shipment_id: 
    :type external_shipment_id: str
    :param label_download_type: 
    :type label_download_type: dict | bytes

    """
    label_download_type = .from_dict(label_download_type)
    return web.Response(status=200)


async def get_label_by_id(request: web.Request, label_id, label_download_type=None) -> web.Response:
    """Get Label By ID

    Retrieve information for individual labels.

    :param label_id: Label ID
    :type label_id: str
    :param label_download_type: 
    :type label_download_type: dict | bytes

    """
    label_download_type = .from_dict(label_download_type)
    return web.Response(status=200)


async def get_tracking_log_from_label(request: web.Request, label_id) -> web.Response:
    """Get Label Tracking Information

    Retrieve the label&#39;s tracking information

    :param label_id: Label ID
    :type label_id: str

    """
    return web.Response(status=200)


async def list_labels(request: web.Request, label_status=None, service_code=None, carrier_id=None, tracking_number=None, batch_id=None, rate_id=None, shipment_id=None, warehouse_id=None, created_at_start=None, created_at_end=None, page=None, page_size=None, sort_dir=None, sort_by=None) -> web.Response:
    """List labels

    This endpoint returns a list of labels that you&#39;ve [created](https://www.shipengine.com/docs/labels/create-a-label/). You can optionally filter the results as well as control their sort order and the number of results returned at a time.  By default, all labels are returned, 25 at a time, starting with the most recently created ones.  You can combine multiple filter options to narrow-down the results.  For example, if you only want to get your UPS labels for your east coast warehouse you could query by both &#x60;warehouse_id&#x60; and &#x60;carrier_id&#x60; 

    :param label_status: Only return labels that are currently in the specified status
    :type label_status: dict | bytes
    :param service_code: Only return labels for a specific [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/)
    :type service_code: str
    :param carrier_id: Only return labels for a specific [carrier account](https://www.shipengine.com/docs/carriers/setup/)
    :type carrier_id: str
    :param tracking_number: Only return labels with a specific tracking number
    :type tracking_number: str
    :param batch_id: Only return labels that were created in a specific [batch](https://www.shipengine.com/docs/labels/bulk/)
    :type batch_id: str
    :param rate_id: Rate ID
    :type rate_id: str
    :param shipment_id: Shipment ID
    :type shipment_id: str
    :param warehouse_id: Only return labels that originate from a specific [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/)
    :type warehouse_id: str
    :param created_at_start: Only return labels that were created on or after a specific date/time
    :type created_at_start: str
    :param created_at_end: Only return labels that were created on or before a specific date/time
    :type created_at_end: str
    :param page: Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned. 
    :type page: int
    :param page_size: The number of results to return per response.
    :type page_size: int
    :param sort_dir: Controls the sort order of the query.
    :type sort_dir: dict | bytes
    :param sort_by: Controls which field the query is sorted by.
    :type sort_by: str

    """
    label_status = .from_dict(label_status)
    created_at_start = util.deserialize_datetime(created_at_start)
    created_at_end = util.deserialize_datetime(created_at_end)
    sort_dir = .from_dict(sort_dir)
    return web.Response(status=200)


async def void_label(request: web.Request, label_id) -> web.Response:
    """Void a Label By ID

    Void a label by ID to get a refund.

    :param label_id: Label ID
    :type label_id: str

    """
    return web.Response(status=200)
