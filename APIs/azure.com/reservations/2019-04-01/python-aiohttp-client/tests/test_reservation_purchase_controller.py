# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.purchase_request import PurchaseRequest
from openapi_server.models.reservation_order_response import ReservationOrderResponse


pytestmark = pytest.mark.asyncio

async def test_reservation_order_purchase(client):
    """Test case for reservation_order_purchase

    Purchase `ReservationOrder`
    """
    body = {"location":"location","sku":{"name":"name"},"properties":{"reservedResourceType":"VirtualMachines","reservedResourceProperties":{"instanceFlexibility":"On"},"billingScopeId":"billingScopeId","quantity":0,"appliedScopes":["appliedScopes","appliedScopes"],"displayName":"displayName","appliedScopeType":"Single","billingPlan":"Upfront","term":"P1Y","renew":False}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}'.format(reservation_order_id='reservation_order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

