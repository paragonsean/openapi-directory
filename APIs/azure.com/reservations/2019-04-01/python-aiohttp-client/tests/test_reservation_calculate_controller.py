# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calculate_price_response import CalculatePriceResponse
from openapi_server.models.error import Error
from openapi_server.models.purchase_request import PurchaseRequest


pytestmark = pytest.mark.asyncio

async def test_reservation_order_calculate(client):
    """Test case for reservation_order_calculate

    Calculate price for a `ReservationOrder`.
    """
    body = {"location":"location","sku":{"name":"name"},"properties":{"reservedResourceType":"VirtualMachines","reservedResourceProperties":{"instanceFlexibility":"On"},"billingScopeId":"billingScopeId","quantity":0,"appliedScopes":["appliedScopes","appliedScopes"],"displayName":"displayName","appliedScopeType":"Single","billingPlan":"Upfront","term":"P1Y","renew":False}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Capacity/calculatePrice',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

