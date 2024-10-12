# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_tracking_status import UpdateTrackingStatus
from openapi_server.models.update_tracking_status_request import UpdateTrackingStatusRequest


pytestmark = pytest.mark.asyncio

async def test_update_tracking_status(client):
    """Test case for update_tracking_status

    Update order tracking status
    """
    body = {"deliveredDate":null,"events":[{"city":"Rio de Janeiro","date":"2015-06-23","description":"Coletado pela transportadora","state":"RJ"},{"city":"Sao Paulo","date":"2015-06-24","description":"A caminho de Curitiba","state":"SP"}],"isDelivered":False}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/oms/pvt/orders/{order_id}/invoice/{invoice_number}/tracking'.format(order_id='1172452900788-01', invoice_number='000030711'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

