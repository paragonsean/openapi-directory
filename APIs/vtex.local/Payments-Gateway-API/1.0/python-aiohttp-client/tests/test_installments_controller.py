# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_request_value import InvalidRequestValue
from openapi_server.models.valid_request import ValidRequest


pytestmark = pytest.mark.asyncio

async def test_installmentsoptions(client):
    """Test case for installmentsoptions

    Installments options
    """
    params = [('request.value', 10),
                    ('request.salesChannel', 1),
                    ('request.paymentDetails[0].id', 2),
                    ('request.paymentDetails[0].value', 10),
                    ('request.paymentDetails[0].bin', 411111)]
    headers = { 
        'Accept': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/installments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

