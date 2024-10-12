# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calculate_sla200_response_inner_inner import CalculateSLA200ResponseInnerInner
from openapi_server.models.calculate_sla_request1 import CalculateSLARequest1


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_calculate_sla(client):
    """Test case for calculate_sla

    Calculate SLA
    """
    body = [{"items":[{"additionalHandlingTime":"00:00:00","dimension":{"height":5,"length":17,"weight":150,"width":17},"groupItemId":null,"id":"1","kitItem":[{"additionalHandlingTime":"00:00:00","dimension":{"height":5,"length":17,"weight":150,"width":17},"groupItemId":null,"id":"2000042","kitItem":[],"price":0,"quantity":1},{"additionalHandlingTime":"00:00:00","dimension":{"height":5,"length":17,"weight":150,"width":17},"groupItemId":null,"id":"2390059","kitItem":[],"price":0,"quantity":1}],"price":0,"quantity":1}],"location":{"country":"BRA","point":[-43.32475950000003,-22.9999575],"zipCode":"22780084"},"salesChannel":"1"}]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/shipping/calculate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

