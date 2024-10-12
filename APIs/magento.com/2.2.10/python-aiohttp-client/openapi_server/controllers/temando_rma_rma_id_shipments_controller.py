from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_rma_rma_shipment_management_v1_assign_shipment_ids_put_request import TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest
from openapi_server import util


async def temando_shipping_rma_rma_shipment_management_v1_assign_shipment_ids_put(request: web.Request, rma_id, body=None) -> web.Response:
    """temando/rma/{rmaId}/shipments

    Assign platform shipment IDs to a core RMA entity.

    :param rma_id: 
    :type rma_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest.from_dict(body)
    return web.Response(status=200)
