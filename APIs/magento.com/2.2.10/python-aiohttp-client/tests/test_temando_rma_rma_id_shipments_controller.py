# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_rma_rma_shipment_management_v1_assign_shipment_ids_put_request import TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_temando_shipping_rma_rma_shipment_management_v1_assign_shipment_ids_put(client):
    """Test case for temando_shipping_rma_rma_shipment_management_v1_assign_shipment_ids_put

    temando/rma/{rmaId}/shipments
    """
    body = openapi_server.TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/temando/rma/{rma_id}/shipments'.format(rma_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

